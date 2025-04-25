from django.shortcuts import render

# Create your views here.
def index(request):
  props={'name':'Fatemeh'}
  return render(request,'first_app/index.html', context=props)