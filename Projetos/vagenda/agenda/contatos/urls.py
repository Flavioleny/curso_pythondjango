from django.conf.urls import url

from agenda.contatos.views import add_contato
from agenda.contatos.views import cadastro_sucesso
from agenda.contatos.views import lista_contatos
from agenda.contatos.views import apagar_contato
from agenda.contatos.views import editar_contato

urlpatterns = [
    url(r'^adicionar-contato/$', add_contato, name='addcontato'),
    url(r'^sucesso/$', cadastro_sucesso, name='sucesso'),
    url(r'^lista-contatos/$', lista_contatos, name='listacontatos'),
    url(r'^deletar-contatos/(?P<id>\d+)/$', apagar_contato, name='apagarcontatos'),
    url(r'^editar-contatos/(?P<id>\d+)/$', editar_contato, name='editarcontatos'),   
]