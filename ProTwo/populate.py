import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

## fake pop script
import random
from AppTwo.models import *
from faker import Faker

f = Faker()

def populate(N=5):
    for entry in range (N):
        #to get topic for entry

        fake_Name = f.name().split()
        fake_FirstName = fake_Name[0]
        fake_LastName = fake_Name[1]
        fake_Email = f.email()

        user = User.objects.get_or_create(FirstName=fake_FirstName,LastName=fake_LastName,Email=fake_Email)[0]
        
if __name__== '__main__':
    print('pop script')
    populate(20)
    print("pop done")
