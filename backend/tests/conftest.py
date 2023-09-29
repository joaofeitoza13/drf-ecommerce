import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")

import django  # noqa: E402

django.setup()

import pytest  # noqa: E402
from pytest_factoryboy import register  # noqa: E402
from rest_framework.test import APIClient  # noqa: E402

from .factories import (
    BrandFactory,
    CategoryFactory,
    ProductFactory,
    ProductLineFactory,
)  # noqa: E402

register(CategoryFactory)  # It is registered as snake_case => category_factory
register(BrandFactory)  # It is registered as snake_case => category_factory
register(ProductFactory)  # It is registered as snake_case => category_factory
register(ProductLineFactory)  # It is registered as snake_case => category_line_factory


@pytest.fixture
def api_client():
    return APIClient
