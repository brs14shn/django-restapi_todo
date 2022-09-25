
from django.urls import path,include
from .views import (
    TodoModelViewSet,
    CategoryListCreate,
    CategoryConcrateURD,

)
from rest_framework import routers


#Viewset
#Default
router = routers.DefaultRouter()
#router = routers.SimpleRouter()
router.register('todos', TodoModelViewSet )

#Simple




urlpatterns = [

    path("",include(router.urls)),
    #or
    #urlpatterns+=router.urls


     #! CBV ##CONCRATE APIVİEW 👇
    path("list/",CategoryListCreate.as_view()),
    path("urd/<int:pk>",CategoryConcrateURD.as_view()),
    
]


