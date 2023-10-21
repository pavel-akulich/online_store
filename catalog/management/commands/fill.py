from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    """Команда записи категорий в БД"""

    def handle(self, *args, **kwargs):
        # добавляем категории
        categories_list = [
            {'name': 'Компьютерные мониторы'},
            {'name': 'Компьютерные мышки'},
            {'name': 'Компьютерные клавиатуры'},
            {'name': 'Компьютерные принтеры'}
        ]

        Category.objects.all().delete()

        categories_for_create = []
        for category_item in categories_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_for_create)
