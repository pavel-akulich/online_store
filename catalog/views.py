from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    # выборка последних 5 товаров и вывод их в консоль
    latest_products = Product.objects.order_by('-created_at')[:5]
    for product in latest_products:
        print(f'Название продукта: {product.name}, стоимость: {product.price}')

    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'name = {name}, phone = {phone}, message = {message}')

        # Открываем текстовый файл для записи данных из формы обратной связи
        with open('feedbacks.txt', 'a') as file:
            file.write(f'name = {name}, phone = {phone}, message = {message}\n')

    # получаем контакты из админки для последующего вывода в шаблоне
    contacts_for_support = Contact.objects.all()

    return render(request, 'catalog/contacts.html', {'contacts': contacts_for_support})
