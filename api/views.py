from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer


# function based - example
@api_view(['GET'])
def overview(request):
    api_urls = {
        'Simple': '/index/',
        'Class based View': '/message/',
        'Quizez': '/quizes/',
        'FunctionViewQuiz': '/functionViewQuiz/',
        'GenericView': '/genericView/',
    }
    return Response(api_urls)


@api_view(['GET', 'POST'])
def index(request):
    print(request.user)
    print(request.auth)
    if request.method == 'GET':
        message = 'Hello from django'
        return Response(data=message, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        print(request.data)
        return Response(data=request.data, status=status.HTTP_200_OK)
    else:
        return Response(data="Request method is not right")


# class based - example
class Message(APIView):
    print('hit by api call')

    def get(self, request):
        return Response(data="This is a class based view hit by get method", status=status.HTTP_200_OK)

    def post(self, request):
        return Response(data="This is a class based view hit by a post method ", status=status.HTTP_200_OK)


# using the modelserializers
class QuizView(APIView):

    def get_object(self):
        try:
            return Quiz.objects.all()
        except Quiz.DoesNotExit:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request):
        queryset = self.get_object()
        serializer = QuizSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print("hitting post")
        serializer = QuizSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        queryset = Quiz.objects.get(id=request.data['id'])
        queryset.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)

    def put(self, request):
        quiz = Quiz.objects.get(id=request.data['id'])
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def QuizV(request):
    queryset = Quiz.objects.all()
    serializer = QuizSerializer(queryset, many=True)
    return Response(data=serializer.data, status=status.HTTP_404_NOT_FOUND)


# GENERIC VIEWS
class GenericQuizView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
