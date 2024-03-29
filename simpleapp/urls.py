from django.urls import path
# Импортируем созданное нами представление
from .views import Products, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('', Products.as_view()),
   path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Ссылка на детали товара
   path('create/', ProductCreateView.as_view(), name='product_create'),  # Ссылка на создание товара
   path('create/<int:pk>', ProductUpdateView.as_view(), name='product_update'),  # добавление продукта
   path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),  # удаление продукта
]

