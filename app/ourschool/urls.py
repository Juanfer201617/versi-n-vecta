from django.urls import path
from . import views
from .views import lista_usuarios

urlpatterns = [
    path('', views.inicio,name="inicio"),
    path('registro/', views.registrarse, name='registarse'),
    path('iniciar/', views.iniciar, name='iniciar'),
    path('pprincipal/', views.iniciar, name='pprincipal'),
    path('cerrar_session/', views.cerrar_session, name='cerrar_session'),
    path('registrarse/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('actualizar_perfil', views.actualizar_perfil, name='actualizar_perfil'),
    path('inicio_estudiante/', lista_usuarios, name='inicio_estudiante'),


]
