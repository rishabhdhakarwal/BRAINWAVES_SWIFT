from django.contrib import admin
from django.urls import path
from stocks import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'client/', views.client),
    url(r'sg/', views.sg),
    url(r'status/', views.status),
    url(r'^stock_history', views.stock_history),
]
