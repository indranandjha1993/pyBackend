from .user import views as user_view
from .blog import views as blog_view
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', user_view.UserViewSet)
router.register(r'groups', user_view.GroupViewSet)
router.register(r'posts', blog_view.PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
]