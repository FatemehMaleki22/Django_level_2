from django.shortcuts import render
from first_app.models import AccessRecord, Topic,Webpage, User
from first_app.forms import SignupForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
  webpages_list = AccessRecord.objects.order_by('date')
  date_dict = {'access_records': webpages_list}
  return render(request,'first_app/index.html', context=date_dict)

def user(request):
  users_list = User.objects.order_by('first_name')
  user_dict = {'users': users_list}
  return render(request,'first_app/user.html', context=user_dict)

@csrf_protect
def signup(request):
  form = SignupForm()
  if request.method == 'POST':
    form = SignupForm(request.POST)
    print('in POST')
    if form.is_valid():
      form.save(commit= True)
      print('FORM saved')
      return index(request)
    else:
      print('Error form is Invalid')
  return render (request, 'first_app/signup.html',{'form':form})   


def form_name_view(request):
  form = forms.FormName()
  if request.method == 'POST':
    form = forms.FormName(request.POST)
    if form.is_valid():
      print('Validation is succeed.')
      print('NAME '+ form.cleaned_data['name'])
      print('EMAIL '+ form.cleaned_data['email'])
      print('TEXT '+ form.cleaned_data['text'])
  
  return render(request, 'basicapp/form_page.html',{'form':form})