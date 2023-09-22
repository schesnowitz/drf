
from django.contrib import admin
from django.urls import path
from booze import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booze/', views.booze_list),
]
