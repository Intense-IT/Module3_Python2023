from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()


router.register(r'posts', views.PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(),
         name='category-detail'),
]
