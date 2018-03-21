from django.conf.urls import url
from django.contrib import admin

from csv_importer import views


urlpatterns = [
    url('admin/', admin.site.urls),
    url('', views.main, name='csv_importer'),
]