from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Appointment, Contact, Comment

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['fname', 'lname', 'email', 'message']