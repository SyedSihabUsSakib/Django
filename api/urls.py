from home.views import index, login, people, color, PersonAPI, peopleViewSet
from django.urls import include, path


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Person', peopleViewSet, basename='Person')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index),
    path('people/', people),
    path('color/', color),
    path('login/', login),
    path('peopleapi/', PersonAPI.as_view())
]
