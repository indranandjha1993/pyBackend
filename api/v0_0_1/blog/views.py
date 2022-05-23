from rest_framework import viewsets
from rest_framework import permissions
from blog.models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows post to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-publish_date')
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
