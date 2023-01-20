from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/<str:category>', views.gallery, name='gallery'),
    # path('gallery/<str:category>', views.gallery, name='gallery'),
    # path('gallery_<str:category>/<str:product>', views.product_page, name='product_page'),
    # path('<str:firstname>_<str:lastname>/', views.customer_space, name='customer_space'),
]