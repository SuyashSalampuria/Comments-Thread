from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pages', views.PageViewSet)
router.register(r'messages', views.ParentMessageViewSet)
router.register(r'threads', views.ThreadMessageViewSet)

urlpatterns = [
    path('threads/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]