from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit

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


class UserProfileForm(forms.ModelForm):

    def eighteen(self):
        max_year = 19

        return max_year

    def __init__(self, *args,  **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput()
        self.fields['last_name'].widget = forms.TextInput()
        self.fields['address_city'].widget = forms.TextInput()
        self.fields['bio'].widget = forms.Textarea()
        self.fields['goal'].widget = forms.Textarea()
        self.fields['date_of_birth'].widget = forms.SelectDateWidget(years=range(1970,1999), attrs=({'style':'width:20%; height:33%; display: inline-block;'}))
        self.fields['goal'].widget = forms.Textarea()
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div('last_name', css_class="col-md-4"),
                Div('first_name', css_class="col-md-4"),
                css_class='row'
            ),
            Div(
                Div('address_city', css_class="col-md-3"),
                Div('address_state', css_class="col-md-3"),
                css_class='row'
            ),
            Div(
                Div('height', css_class="col-md-2"),
                Div('weight', css_class="col-md-2"),
                Div('gender', css_class="col-md-2"),
                css_class='row'
            ),
            Div(
                Div('date_of_birth', css_class="col-md-8"),
                css_class='row'
            ),
            Div(
                Div('image_url', css_class="col-md-10"),
                css_class='row'
            ),
            Div(
                Div('bio', css_class="col-md-6"),
                css_class='row'
            ),
            Div(
                Div('goal', css_class="col-md-6"),
                css_class='row'
            ),
            Div(
                 Div('activities', css_class="col-md-6"),
                 css_class='row'
            ),
            Submit('Update', 'Update', css_class='btn btn-primary"'),
        )

    class Meta:
        model = UserProfile

        fields = ['first_name', 'last_name','address_city', 'address_state',
                  'date_of_birth', 'gender',
                  'bio', 'goal', 'activities',
                  'image_url', 'height', 'weight']