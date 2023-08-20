from rest_framework import serializers
from .models import Color, Person


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name', 'id']


class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    colorInfo = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1

    def get_colorInfo(self, obj):
        colorObj = Color.objects.get(id=1)
        return {"color": colorObj.color_name, "hexCode": "#000"}

    def validate(self, data):
        specialCharacters = "@\,"
        if any(c in specialCharacters for c in data['name']):
            raise serializers.ValidationError(
                "name can not contain special characters")
        if data['age'] < 18:
            raise serializers.ValidationError('Age should be greater than 18')
        return data
