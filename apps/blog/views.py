from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.blog.models import Article
from .serializers import ArticleSerializer

# 初级写法,换成类显示更好的,类的话在路由限定请求方式,报错明确
@api_view(['GET', 'POST'])
def article_list(request):
    """
    List all articles, or create a new article.
    """
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            # Very important. Associate request.user with author
            # 注意：由于序列化器中author是read-only字段，用户是无法通过POST提交来修改的，我们在创建Article实例时需手动将author和request.user绑定，如下所示：
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    """
    Retrieve，update or delete an article instance。"""
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)