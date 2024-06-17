from django.urls import path

from . import views



urlpatterns = [
    path('template/', views.template_list_create_view, name='template-list'),
    path('category/', views.category_list_create_view, name='category-list'),
    path('product/', views.products_list_create_view, name='product-list'),
    path('billing/', views.billing_list_create_view, name='billing-list'),
    path('Ratings/', views.Ratings_list_create_view, name='Rating-list')

]
