from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = "general/home.html"
    
    # def get(self, request, *args, **kwargs):
    #     form = self.form_class
    #     return render(request, self.template_name, {'form': form})
  
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #     form.save()
    #     return HttpResonseRedirect(reverse('list-view'))
    #     else:
    #     return render(request, self.template_name, {'form': form})