from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

def checkIfActivated(func):
    def inner(*arg,**kwarg):
        request=arg[0]
        print("Here")
        #token=request.headers["Authorization"].split(" ")[1]
        token=request.query_params.get("token")
        print(token)
        user=get_object_or_404(Token, pk=token).user
        print(user)
        if user.is_active:
            return Response({"msg":"User Already Active"})
        else:
            return func(user)
    return inner