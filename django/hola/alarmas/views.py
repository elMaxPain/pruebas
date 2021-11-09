from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

alarmas = ['5:30', '5:35', '5:40', '5:50']

# Create your views here.

def index(request):
    return render(request, 'alarmas/index.html', {'alarmas':alarmas})

def v2(request):
    if request.method == 'POST':
        form = FNuevaAlarma(request.POST)
        if form.is_valid():
            alarma = form.cleaned_data['alarma']
            alarmas.append(alarma)
            return HttpResponseRedirect(reverse('alarmas:index'))
        else:
            return render(request, 'alarmas/v2.html', {'cont_form':form})
    else:
        return render(request, 'alarmas/v2.html', {'cont_form':FNuevaAlarma()})

class FNuevaAlarma(forms.Form): # hereda
    alarma = forms.CharField(label='Nueva alarma')  # Campo de caracteres
                                                    # con etiqueta
                                                    # <input type='text' ...>
    #snooze = forms.IntegerField(label='Repetir', min_value=0, max_value=10)
