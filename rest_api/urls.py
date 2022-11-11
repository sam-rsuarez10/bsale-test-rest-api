from django.urls import path
from .views import ProductList, CategoryList
urlpatterns = [
    # list of products
    path("products/", ProductList.as_view(), name="products_list"),
    # list of categories
    path("categories/", CategoryList.as_view(), name="category_list")
]
