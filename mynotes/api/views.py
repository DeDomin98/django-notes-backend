from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Note
from .serializers import NoteSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .models import UserProfile
from rest_framework import status
from django.contrib.auth.models import User

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getNotes(request):
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()
            
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    user = request.user
    note = Note.objects.create(
        body=data['body'],
        user=user,  # Set the user identifier for the new note
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    
    return Response(status=204)


from rest_framework.permissions import AllowAny

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

@api_view(['GET'])
def check_username(request):
    username = request.query_params.get('username')

    # Sprawdzenie, czy użytkownik o podanej nazwie już istnieje (przykładowe zapytanie do bazy danych)
    from .models import User  # Załóżmy, że masz model User, który reprezentuje użytkowników
    user_exists = User.objects.filter(username=username).exists()

    if user_exists:
        return Response({"error": "UserAlreadyExists"})

    return Response({"message": "Username is available"})