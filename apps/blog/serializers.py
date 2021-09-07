from rest_framework import serializers
from apps.blog.models import Article
from django.contrib.auth import get_user_model

User = get_user_model()


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=90)
    body = serializers.CharField(required=False, allow_blank=True)
    author = serializers.ReadOnlyField(source="author.id")
    status = serializers.ChoiceField(choices=Article.STATUS_CHOICES, default='p')
    create_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create a new "article" instance
        """
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Use validated data to return an existing `Article`instance。"""
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

# 简洁写法
class Article2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')


# 如果你希望author不可见并让DRF根据request.user自动补全这个字段，可以按如下修改ArticleSerializer
class Article3Serializer3(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'create_date')
