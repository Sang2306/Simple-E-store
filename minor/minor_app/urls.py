from django.urls import path

from . import views

app_name = 'minor_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('order/', views.order, name='order'),
    path('order/ordered/', views.ordered, name='ordered'),
    path('order/load_states/', views.load_states, name='load_states'),
    path('order/load_cities/', views.load_cities, name='load_cities'),
    path('order/load_delivery_date/', views.load_delivery_date, name='load_delivery_date'),
    path('product/load_sub_categories/', views.load_sub_categories, name='load_sub_categories'),
]
