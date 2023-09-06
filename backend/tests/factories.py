import factory
from apps.product.models import Brand, Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "test_category_name"


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = "test_brand_name"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "test_product_name"
    description = "test_product_description"
    is_digital = True
    """
    The usage of the SubFactory assures the new
    object is created isolated and independent.
    Avoiding cyclid creations.
    """
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
