from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# link to info: http://code.techandstartup.com/django/registration/
# The custom User Registration Form inherits from Django's UserCreationFrom
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

    def save(self, commit=True):  # commit means save data to the database
        # create a user from this registration form
        user = super(UserRegisterForm, self).save(commit=False)  # False here means don't save User yet

        # cleaned data makes sure that data being passed in is valid enough to be stored in the database
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']

        if commit:
            user.save()  # runs sql on the database to store in the database
        return user