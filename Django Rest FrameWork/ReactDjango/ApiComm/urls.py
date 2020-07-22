from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register("api",GenericPost)
#router.register("auth",UserView)

urlpatterns = [
    path('',include(router.urls)),
    path('login',LoginView.as_view()),
    path('signup',SignupView.as_view()),
    path('activate', ActivateUsers)
]