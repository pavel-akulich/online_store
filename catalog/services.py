from django.conf import settings
from django.core.cache import cache
from catalog.models import Category


def cache_categories():
    """
    Сервисная функция для выборки и кэширования категорий продуктов
    """
    if settings.CACHE_ENABLED:
        key = 'categories_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()

    return category_list
