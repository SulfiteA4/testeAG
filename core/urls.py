from django.contrib import admin
from django.urls import path, include
from .views import home, cadastro_motorista, cadastrar_motorista, cadastro_veiculo, cadastrar_veiculo, cadastro_controle, cadastrar_controle

urlpatterns = [
    path('', home),
    # url Motorista
    path('cadastro_motorista/', cadastro_motorista, name="cadastro_motorista"), 
    path('cadastrar_motorista/', cadastrar_motorista, name="cadastrar_motorista"), 
    # url Veiculo
    path('cadastro_veiculo/', cadastro_veiculo, name="cadastro_veiculo"), 
    path('cadastrar_veiculo/', cadastrar_veiculo, name="cadastrar_veiculo"), 
    # url controle
    path('cadastro_controle/', cadastro_controle, name="cadastro_controle"), 
    path('cadastrar_controle/', cadastrar_controle, name="cadastrar_controle"), 

    # path('editar_controle/<int:id>', editar_controle, name="editar_controle"),  
    # path('update_controle/<int:id>', update_controle, name="update_controle")


]
