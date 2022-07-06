from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Test
from .serializers import TestSerializer

# Create your views here.

class PostList(APIView):
    # 게시물 생성
    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    #  게시물 조회
    def get(self, request, format=None):
        queryset = Test.objects.all()
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data)


class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Test.objects.get(pk=pk)
        except Test.DoesNotExist:
            raise Http404
    # 특정 게시물 조회
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = TestSerializer(post)
        return Response(serializer.data)

    # 특정 게시물 수정
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = TestSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    # 특정 게시물 삭제
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)