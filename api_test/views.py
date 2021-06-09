from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from .models import TestModel
from .serializers import TestModelSerializer


def simple(request):
    return response.HttpResponse("test")


# API view method
class SimpleApiView(APIView):

    def post(self, request):
        serializer = TestModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({"data": serializer.data})

    def get(self, request):
        content = TestModel.objects.all()
        serializer = TestModelSerializer(content, many=True)
        return Response({"data": serializer.data})

    def put(self, request, *args, **kwargs):
        model_id = kwargs.get("id", None)
        if not model_id:
            return JsonResponse({"error": "method /PUT/ not allowed"})
        try:
            instance = TestModel.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "Object does not exist"})

        serializer = TestModelSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})


# Generics API view method
class SimpleGenericsView(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer


class SimpleGenericsUpdateView(generics.UpdateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer
    lookup_field = "id"


# ViewSet method
class SimpleViewSetView(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer
