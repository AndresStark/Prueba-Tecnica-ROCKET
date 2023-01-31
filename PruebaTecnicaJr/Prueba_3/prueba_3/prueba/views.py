from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import DetailModel
from .forms import DetailForm


class IndexView(generic.ListView):
    template_name = "prueba/index.html"
    context_object_name = "texto"

    def get_queryset(self):
        a = DetailModel()
        a.detalle = "Este texto es un ejemplo"
        a.save()
        return a


class DetailView(generic.ListView):
    model = DetailModel
    template_name = "prueba/detail.html"
    form_class = DetailForm

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)            
            if form.is_valid():
                return render(request, 'prueba/detail.html', {'form': form})
        else:
            form = self.form_class()

        return render(request, 'prueba/detail.html', {'form': form})

    def get(self, request):
        if request.method == 'GET':
            return HttpResponse("Este es un ejemplo de metodo GET")

