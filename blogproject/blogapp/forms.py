from django import forms
from .models import post



#creating a  form

class blogform(forms.ModelForm):

    #class meta creating
    class Meta:

        model = post
        
        fields = [
            "title",
            "body",
            
            "Create_at"
        ]
