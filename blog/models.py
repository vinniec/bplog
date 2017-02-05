#~ from django.db import models
#~ # Create your models here.

from django.db import models        #gli oggetti di django importati dal db
from django.utils import timezone   #modulo per gestione delle date?

#andiamo a definire il nostro oggetto Post, un model di django
#ereditiamo il modello di django, còsì abbiamo questo tipo di oggetto, così
#che django sappia che dovrà salvarlo nel database
class Post(models.Model):
    #attributi o proprietà della classe         #autore del post, è una chiave esterna? è una
    author = models.ForeignKey('auth.User')     #relazione/link con un altro oggetto/modello
                                                #auth.User sono modelli default degli utenti
    title  = models.CharField(max_length=200)   #titolo del post, campo testo?
    text   = models.TextField()                 #testo del post, campo testo lunghezza illimitata?
    created_date   = models.DateTimeField(      #data creazione post, campo data, data da timezone
        default=timezone.now)
    published_date = models.DateTimeField(      #data pubblicazione post, campo data, blank vuol
        blank=True, null=True)                  #dire non riempito e null che può rimanere vuoto

    #metodo che setta il valore della data di pubblicazione a quello dell'invocazione
    #sarà il metodo della pubblicazione
    def publish(self):
        self.published_date = timezone.now()

    #metodo che setta la stringa di ritorno dell'oggetto
    def __str__(self):
        return self.title
