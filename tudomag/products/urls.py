from django.urls import path
from products import views



urlpatterns = [
    path('', views.homepage_view, name="homepage"),
    path('category_details/<int:pk>', views.CategoryDetailView.as_view(), name="category_details"),
    path('category_list/', views.CategoryListView.as_view(), name="category_list"),
    path('category_create/', views.CategoryCreateView.as_view(), name="category_create"),
    path('category_update/<int:pk>', views.CategoryUpdateView.as_view(), name="category_update"),
    path('category_delete/<int:pk>', views.CategoryDeleteView.as_view(), name="category_delete"),
    path('accounts/profile/', views.homepage_view, name="homepage"),
]
