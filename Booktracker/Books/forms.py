from django import forms
from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        # fields = ('title', 'author', 'description','status','date')
        fields="__all__"
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'author'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'add your thoughts here :) Naked truths only!'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'date':forms.DateInput(attrs={'class':'form-control'})
        }