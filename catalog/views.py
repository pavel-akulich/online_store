from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'name = {name}, phone = {phone}, message = {message}')

        # Открываем файл для записи данных из формы обратной связи
        with open('feedbacks.txt', 'a') as file:
            file.write(f'name = {name}, phone = {phone}, message = {message}\n')

    return render(request, 'catalog/contacts.html')
