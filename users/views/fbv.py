import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse

from users.models import User


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Your new password',
        message=f'your new password: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:home'))


def verify(request):
    if request.method == 'POST':
        number = request.POST.get('number')
    try:
        user = User.objects.get(verification_code=number)
        user.verified = True
        user.save()
        return redirect(reverse('users:login'))
    except:
        return render(request, 'users/verification.html')
