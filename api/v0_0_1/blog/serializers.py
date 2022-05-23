from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'title', 'subtitle', 'slug', 'body', 'meta_description', 'publish_date', 'author', 'tags']
