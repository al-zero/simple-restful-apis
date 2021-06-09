from django.shortcuts import render
from .serializers import NoteSerializer
from .models import Note
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def notes_overview(request):
    api_urls = {
        'List View': 'notes-list/',
        'Detail View': 'note-detail/<int:id>/',
        'Create View': 'note-create/',
        'Update View': 'note-update/<int:id>/',
        'Delete View': 'note-delete/<int:id>/',

    }
    return Response(api_urls)


@api_view(['GET'])
def notes_list(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def note_create(request):
    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["PUT"])
def note_update(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["GET"])
def note_delete(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note deleted!")
