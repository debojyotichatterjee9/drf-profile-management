from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse

class HealthCheckView(View):
    def get(self, request):
        return JsonResponse("Status: OK", safe=False)
