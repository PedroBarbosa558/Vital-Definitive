from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import TiposExames, PedidosExames, SolicitacaoExame, AcessoMedico
from datetime import datetime

@login_required
def solicitar_exames(request):
    tipos_exames = TiposExames.objects.all()
    if request.method == "GET":
        return render(request, 'solicitar_exames.html', {'tipos_exames': tipos_exames})
    elif request.method == "POST":
        exames_id = request.POST.getlist('exames')
        solicitacao_exames = []
        pedido_exames = []
        
        for exame_id in exames_id:
            exame = TiposExames.objects.get(id=exame_id)
            solicitacao = SolicitacaoExame(
                usuario=request.user,
                exame=exame,
                status="E"
            )
            solicitacao.save()
            solicitacao_exames.append(solicitacao)
            
        pedido = PedidosExames(
            usuario=request.user,
            data=datetime.now()
        )
        pedido.save()
        
        for solicitacao in solicitacao_exames:
            pedido.exames.add(solicitacao)
            
        pedido.save()
        
        messages.success(request, 'Pedido de exame realizado com sucesso')
        return redirect('solicitar_exames')

@login_required
def gerar_acesso_medico(request):
    if request.method == "POST":
        identificacao = request.POST.get('identificacao')
        tempo_de_acesso = request.POST.get('tempo_de_acesso')
        data_exame_inicial = request.POST.get('data_exame_inicial')
        data_exame_final = request.POST.get('data_exame_final')
        
        acesso_medico = AcessoMedico(
            usuario=request.user,
            identificacao=identificacao,
            tempo_de_acesso=tempo_de_acesso,
            data_exames_iniciais=data_exame_inicial,
            data_exames_finais=data_exame_final,
            criado_em=timezone.now(),
        )
        acesso_medico.save()
        
        messages.success(request, 'Acesso médico gerado com sucesso')
        return redirect('gerar_acesso_medico')

    acessos_medicos = AcessoMedico.objects.filter(usuario=request.user)
    return render(request, 'gerar_acesso_medico.html', {'acessos_medicos': acessos_medicos})

@login_required
def gerenciar_exames(request):
    exames = SolicitacaoExame.objects.filter(usuario=request.user)
    return render(request, 'gerenciar_exames.html', {'exames': exames})

@login_required
def permitir_abrir_exame(request, exame_id):
    exame = SolicitacaoExame.objects.get(id=exame_id)
    if not exame.requer_senha:
        return redirect(exame.resultado.url)
    
    return redirect(f'/exames/solicitar_senha_exame/{exame_id}')

@login_required
def solicitar_senha_exame(request, exame_id):
    exame = SolicitacaoExame.objects.get(id=exame_id)
    if request.method == "GET":
        return render(request, 'solicitar_senha_exame.html', {'exame': exame})
    elif request.method == "POST":
        senha = request.POST.get("senha")
        if senha == exame.senha:
            return redirect(exame.resultado.url)
        else:
            messages.error(request, 'Senha inválida')
            return redirect(f'/exames/solicitar_senha_exame/{exame_id}')

def acesso_medico(request, token):
    acesso_medico = AcessoMedico.objects.get(token=token)
    
    if timezone.now() > (acesso_medico.criado_em + timezone.timedelta(hours=acesso_medico.tempo_de_acesso)):
        messages.error(request, 'Token expirado')
        return redirect('/')
    
    pedidos = PedidosExames.objects.filter(usuario=acesso_medico.usuario).filter(data__gte=acesso_medico.data_exames_iniciais).filter(data__lte=acesso_medico.data_exames_finais)
    
    return render(request, 'acesso_medico.html', {'pedidos': pedidos})