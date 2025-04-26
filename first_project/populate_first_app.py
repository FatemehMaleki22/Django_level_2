import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, Webpage, Topic,User

from faker import Faker
fakegen = Faker()

topics =['Search','Social', 'Marketplace','News','Games']

def add_topic():
  t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
  #t.save()
  return t

def populate(N=5):
  for entry in range(N):
    top = add_topic()
    fake_url = fakegen.url()
    fake_date = fakegen.date()
    fake_name = fakegen.company()
    
    webpage = Webpage.objects.get_or_create(topic = top, url= fake_url, name = fake_name)[0]
    AccessRecord.objects.get_or_create(name= webpage, date= fake_date)[0]
    fake_first_name = fakegen.first_name()
    fake_last_name = fakegen.last_name()
    fake_email = fakegen.email()
    User.objects.get_or_create(last_name=fake_last_name, first_name = fake_first_name, email= fake_email)
     
    
  
if __name__ == '__main__':
  print('Populating Script!')
  populate(20)
  print('Popolating complete')