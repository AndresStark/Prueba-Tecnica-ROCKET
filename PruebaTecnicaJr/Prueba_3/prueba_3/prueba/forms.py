from django import forms

class DetailForm(forms.Form):
    detalle = forms.CharField()

    def __str__(self):
        return str(self.detalle)