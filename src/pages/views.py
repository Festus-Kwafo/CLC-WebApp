from django.shortcuts import render
from django.views import View
from .models import Event, Message
from datetime import date, timedelta



# Create your views here.
class IndexView(View):
    template_name = "templates/pages/index.html"

    def get(self, request):
        start_date = date.today()
        end_date = start_date + timedelta(days=30)
        events = Event.objects.filter(start_date__range=[start_date, end_date])
        closest_event = Event.objects.filter(start_date__range=[start_date, end_date]).order_by('start_date')[0]

        context = {
            'events': events,
            'closest_event': closest_event
        }

        return render(request, self.template_name, context)

class AboutView(View):
    template_name = "templates/pages/about.html"

    def get(self, request):
        return render(request, self.template_name)

class SermonView(View):
    template_name = "templates/pages/sermon.html"

    def get(self, request):
        return render(request, self.template_name)

class GivingView(View):
    template_name = "templates/pages/giving.html"

    def get(self, request):
        return render(request, self.template_name)

class OutreachView(View):
    template_name = "templates/pages/outreach.html"

    def get(self, request):
        return render(request, self.template_name)

        
class StoreView(View):
    template_name = "templates/pages/store.html"
    def get(self, request):
        return render(request, self.template_name)

class OrderView(View):
    template_name = "templates/pages/order.html"
    def get(self, request):
        return render(request, self.template_name)

class BranchesView(View):
    template_name = "templates/pages/branches.html"
    def get(self, request):
        return render(request, self.template_name)

