from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'dia/index.html', {
        'esViernes': datetime.today().isoweekday() == 5
        #'esViernes': 'Ya es viernes' if datetime.today().isoweekday() == 2 else 'No es viernes'
    })
