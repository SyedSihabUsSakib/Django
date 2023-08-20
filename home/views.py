from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Person, Color
from home.serializers import ColorSerializer, PeopleSerializer


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
