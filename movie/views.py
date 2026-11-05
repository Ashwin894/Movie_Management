from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class MovieView(View):
    def post(self,request):
        variable=request.body

        data=loads(variable)
        title=data.get("title")
        director=data.get("director")
        year=data.get("year")
        data={
            "Title":title,
            "Director":director,
            "Year":year
        }
        return JsonResponse(data)
