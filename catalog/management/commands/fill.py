import codecs
import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    """Команда для добавления нового товара из формы на странице магазина в каталог"""

    def handle(self, *args, **kwargs):
        with open('catalog/product_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                category_name = codecs.decode(item['category'], 'unicode_escape').encode('latin1').decode('utf-8')

                # Создаем экземпляр модели Category на основе имени категории
                category, created = Category.objects.get_or_create(name=category_name)

                product = Product(
                    name=item['name'],
                    description=item['description'],
                    photo=item['photo'],
                    category=category,
                    price=item['price'],
                    created_at=item['created_at'],
                    modified_at=item['modified_at']
                )

                product.save()
