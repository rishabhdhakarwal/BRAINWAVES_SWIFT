from django.contrib import admin
from django.urls import path
from stocks import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'client/', views.client),

]
