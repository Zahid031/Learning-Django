from django import forms
class feedback(forms.Form):
    tittle=forms.CharField(label="tittle", max_length=50,widget=forms.TextInput (attrs={"class":"form-control"}))
    subject=forms.CharField(label="subject", max_length=200,widget=forms.Textarea (attrs={"class":"form-control"}))