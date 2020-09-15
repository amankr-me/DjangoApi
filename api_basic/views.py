from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article,Locality
from .serializers import ArticleSerializer ,LocalitySerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
# Create your views here.


def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid() :
            serializer.save()
            return JsonResponse(serializer.data, status= 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def article_detail(request, pk):
    try: article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status= 404)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status= 400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)




@csrf_exempt
# Create your views here.


def locality_list(request):

    if request.method == 'GET':
        users = Locality.objects.all()
        serializer = LocalitySerializer(users, many = True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LocalitySerializer(data=data)

        if serializer.is_valid() :
            serializer.save()
            return JsonResponse(serializer.data, status= 201)
        return JsonResponse(serializer.errors, status = 400)



@csrf_exempt
def locality_detail(request, pk):
    try: locality = Locality.objects.get(pk=pk)
    except Locality.DoesNotExist:
        return HttpResponse(status= 404)
    
    if request.method == 'GET':
        serializer = LocalitySerializer(locality)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LocalitySerializer(locality, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status= 400)

    elif request.method == 'DELETE':
        locality.delete()
        return HttpResponse(status=204)
