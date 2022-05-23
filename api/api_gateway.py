from django.urls import include, path
from api.v0_0_1 import router

urlpatterns = [
    path('v0.0.1/', include(router)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]