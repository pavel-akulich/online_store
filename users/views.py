import random
import string

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, View

from users.forms import UserRegisterForm, UserForm, VerificationForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Log in to account'
    }


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    extra_context = {
        'title': 'Registration'
    }
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        generate_code = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        user.verify_code = generate_code
        user.save()

        # Отправляем письмо с кодом активации
        send_mail(
            subject='Код верификации',
            message=f'Пожалуйста, для вашей верификации и активации аккаунта введите код: {generate_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return redirect(reverse('users:verification', kwargs={'pk': user.pk}))


class UserVerifyView(View):
    template_name = 'users/verification.html'
    extra_context = {
        'title': 'Verification'
    }

    def get(self, request, *args, **kwargs):
        form = VerificationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = VerificationForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['verify_code']
            user_pk = kwargs.get('pk')
            user = get_object_or_404(User, pk=user_pk)

            if entered_code == user.verify_code:
                user.is_active = True
                user.save()
                messages.success(request, 'Аккаунт успешно активирован!')
                return redirect(reverse('users:login'))
            else:
                messages.error(request, 'Неверный код верификации. Попробуйте снова.')

        return render(request, self.template_name, {'form': form})


class UserUpdateView(UpdateView):
    model = User
    extra_context = {
        'title': 'My profile'
    }
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


class GenerateNewPasswordView(View):
    def generate_random_password(self, length=12):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def get(self, request, *args, **kwargs):
        new_password = self.generate_random_password()
        send_mail(
            subject='Password reset',
            message=f'Your new password: {new_password}\n'
                    f'Login with your new password',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email]
        )
        request.user.set_password(new_password)
        request.user.save()
        return redirect(reverse('users:login'))
