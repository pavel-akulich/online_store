from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    # Вывод 4 последних добавленных продуктов на главную страницу
    latest_products = Product.objects.order_by('-created_at')[:4]
    context = {
        'object_list': latest_products,
        'title': 'My store'
    }

    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Открываем текстовый файл для записи данных из формы обратной связи
        with open('feedbacks.txt', 'a') as file:
            file.write(f'name = {name}, phone = {phone}, message = {message}\n')

    # получаем контакты из админки для последующего вывода в шаблоне
    contacts_for_support = Contact.objects.all()

    context = {
        'contacts': contacts_for_support,
        'title': 'Contacts My Store',
    }

    return render(request, 'catalog/contacts.html', context)


def catalog_products(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Catalog of My Store',
    }
    return render(request, 'catalog/catalog_products.html', context)
