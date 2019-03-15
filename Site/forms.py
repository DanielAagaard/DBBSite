from django import forms

class SiteForm(forms.Form):
    Title = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class' : 'txtField'}))
    Year = forms.CharField(max_length=4, widget=forms.NumberInput(attrs={'class' : 'numField', 'min' : '1900', 'max' : '2019', 'value' : '2019', 'onkeydown' : 'return false'}))
    Rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'numField', 'min' : '0', 'max' : '10', 'value' : '10', 'onkeydown' : 'return false'}))