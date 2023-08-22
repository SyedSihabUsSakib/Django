from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Person, Color
from home.serializers import ColorSerializer, LoginSerializer, PeopleSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": serializer.errors
            }, status.HTTP_400_BAD_REQUEST)
        user = authenticate(
            username=serializer.data["username"], password=serializer.data["password"])

        if not user:
            return Response({
                "status": False,
                "message": "invalid credentials"
            }, status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "status": True,
            "message": "login in successful with token being generated",
            "token": str(token)
        }, status.HTTP_202_ACCEPTED)


class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": serializer.errors
            }, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"status": True, "message": "user is created"}, status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def index(request):
    courses = {
        'course_name': 'Python',
        'learner': 'Sihab',
        'learn': ['Django Rest Framework', 'flask', 'API']
    }
    if request.method == 'GET':
        print('You hit a get method')
        print(request.GET.get('search'))
        return Response(courses)
    elif request.method == 'POST':
        print('You hit a post method')
        data = request.data
        print(data['name'])
        return Response(courses)

# API_View Class


class PersonAPI(APIView):
    def get(self, request):
        objs = Person.objects.all()
        # print(objs)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        obj = Person.objects.get(id=data["id"])
        obj.delete()
        return Response("People has been Deleted")

# Api_view decorator


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def people(request):
    if request.method == 'GET':
        # print("you hit get method")
        objs = Person.objects.all()
        # print(objs)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print("you hit post method")
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Person.objects.get(id=data["id"])
        obj.delete()
        return Response("People has been Deleted")


# Color View
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def color(request):
    if request.method == 'GET':
        # print("you hit get method")
        objs = Color.objects.all()
        # print(objs)
        serializer = ColorSerializer(objs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print("you hit post method")
        data = request.data
        serializer = ColorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = Color.objects.get(id=data['id'])
        serializer = ColorSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj = Color.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Color.objects.get(id=data["id"])
        obj.delete()
        return Response("People has been Deleted")

# serializers.Serializer


@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        print(serializer.validated_data)
        return Response("Success")
    return Response(serializer.errors)


class peopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith=search)
        serializer = PeopleSerializer(queryset, many=True)
        return Response({'status': 200, 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
