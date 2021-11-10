from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    if "alarmas" not in request.session:
        request.session["alarmas"] = ['5:30', '5:35']
    return render(request, 'alarmas/index.html', {'alarmas':request.session["alarmas"]})

def v2(request):
    if request.method == 'POST':
        form = FNuevaAlarma(request.POST)
        if form.is_valid():
            alarma = form.cleaned_data['alarma']
            # Validar si alarma está en el formato correcto
            request.session["alarmas"] += [alarma]
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
