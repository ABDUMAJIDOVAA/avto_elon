from django.urls import path
from .views import (
    all_avtolar, avtolar_list, avtolar_detail, avto_create, avto_update, avto_delete,
    avto_by_category, category_list, category_detail, category_create, category_update, category_delete, 
    user_login, user_logout, user_register,edit_profile, view_profile
)

urlpatterns = [
    path('', all_avtolar, name='index'),
    path('avto/list', avtolar_list, name='avto_list'),
    path('avto/<int:pk>/detail/', avtolar_detail, name='avto_detail'),
    path('avto/new/', avto_create, name='avto_create'),
    path('avto/<int:pk>/edit/', avto_update, name='avto_update'),
    path('avto/<int:pk>/delete/', avto_delete, name='avtp_delete'),
    path('avto-by-category/<int:category_id>/', avto_by_category, name='avto_by_category'),
    path('category/', category_list, name='category_list'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
    path('category/new/', category_create, name='category_create'),
    path('category/<int:pk>/edit/', category_update, name='category_update'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),
    path('user-login/', user_login, name='user_login'),
    path('user-logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('profile/', view_profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]
