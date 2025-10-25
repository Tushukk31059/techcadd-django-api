from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin

def home(request):
    return HttpResponse("✅ Techcadd Django API is running successfully!")

urlpatterns = [
    path('', home),  # 👈 add this line
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
