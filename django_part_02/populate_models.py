import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_part_02.settings')

import django
from django.conf import settings

if not settings.configured:
    settings.INSTALLED_APPS

django.setup()
    
import random

from faker import Faker
from pydoc_data.topics import topics

from first_app.models import AccessRecord, Topic, Webpage

fake = Faker()
topics = ['Search','Social','Marketplace','News','Games']


def add_topics():
    top_name = random.choice(topics) # type: ignore
    print(top_name)
    t = Topic.objects.get_or_create(top_name=top_name)[0]  # type: ignore
    t.save()
    
    return t


def populate(n=5):
    for i in range(n):
        top = add_topics()
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.name()
        
        webpage = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        
        acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]
        # webpage.save()
        # acc_rec.save()
        
    

if __name__ == '__main__':
    try:
        print("Running script to populate models")
        populate(n=20)
        print("Done!")
    
    except Exception as e:
       print(e)
