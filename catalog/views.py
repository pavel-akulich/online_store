from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from catalog.models import Product, Contact


class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'My store'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.order_by('-created_at')[:4]
        return context_data


class ContactPageView(TemplateView):
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


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Catalog of My Store'
    }


class ProductCreateView(CreateView):
    extra_context = {
        'title': 'Create a Product'
    }
    model = Product
    fields = ('name', 'description', 'photo', 'category', 'price')
    success_url = reverse_lazy('catalog:catalog_products')
