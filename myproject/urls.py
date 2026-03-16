from django.contrib import admin
from django.urls import path, include # เพิ่ม include ตรงนี้

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')), # เพิ่มบรรทัดนี้เพื่อเชื่อมไปหา myapp
]