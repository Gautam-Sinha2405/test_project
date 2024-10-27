from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from library.serializer import BookSerializer, AuthorSerializer


# Create your views here.
@api_view(['POST'])
def create_book(request):
    book_serializer = BookSerializer(data=request.data)
    if book_serializer.is_valid():
        book_serializer.save()
        return Response(book_serializer.data, status=status.HTTP_201_CREATED)

    return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_author(request):
    author_serializer = AuthorSerializer(data=request.data)
    if author_serializer.is_valid():
        author_serializer.save()
        return Response(author_serializer.data, status=status.HTTP_201_CREATED)