from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.urls import path
from booze import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booze/', views.booze_list),
    path('booze/<int:pk>', views.booze_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)