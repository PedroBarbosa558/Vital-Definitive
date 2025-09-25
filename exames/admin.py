from django.contrib import admin
from .models import AcessoMedico, ExamesRealizados, TiposExames, PedidosExames, SolicitacaoExame


admin.site.register(TiposExames)
admin.site.register(PedidosExames)
admin.site.register(SolicitacaoExame)
admin.site.register(AcessoMedico)
admin.site.register(ExamesRealizados)



