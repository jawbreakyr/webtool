from django.shortcuts import render
import random


SECRET_FILE = ''

def get_key_gen(request):
    try:
        SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
        secret = file(SECRET_FILE, 'w')
        secret.write(SECRET_KEY)
        secret.close()
    except IOError:
        Exception('Please create a %s file with random characters \
            to generate your secret key!' % SECRET_FILE)

    return render(request, 'home.html', {'SECRET_KEY': SECRET_KEY},)
   






   # """ try:
   #  SECRET_KEY
   #  except NameError:
   #      SECRET_FILE = ('secret.txt')
   #      try:
   #          SECRET_KEY = open(SECRET_FILE).read().strip()
   #      except IOError:
   #          try:
   #              import random
   #              SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
   #              secret = file(SECRET_FILE, 'w')
   #              secret.write(SECRET_KEY)
   #              secret.close()
   #          except IOError:
   #              Exception('Please create a %s file with random characters \
   #              to generate your secret key!' % SECRET_FILE)"""
    

