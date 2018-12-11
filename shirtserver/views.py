from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Shirt

class IndexView(generic.ListView):
    template_name = 'shirtserver/index.html'
    context_object_name = 'shirt_list'

    def get_queryset(self):
        return Shirt.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Shirt
    template_name = 'shirtserver/detail.html'
