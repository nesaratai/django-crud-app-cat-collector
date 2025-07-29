from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
    path('cats/', views.cat_index, name='cat-index'),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
]