from django.shortcuts import render, get_object_or_404, redirect
from .models import Nutricionista, Paciente, Sesion
from .forms import NutricionistaForm, PacienteForm, SesionForm

# Nutricionista Views

def home_vista(request):
    return render(request, 'nutria_app/base.html')


def lista_nutricionistas(request):
    nutricionistas = Nutricionista.objects.all()
    return render(request, 'nutria_app/lista_nutricionistas.html', {'nutricionistas': nutricionistas})

def detalle_nutricionista(request, id):
    nutricionista = get_object_or_404(Nutricionista, id=id)
    return render(request, 'nutria_app/detalle_nutricionista.html', {'nutricionista': nutricionista})

def registrar_nutricionista(request):
    if request.method == 'POST':
        form = NutricionistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_nutricionistas')
    else:
        form = NutricionistaForm()
    return render(request, 'nutria_app/crear_nutricionista.html', {'form': form})

# Paciente Views

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'nutria_app/lista_pacientes.html', {'pacientes': pacientes})

def detalle_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    return render(request, 'nutria_app/detalle_paciente.html', {'paciente': paciente})

def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'nutria_app/crear_paciente.html', {'form': form})

# Sesion Views

def lista_sesiones(request):
    sesiones = Sesion.objects.all()
    return render(request, 'nutria_app/lista_sesiones.html', {'sesiones': sesiones})

def detalle_sesion(request, id):
    sesion = get_object_or_404(Sesion, id=id)
    return render(request, 'nutria_app/detalle_sesion.html', {'sesion': sesion})

def registrar_sesion(request):
    if request.method == 'POST':
        form = SesionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_sesiones')
    else:
        form = SesionForm()
    return render(request, 'nutria_app/crear_sesion.html', {'form': form})
