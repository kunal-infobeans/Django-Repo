from django import forms
from django.core import validators
from first_app.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
  class Meta():
     model = UserProfileInfo
     fields = ('portfolio_site','profile_pic')  















# class NewUser(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'

# def check(value):
#      if value[0].lower() != 'z':
#          raise forms.ValidationError("Need to start with Z")


# class FormName(forms.Form):
#     name = forms.CharField(validators=[check])
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter your email again')
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False,
#                                  widget=forms.HiddenInput,
#                                  validators=[validators.MaxLengthValidator])
    
#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         vemail = all_clean_data['verify_email']

#         if email != vemail:
#             raise forms.ValidationError("Make sure email matches")
    # def clean_botcatcher(self):
    #     botcatcher = self.changed_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA Bot!")
    #     return botcatcher