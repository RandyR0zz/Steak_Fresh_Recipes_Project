from django import forms
from django.core.exceptions import ValidationError

def validate_symbols(value):
    
    '''Function for validation special symbol(s) or empty data'''
    
    symbols = '@#$%^&*()_+=<>/\`~|]['
    
    for symbol in symbols:
        for letter in value:
            if symbol == letter:
                raise ValidationError('Must not contain special symbol(s)')
    
    return value

class AddPost(forms.Form):
    
    '''
    Class of creating a post form
    
    Attributes
    ----------
    title : str
        Title(s) of post(s)
    content : str
        Content(s) of post(s)
    recipe : str
        Recipes(s) of post(s)
    '''
    
    title = forms.CharField(validators=[validate_symbols], max_length=100, widget=forms.Textarea(attrs={'placeholder': 'Title'}))
    content = forms.CharField(validators=[validate_symbols], max_length=1000, widget=forms.Textarea(attrs={'placeholder': 'Content'}))
    recipe = forms.CharField(validators=[validate_symbols], widget=forms.Textarea(attrs={'placeholder': 'Recipe'}))