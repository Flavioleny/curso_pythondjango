from django import forms

from .models import Contato

class ContatoForm(forms.ModelForm):
	class Meta:
		model = Contato
		fields = ('nome','email','telefone','sexo','cidade') #Mostra os campo na visualizacao html
		#exclude = ('nome',) //Excluir os campo na visualizacao html
