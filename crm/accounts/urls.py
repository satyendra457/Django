from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="dashboard"),
    path('product/', views.ProductDetails, name='product_details'),
    path('create_product/', views.CreateProduct, name='product_create'),
    path('update_product/<str:pk>/', views.UpdateProduct, name='update_product'),
    path('delete_product/<str:pk>/', views.DeleteProduct, name='delete_product'),
    path('tag_details/', views.TagsDetails, name="tag_details"),
    path('create_tag/', views.CreateTags, name='create_tag'),
    path('update_tag/<str:pk>/', views.UpdateTags, name='update_tag'),
    path('delete_tag/<str:pk>/', views.DeleteTags, name='delete_tag'),
]