from django.urls import path
from django.contrib import admin
from .views import MaestroProducto_create, MaestroProducto_read, MaestroProducto_read_all
from .views import MaestroProducto_update, MaestroProducto_delete, login


urlpatterns = [
    path('mp_create/', MaestroProducto_create.as_view(), name="mp_create"),
    path('mp_update/', MaestroProducto_update.as_view(), name="mp_update"),
    path('mp_read/<id>/', MaestroProducto_read, name="mp_read"),
    path('mp_read_all/', MaestroProducto_read_all, name='mp_read_all'),
    path('mp_delete/<id>/', MaestroProducto_delete, name="mp_delete"),
    path('login', login, name='login'),
]