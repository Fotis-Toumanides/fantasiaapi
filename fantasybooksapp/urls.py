from django.contrib import admin
from django.urls import path,include
from fantasybooksapp import views
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render

from rest_framework.routers import DefaultRouter

from .views import RegisterViewset,LoginViewset, UserViewset
from knox import views as knox_views
app_name = 'fantasybooksapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookdescriptions/', views.BookDescriptionListCreateView.as_view(), name='bookDescription-list-create'),
    path('bookdescriptions/<int:pk>/', views.BookDescriptionRetrieveUpdateDestroyView.as_view(), name='bookDescription'),
    path('book/', views.BookListCreateView.as_view(), name='book-list-create'),
    path('book/<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view(), name='book-content'),
    path('bookmarks/', views.BookmarkListCreateView.as_view(), name='bookmarks'),
    path('bookmark/<int:pk>/', views.BookmarkRetrieveUpdateDestroyView.as_view(), name='bookmark'),

    path('register/', RegisterViewset.as_view({'post': 'create'}), name='register'),
    path('login/', LoginViewset.as_view({'post': 'create'}), name='login'),
    path('users/', UserViewset.as_view({'get': 'list'}), name='users'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
