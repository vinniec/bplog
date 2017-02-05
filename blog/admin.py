#~ from django.contrib import admin
#~ # Register your models here.

from django.contrib import admin
from .models import Post            #importo i modelli del blog, in questo caso il Post

admin.site.register(Post)   #registrando il modello sarà visibile nel menù dell'admin di django
