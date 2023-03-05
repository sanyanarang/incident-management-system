from rest_framework.serializers import ModelSerializer
from .models import Incident
class IncidentSerializer(ModelSerializer):
        class Meta:
                model = Incident
                fields = '__all__'

        # def create(self, validated_data):
        #         print(validated_data)
        #         incident = Incident(
        #         email=validated_data['email'],
        #         username=validated_data['username']
        # )
        # user.set_password(validated_data['password'])
        # user.save()
        # return user