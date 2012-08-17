from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
#from cwreport.models import ???
import datetime



#def cwreports(request):
#	ticket = Tickets.objects.filter(priority=10)[:15]
#return render_to_response('reports.html', {'ticket':ticket},
#                              context_instance=RequestContext(request))	
