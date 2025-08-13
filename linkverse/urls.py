from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_login, name='login'),  # Set login as the home page
    path('guest/', views.guest_home, name='guest_home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'), 

    path('creator-dashboard/', views.creator_dashboard, name='creator_dashboard'),

    path('create-category/', views.create_category, name='create_category'),
    path('category-list/', views.category_list, name='category_list'),
    path('update-category/<int:pk>/', views.update_category, name='update_category'),
    path('delete-category/<int:pk>/', views.delete_category, name='delete_category'),

    # Link URLs
    path('create-link/', views.create_link, name='create_link'),
    path('link-list/', views.link_list, name='link_list'),
    path('update-link/<int:pk>/', views.update_link, name='update_link'),
    path('delete-link/<int:pk>/', views.delete_link, name='delete_link'),
]
