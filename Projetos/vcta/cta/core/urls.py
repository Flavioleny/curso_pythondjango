from django.conf.urls import url

from cta.core.views import home #, cadastro_usuario

urlpatterns = [
    url(r'^$', home, name='home'),
    #url(r'^cadastro-usuario/$', cadastro_usuario, name='cadastrousuario'),
]