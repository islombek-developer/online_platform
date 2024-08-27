"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from app.views import UserView,CommentView,EmailView,LikesView,LikecreateView,LessonView,CourseView

router = routers.SimpleRouter()
router.register('user', UserView)
router.register('lesson', LessonView)
router.register('course', CourseView)
router.register('comment', CommentView)


api_urlpatterns = [
  
    path('accounts/', include('rest_registration.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/token/', include('djoser.urls.authtoken')),
    path('api/v1/', include(api_urlpatterns)),
    path('api/v2/', include(router.urls)),
    path('like/<int:pk>/',LikesView.as_view()),
    path('like/create/',LikecreateView.as_view()),
    path('api/v2/email/', EmailView.as_view()),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)