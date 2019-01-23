from django import forms
from .models import *

# class AuthorForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     email = forms.EmailField()
#     active = forms.BooleanField(required=False) # required=False makes the field optional
#     created_on = forms.DateTimeField()
#     last_logged_in = forms.DateTimeField()



# Use this in the view
# Bind data from request.POST into a PostForm
# form = PostModelForm(request.POST)

class ReportCommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    active = forms.BooleanField(required=False) # required=False makes the field optional
    created_on = forms.DateTimeField()
    last_logged_in = forms.DateTimeField()
    class Meta:
        fields = '__all__'


class ReportCommentForm2(forms.ModelForm):
    class Meta:
        model = ReportComment
        fields = '__all__'
