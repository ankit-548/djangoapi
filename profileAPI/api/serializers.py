from rest_framework import serializers
from api.models import Profile
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # profile_picture = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model= Profile
        fields="__all__"
