import factory
from apps.product.models import Brand, Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "test_category_name_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: "test_brand_name_%d" % n)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: "test_product_name_%d" % n)
    description = factory.Sequence(lambda n: "test_product_description_%d" % n)
    is_digital = True
    """
    The usage of the SubFactory assures the new
    object is created isolated and independent.
    Avoiding cyclid creations.
    """
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
