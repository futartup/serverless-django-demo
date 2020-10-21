from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ValidationError


from users.models import *


class TokenObtainPairPatchedSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['user'] = user.email
        token['admin'] = user.is_staff
        token['email'] = user.email
        token['student'] = user.is_student  
        token['admin'] = user.is_staff 
        token['id'] = user.id

        if user.is_student:
            token['grade'] = user.grade 
            token['class'] = user.sclass 
            token['school_name'] = user.school_name 
            token['city'] = user.city 

        return token

    def validate(self, attrs):
        self.user = AppUser.objects.filter(email=attrs['username'], password=attrs['password']).first()
        if not self.user:
            raise ValidationError('The user is not valid.')

        if self.user:
            r = {}
            refresh = self.get_token(self.user)
            r['refresh'] = str(refresh)
            r['access'] = str(refresh.access_token)
            return r


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'