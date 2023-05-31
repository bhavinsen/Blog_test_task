from dataclasses import fields
from turtle import title
from django import forms
from .models import Author, Book  


class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(),
                                    to_field_name = 'name',
                                    empty_label="Select Author")  
    
    class Meta:
        model =Book
        fields= ['title', 'author']
        
    def clean(self):
 
        # data from the form is fetched using super function
        super(BookForm, self).clean()
         
        # extract the username and text field from the data
        title = self.cleaned_data.get('title')
 
        # conditions to be met for the username length
        if Book.objects.filter(title= title).exists():   
            self._errors['title'] = self.error_class([
                'Title already exists'])
        return self.cleaned_data  