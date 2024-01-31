from django.urls import reverse

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Usuario

# Create your views here.
def inicio(requets):
    return render(requets,'ourschool/inicio.html')

def registrarse(request):
    return render(request,'ourschool/registrarse.html')



def iniciar(request):
    email = None
    clave = None

    if request.method == "POST":
        email = request.POST.get("correo")
        clave = request.POST.get("contrasena")

    try:
        usuario = Usuario.objects.get(correo=email, contrasena=clave)
        messages.success(request, "Bienvenido!")

        # Al autenticar al usuario, establece la sesión y redirige según el rol
        request.session['logueo'] = {'rol': usuario.rol}
        if usuario.rol == 2:
            return render(request, 'ourschool/inicio_estudiante.html')
        elif usuario.rol == 3:
            return render(request, 'ourschool/inicio_estudiante.html')
        elif usuario.rol == 1:
            return render(request, 'ourschool/inicio_estudiante.html')
        else:
            messages.error(request, "Rol no válido")

    except Usuario.DoesNotExist:
        messages.error(request, "Usuario o contraseña no válidos")
        return render(request, 'ourschool/iniciar.html')


def cerrar_session(request):
    try:
        del request.session['logueo']
        messages.success(request, 'Sesión cerrada correctamente')
        return redirect('inicio')

    except Exception as e:
        messages.error(request, f'Error: {e}')
        return redirect('inicio')  # O redirige a la página que consideres apropiada en caso de error



def registro(request):
    if request.method == "POST":
        # Obtener datos del formulario
        nom_ape = request.POST.get('nombre_apellido')
        tipo_doc = request.POST.get('tipo_documento')
        num_doc = request.POST.get('numero_documento')
        tel = request.POST.get('telefono')
        cor = request.POST.get('correo')
        fec_nac = request.POST.get('fecha_nacimiento')
        contr = request.POST.get('contrasena')
        r = request.POST.get('rol')

        try:
            # Crear un nuevo objeto Usuario
            nuevo_usuario = Usuario(
                nombre_apellido=nom_ape,
                tipo_documento=tipo_doc,
                numero_documento=num_doc,
                telefono=tel,
                correo=cor,
                fecha_nacimiento=fec_nac,
                contrasena=contr,
                rol=r
            )

            # Validar el objeto
            nuevo_usuario.full_clean()

            # Guardar el objeto en la base de datos
            nuevo_usuario.save()

            messages.success(request, 'Se guardó correctamente')
            return redirect('iniciar')

        except ValidationError as e:
            messages.warning(request, f'Error: {e}')

    return HttpResponseRedirect(reverse('inicio'))


from django.shortcuts import render

def perfil(request):
    # Obtener información del usuario actual (puedes usar request.user si estás utilizando el sistema de autenticación de Django)
    usuario = request.user  # Asegúrate de haber configurado correctamente la autenticación de Django

    # Pasar la información del usuario a la plantilla
    context = {'usuario': usuario}
    return render(request, 'ourschool/perfil.html', context)


def lista_usuarios(request):
    # Obtener datos de la base de datos
    data = Usuario.objects.all()

    # Pasar los datos a la plantilla
    return render(request, 'ourschool/inicio_estudiante.html', {'data': data})

def actualizar_perfil(request):
    if request.method == 'POST':
        form = UsuarioUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('pprincipal')  # Redirige al perfil después de la actualización
    else:
        form = UsuarioUpdateForm(instance=request.user)

    return HttpResponseRedirect(reverse('perfil'))