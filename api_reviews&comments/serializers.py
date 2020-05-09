from rest_framework import serializers
from .models import Review, Comment


class ReviewSerialier(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)


    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date',)
        model = Review
        

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)


    class Meta:
        fields = ('id', 'text', 'author', 'pub_date',)
        model = Comment