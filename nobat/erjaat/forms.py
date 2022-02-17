from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _
from .models import Erjaat


class ErjaatForm(ModelForm):
    class Meta:
        model = Erjaat
        fields = ['asli','faree','bakhsh','babat','malek_mellicode']
        widgets = {
            'asli': TextInput(attrs={'class': 'form-control' }),
        }
        labels = {
            'asli': _('اصلی'),
        }
