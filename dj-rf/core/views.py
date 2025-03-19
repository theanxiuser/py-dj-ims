from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Blog
from core.serializers import BlogSerializer


class BlogDetailView(APIView):

    def get_object(self, pk):
        return Blog.objects.get(pk=pk)

    def get(self, request, pk):
        blog = self.get_object(pk)
        if not blog:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        blog = self.get_object(pk)
        if not blog:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = self.get_object(pk)
        if not blog:
            return Response(status=status.HTTP_404_NOT_FOUND)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class BlogView(APIView):

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)