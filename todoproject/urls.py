from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),     #何も文字列がない場合，todoのurlsを呼び出す
]
