from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.http.response import JsonResponse

from rest_framework_simplejwt import views as jwt_views

from users.models import *
from users.serializers import *


class TokenObtainPairPatchedView(jwt_views.TokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = TokenObtainPairPatchedSerializer


class UserViewSet(ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all().select_related('belongs_to')
    serializer_class = SubjectSerializer
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        belongs_to = request.GET['query']['id']
        queryset = self.get_queryset().filter(belongs_to=belongs_to)
        serializer = self.serializer_class(queryset, many=True).data 
        return JsonResponse(serializer,status=200, safe=False)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['belongs_to'] = request.GET['query']['id']
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)