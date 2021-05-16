from django.urls   import path

from product.views import MainView, SubCategoryView, ProductListView, ProductDetailView, FilterSortView

urlpatterns = [
    path('/main', MainView.as_view()),
    path('/<str:category_name>', SubCategoryView.as_view()),
    path('/cat/<str:sub_category_name>', ProductListView.as_view()),
    path('/p/<str:product_name>', ProductDetailView.as_view()),
    path('/p/<str:sub_category_name>/', FilterSortView.as_view())
]