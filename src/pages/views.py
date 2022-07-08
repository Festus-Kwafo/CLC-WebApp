from django.shortcuts import render
from django.views import View

# Create your views here.
class IndexView(View):
    template_name = "templates/pages/index.html"

    def get(self, request):
        return render(request, self.template_name)

class AboutView(View):
    template_name = "templates/pages/about.html"

    def get(self, request):
        return render(request, self.template_name)
        
class SermonView(View):
    template_name = "templates/pages/about.html"

    def get(self, request):
        return render(request, self.template_name)

class GivingView(View):
    template_name = "templates/pages/about.html"

    def get(self, request):
        return render(request, self.template_name)

class OutreachView(View):
    template_name = "templates/pages/about.html"

    def get(self, request):
        return render(request, self.template_name)

