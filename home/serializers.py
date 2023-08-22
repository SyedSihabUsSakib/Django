from rest_framework import serializers
from .models import Color, Person
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('username is already taken')
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('email is already taken')
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
        print(validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']


class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    colorInfo = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1

    def get_colorInfo(self, obj):
        colorObj = Color.objects.get(id=3)
        return {"color": colorObj.color_name, "hexCode": "#000"}

    def validate(self, data):
        specialCharacters = "@\,"
        if any(c in specialCharacters for c in data['name']):
            raise serializers.ValidationError(
                "name can not contain special characters")
        if data['age'] < 18:
            raise serializers.ValidationError('Age should be greater than 18')
        return data
