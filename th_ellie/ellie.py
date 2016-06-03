# coding: utf-8
# add here the call of any native lib of python like datetime etc.
#
# add the python API here if needed
#from external_api import CallOfApi

# django classes
from django.conf import settings
from django.utils.log import getLogger

# django_th classes
from django_th.services.services import ServicesMgr
from django_th.models import UserService, ServicesActivated
from django.core.cache import caches

"""
    handle process with dummy
    put the following in settings.py

    TH_DUMMY = {
        'consumer_key': 'abcdefghijklmnopqrstuvwxyz',
    }

    TH_SERVICES = (
        ...
        'th_dummy.my_dummy.ServiceDummy',
        ...
    )

"""

logger = getLogger('django_th.trigger_happy')


class ServiceEllie(ServicesMgr):

    def process_data(self, trigger_id):
        """
            get the data from the cache
            :param trigger_id: trigger ID from which to save data
            :type trigger_id: int
        """
        cache = caches["th_ellie"]
        datas = cache.get('tasks')
        if not datas:
            return []
        #datas  [{"title": title, "description": description}, {"title": title, "description": description}]
        l = []
        for i in datas:
           l.append(i)
        return l