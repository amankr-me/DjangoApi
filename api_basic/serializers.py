from rest_framework import serializers
from .models import Article ,Locality



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']


class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
        fields = ['id','city', 'state','locality']