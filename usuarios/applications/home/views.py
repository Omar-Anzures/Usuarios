import datetime

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.views.generic import TemplateView


class FechaMixin(object):
    def get_context_data(self, **kwargs):
        context = super(FechaMixin,self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now()
        return context
    

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = "home/index.html"
    login_url = 'users_app:login'


class TemplateMixi(FechaMixin,TemplateView):
    template_name = 'home/mixi.html'

