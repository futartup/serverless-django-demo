from rest_framework import serializers

from users.models import *


class ConfigurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ('first_name', 'last_name')
