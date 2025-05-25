from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse

@api_view(["GET"])
def homeview(request):
    return redirect("/accounts/")