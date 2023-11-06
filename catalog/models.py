from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """Модель для категорий"""
    name = models.CharField(max_length=250, verbose_name='наименование категории')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        """Строковое представление объекта"""
        return f'Категория {self.name}'

    class Meta:
        """Мета класс настройка для именования объектов"""
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Модель для продуктов"""
    name = models.CharField(max_length=250, verbose_name='наименование продукта')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    photo = models.ImageField(**NULLABLE, upload_to='products/', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        """Строковое представление объекта"""
        return f'{self.name} из категории {self.category}'

    class Meta:
        """Мета класс настройка для именования объектов"""
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Version(models.Model):
    """Модель для версий продукта"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    version_number = models.FloatField(verbose_name="Номер версии")
    version_name = models.CharField(max_length=150, verbose_name="Название версии")

    is_active = models.BooleanField(default=False, verbose_name='Признак активности версии')

    def __str__(self):
        """Строковое представление объекта"""
        return f'{self.version_name} - {self.version_number}'

    class Meta:
        """Мета класс настройка для именования объектов"""
        verbose_name = "Версия"
        verbose_name_plural = "Версии"


class Contact(models.Model):
    """Модель для контактов"""
    name = models.CharField(max_length=150, verbose_name='имя контакта')
    email = models.EmailField(verbose_name='email контакта')
    phone = models.CharField(max_length=30, verbose_name='номер телефона')
    address = models.TextField(verbose_name='адрес')

    def __str__(self):
        """Строковое представление объекта"""
        return f'Имя:{self.name}, email:{self.email}, телефон:{self.phone}'

    class Meta:
        """Мета класс настройка для именования объектов"""
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ('name',)
