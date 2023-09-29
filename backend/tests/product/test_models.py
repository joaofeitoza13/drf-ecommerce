import pytest

pytestmark = pytest.mark.django_db

# Testing example
# class TestClass:
#     def test_class_method():
#     1 - arrange
#     2 - act
#     3 - assert


class TestCategoryModel:
    def test_str_method(self, category_factory):
        data = category_factory(name="test_category")

        assert data.__str__() == "test_category"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        data = brand_factory(name="test_brand")

        assert data.__str__() == "test_brand"


class TestProductModel:
    def test_str_method(self, product_factory):
        data = product_factory(name="test_product")

        assert data.__str__() == "test_product"


class TestProductLineModel:
    def test_str_method(self, product_line_factory):
        data = product_line_factory(sku="test_product_line")

        print("")
        print(type(data.price))

        assert data.__str__() == "test_product_line"

    def test_clean_fields_method(self, product_line_factory):
        # qs = ProductLine
        # data = product_line_factory()
        pass
