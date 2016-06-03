"""ellie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import patterns, include, url
from django_th.forms.wizard import DummyForm, ProviderForm
from django_th.forms.wizard import ConsumerForm, ServicesDescriptionForm

from django_th.views import TriggerListView, TriggerDeleteView
from django_th.views import TriggerUpdateView, TriggerEditedTemplateView
from django_th.views import TriggerDeletedTemplateView, trigger_on_off
from django_th.views import trigger_switch_all_to, trigger_edit
from django_th.views import service_related_triggers_switch_to

from django_th.views_userservices import UserServiceListView
from django_th.views_userservices import UserServiceCreateView
from django_th.views_userservices import UserServiceUpdateView
from django_th.views_userservices import UserServiceDeleteView
from django_th.views_userservices import renew_service
from django_th.views_wizard import UserServiceWizard

from django.contrib import admin
admin.autodiscover()


from django.conf.urls import include, url
from django.contrib import admin
from th_ellie import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'', include('th_github.urls')),
    url(r"^th/callbackgithub/$",
                 "django_th.views_wizard.finalcallback",
                 {'service_name': 'ServiceGithub', },
                 name="github_callback",
                 ),
    url(r"^th/callbackellie/$",
                 "django_th.views_wizard.finalcallback",
                 {'service_name': 'ServiceEllie', },
                 name="ellie_callback",
                 ),
    url(r'^th/send_name_to_github/$', views.send_name_to_github),


    url(r'^jsreverse/$', 'django_js_reverse.views.urls_js',
          name='js_reverse'),
    # ****************************************
    # admin module
    # ****************************************
    url(r'^admin/', include(admin.site.urls)),
    # ****************************************
    # auth module
    # ****************************************
    url(r'^auth/', include('django.contrib.auth.urls')),
    # ****************************************
    # customized logout action
    # ****************************************
    url(r'^logout/$',
        'django_th.views.logout_view', name='logout'),

    # ****************************************
    # trigger happy module
    # ****************************************
    url(r'^th/$', TriggerListView.as_view(),
        name='base'),
    url(r'^th/trigger/filter_by/(?P<trigger_filtered_by>[a-zA-Z]+)$',
        TriggerListView.as_view(),
        name='trigger_filter_by'),
    url(r'^th/trigger/order_by/(?P<trigger_ordered_by>[a-zA-Z_]+)$',
        TriggerListView.as_view(),
        name='trigger_order_by'),
    url(r'^th/trigger/$', TriggerListView.as_view(),
        name='home'),
    # ****************************************
    # * trigger
    # ****************************************
    url(r'^th/trigger/delete/(?P<pk>\d+)$',
        TriggerDeleteView.as_view(),
        name='delete_trigger'),
    url(r'^th/trigger/edit/(?P<pk>\d+)$',
        TriggerUpdateView.as_view(),
        name='edit_trigger'),
    url(r'^th/trigger/editprovider/(?P<trigger_id>\d+)$',
        trigger_edit, {'edit_what': 'Provider'},
        name='edit_provider'),
    url(r'^th/trigger/editconsumer/(?P<trigger_id>\d+)$',
        trigger_edit, {'edit_what': 'Consumer'},
        name='edit_consumer'),
    url(r'^th/trigger/edit/thanks',
        TriggerEditedTemplateView.as_view(),
        name="trigger_edit_thanks"),
    url(r'^th/trigger/delete/thanks',
        TriggerDeletedTemplateView.as_view(),
        name="trigger_delete_thanks"),
    url(r'^th/trigger/onoff/(?P<trigger_id>\d+)$',
        trigger_on_off,
        name="trigger_on_off"),
    url(r'^th/trigger/all/(?P<switch>(on|off))$',
        trigger_switch_all_to,
        name="trigger_switch_all_to"),
    # ****************************************
    # * service
    # ****************************************
    url(r'^th/service/$', UserServiceListView.as_view(),
        name='user_services'),
    url(r'^th/service/(?P<action>\w+)$',
        UserServiceListView.as_view(),
        name='user_services'),
    url(r'^th/service/add/$', UserServiceCreateView.as_view(),
        name='add_service'),
    url(r'^th/service/edit/(?P<pk>\d+)$',
        UserServiceUpdateView.as_view(),
        name='edit_service'),
    url(r'^th/service/delete/(?P<pk>\d+)$',
        UserServiceDeleteView.as_view(),
        name='delete_service'),
    url(r'^th/service/renew/(?P<pk>\d+)$',
        renew_service,
        name="renew_service"),
    url(r'^th/service/delete/$',
        UserServiceDeleteView.as_view(),
        name='delete_service'),
    url(r'^th/service/onoff/(?P<user_service_id>\d+)/(?P<switch>'
        r'(on|off))$',
        service_related_triggers_switch_to,
        name="service_related_triggers_switch_to"),
    # ****************************************
    # wizard
    # ****************************************
    url(r'^th/service/create/$',
        UserServiceWizard.as_view([ProviderForm,
                                   DummyForm,
                                   ConsumerForm,
                                   DummyForm,
                                   ServicesDescriptionForm]),
        name='create_service'),
    # every service will use django_th.views.finalcallback
    # and give the service_name value to use to
    # trigger the real callback
    
    url(r"^th/callbackgithub/$",
        "django_th.views_wizard.finalcallback",
        {'service_name': 'ServiceGithub', },
        name="github_callback",
        ),
]
