from django.urls import path
from .views import CatalogListView, CatalogDetailView, CatalogTemplateView

app_name = 'catalog'
urlpatterns = [
    path('home/', CatalogListView.as_view(), name='show_home'),
    path('', CatalogListView.as_view(), name='show_home'),
    path('contacts/', CatalogTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>', CatalogDetailView.as_view(), name='product'),
]
