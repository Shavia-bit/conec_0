from django import forms

class Emails(forms.Form):
    Email = forms.EmailField()
    
    def __str__(self):
        return self.Email