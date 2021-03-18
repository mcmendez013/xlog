from django import forms

from .models import Category, Entry

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['text']
        labesl = {'text':''} 

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = {'text'}
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})} 
