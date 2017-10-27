from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View

class LandingView(View):
  def get(self, request):
    context = {"author" : "Rafał",
               "year" : 2017}
    print("GET LandingView")
    return render(request, "landing.html", context)

  def post(self, request):
    return HttpResponse("Przyszedł request POST")
