from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from knox import views as knox_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fantasybooksapp.urls')),
    path('api/auth/', include('knox.urls')),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)