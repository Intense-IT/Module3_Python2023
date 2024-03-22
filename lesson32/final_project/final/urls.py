from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('news.urls', 'news'), namespace='news')),
    path('api/v1/', include(('posts.urls', 'posts'), namespace='posts')),
    path('token/', views.TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
