from django.conf.urls import url
from django.contrib import admin

from csv_importer import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='csv_importer'),
]