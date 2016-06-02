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
        #print('!!!!!!!!!!type(datas) =', type(datas))
        #print('!!!!!!!!!!datas =', datas)
        #datas = ['task1', 'task2']
        # return [{'title':'task1', 'description':'task1'},{'title':'task2', 'description':'task2'}]

        l = []
        for i in datas:
            l.append({'title': i, 'description': i})
        print(l)
        #return [{'title':datas, 'description':datas}]
        return l

    # def __init__(self, ):
    #     pass

    
    # def auth(self, request):
    #     """
    #         let's auth the user to the Service
    #     """
    #     # request_token = super(ServiceEllie, self).auth(request)
    #     # callback_url = self.callback_url(request, 'ellie')

    #     # # URL to redirect user to, to authorize your app
    #     # auth_url_str = '%s?oauth_token=%s&oauth_callback=%s'
    #     # auth_url = auth_url_str % (self.AUTH_URL,
    #     #                            request_token['oauth_token'],
    #     #                            callback_url)

    #     return True

    # def callback(self, request):
    #     """
    #         Called from the Service when the user accept to activate it
    #     """
    #     kwargs = {'access_token': '', 'service': 'ServiceEllie',
    #               'return': 'ellie'}
    #     return super(ServiceEllie, self).callback(request, **kwargs)