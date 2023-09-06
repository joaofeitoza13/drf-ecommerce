import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")

import django  # noqa: E402

django.setup()

from pytest_factoryboy import register  # noqa: E402

from .factories import BrandFactory, CategoryFactory, ProductFactory  # noqa: E402

register(CategoryFactory)  # It is registered as snake_case => category_factory
register(BrandFactory)  # It is registered as snake_case => category_factory
register(ProductFactory)  # It is registered as snake_case => category_factory
