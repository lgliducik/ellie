from django.db import models

# django_th classes
#from django_th.services.services import ServicesMgr
#from django_th.models import UserService, ServicesActivated
from django_th.models.services import Services

class Ellie(Services):

    title = models.CharField(max_length=80)
    trigger = models.ForeignKey('TriggerService')

    class Meta:
        app_label = 'django_th'
        db_table = 'django_th_ellie'

    def __str__(self):
        return "%s" % (self.name)

    def show(self):
        return "My Ellie %s" % (self.name)