from django.shortcuts import render, redirect
from .models import Motorista, Veiculo, Controle
from collections import defaultdict

def home(request):
    controles = Controle.objects.all()
    
    return render(request, "home/index.html", {"controles": controles}) 

# Motorista

def cadastro_motorista(request):
    motoristas = Motorista.objects.all()
    return render(request, "cadastro_motorista/index.html", {"motoristas": motoristas})

def cadastrar_motorista(request):
    nome = request.POST.get("nome_completo")
    telefone = request.POST.get("telefone")
    cnh = request.POST.get("cnh")

    Motorista.objects.create(nome=nome, telefone=telefone, cnh=cnh)
    motoristas = Motorista.objects.all()
    return render(request, "cadastro_motorista/index.html", {"motoristas": motoristas})

# Veiculo

def cadastro_veiculo(request):
    veiculos = Veiculo.objects.all()
    return render(request, "cadastro_veiculo/index.html", {"veiculos": veiculos})

def cadastrar_veiculo(request):
    placa = request.POST.get("placa")
    marca = request.POST.get("marca")
    modelo_veiculo = request.POST.get("modelo_veiculo")
    km_troca_oleo = request.POST.get("km_troca_oleo")

    Veiculo.objects.create(placa=placa, marca=marca, modelo_veiculo=modelo_veiculo, km_troca_oleo=km_troca_oleo)
    veiculos = Veiculo.objects.all()
    return render(request, "cadastro_veiculo/index.html", {"veiculos": veiculos})

#Controle
def cadastro_controle(request):
    motoristas = Motorista.objects.all()
    veiculos = Veiculo.objects.all()
    dados = {
        'motoristas':motoristas,
        'veiculos':veiculos
    }

    return render(request, "home/cadastro_controle.html", dados)

def cadastrar_controle(request):
    v = request.POST.get("veiculo")
    m = request.POST.get("motorista")
    veiculo = Veiculo.objects.get(id=v)
    motorista = Motorista.objects.get(id=m)
    data_saida = request.POST.get("data_saida")
    hora_saida = request.POST.get("hora_saida")
    km_saida = request.POST.get("km_saida")
    destino = request.POST.get("destino")
    data_retorno = request.POST.get("data_retorno")
    hora_retorno = request.POST.get("hora_retorno")
    km_retorno = request.POST.get("km_retorno")
    km_percorrido =str(int(km_retorno) - int(km_saida)) 
    Controle.objects.create(veiculo=veiculo, motorista=motorista, data_saida=data_saida, hora_saida=hora_saida,   km_saida=km_saida, destino=destino, data_retorno=data_retorno, hora_retorno=hora_retorno, km_retorno=km_retorno, km_percorrido=km_percorrido)
    controles = Controle.objects.all()
    return render(request, "home/index.html", {"controles": controles})

# def editar_controle(request, id):
#     # NÃO FINALIZADO
#     controle = Controle.objects.get(id=id)
#     return render(request, "home/update.html", {"controle":controle})

# def update_controle(request, id):
#     # NÃO FINALIZADO
#     v = request.POST.get("veiculo")
#     m = request.POST.get("motorista")
#     veiculo = Veiculo.objects.get(id=v)
#     motorista = Motorista.objects.get(id=m)
#     data_saida = request.POST.get("data_saida")
#     hora_saida = request.POST.get("hora_saida")
#     km_saida = request.POST.get("km_saida")
#     destino = request.POST.get("destino")
#     data_retorno = request.POST.get("data_retorno")
#     hora_retorno = request.POST.get("hora_retorno")
#     km_retorno = request.POST.get("km_retorno")
#     km_percorrido =str(int(km_retorno) - int(km_saida))

#     controle = Controle.objects.get(id=id)

#     controle.veiculo = veiculo
#     controle.motorista = motorista
#     controle.data_saida = data_saida
#     controle.hora_saida = hora_saida
#     controle.km_saida = km_saida
#     controle.destino = destino
#     controle.data_retorno = data_retorno
#     controle.hora_retorno = hora_retorno
#     controle.km_percorrido = km_percorrido

#     controle.save()

#     return redirect(home)

