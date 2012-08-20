from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from prettyreport.models import Tickets
import datetime



def reports(request):
	ticket = Tickets.objects.filter(priority=10)[:15]

	return render_to_response('reports.html', {'ticket':ticket},
				  context_instance=RequestContext(request))	


def dreports(request):
	ticket = list(Tickets.objects.filter(priority=10).order_by('-duedate')[:15])
	
	return render_to_response('dreports.html', {'ticket':ticket},
				  context_instance=RequestContext(request))


def tests(request):
	now = 2 * 343434
	html = "<html><body>2 * 343434 is %s....</body></html>" % now
	return HttpResponse(html)	


class HomeView(TemplateView):
	template_name = "home.html"