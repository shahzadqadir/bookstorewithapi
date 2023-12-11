from django import forms


class BulkBookAdditionForm(forms.Form):
    filename = forms.CharField(max_length=500)