import json
import subprocess
from datetime import datetime

from django.shortcuts import render

from catalog.models import Product, Contact, Category


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


def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')

        # Получаем текущую дату и время
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Создаем список, содержащий словарь с данными
        product_data = [
            {
                'name': name,
                'description': description,
                'photo': '',
                'category': category,
                'price': price,
                'created_at': current_datetime,
                'modified_at': current_datetime
            }
        ]

        with open('catalog/product_data.json', 'w', encoding='utf-8') as file:
            json.dump(product_data, file)

        # После сохранения данных выполняем команду fill с помощью subprocess
        fill_command = 'python3 manage.py fill'
        try:
            subprocess.run(fill_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка выполнения команды fill: {e}")

    context = {
        'object_list': Category.objects.all(),
        'title': 'Create your product',
    }
    return render(request, 'catalog/create_product.html', context)
