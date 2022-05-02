from django.shortcuts import render

# Create your views here.
def v_index(request):
  request.render('index.html')