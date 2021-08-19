from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetials.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
]