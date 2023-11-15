from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contact, Version, Category
from catalog.services import cache_categories


class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'My store'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.order_by('-created_at')[:4]
        return context_data


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    extra_context = {
        'title': 'Categories our products',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category'] = cache_categories()
        return context_data


class ContactPageView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Contacts My Store'
    }

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        with open('feedbacks.txt', 'a') as file:
            file.write(f'name = {name}, phone = {phone}, message = {message}\n')

        return HttpResponseRedirect(self.request.path_info)  # Перенаправит обратно на ту же страницу после POST запроса

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Contact.objects.all()
        return context_data


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    extra_context = {
        'title': 'Catalog of My Store'
    }


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    extra_context = {
        'title': 'Create a Product'
    }
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog_products')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    extra_context = {
        'title': 'View product details'
    }


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        'title': 'Edit product',
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if not (self.object.owner == self.request.user or
                self.request.user.is_superuser or
                self.request.user.groups.filter(name='moderator')):
            raise Http404('У вас нет доступа к этой странице')
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view_product', args=[self.kwargs.get('pk')])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog_products')
    extra_context = {
        'title': 'Delete product',
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404('У вас нет доступа к этой странице')
        return self.object
