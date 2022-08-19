from django import forms
from django.contrib.auth import get_user_model,authenticate
User = get_user_model()

class UserRegistration(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text",
        "name":"username",
        "placeholder":"Username",
        "required":"",
        "id":"id_username",
        "pattern":"[A-Za-z0-9]{4,20}",
        "title": "minimal length of user field 4",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "type":"password",
        "name":"password",
        "placeholder":"Password",
        "required":"",
        "id":"id_password",
        "pattern": "[A-Za-z0-9]{4,20}",
        "title": "minimal length of password field 4",

    }))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "type":"password",
        "name":"repeat_password",
        "placeholder":"Repeat Password",
        "required":"",
        "id":"id_repeat_password",
        "pattern": "[A-Za-z0-9]{4,20}",
        "title": "minimal length of user field 4",
    }))

    def clean_repeat_password(self):
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')
        if not repeat_password:
            raise forms.ValidationError("You must confirm your password")
        if password != repeat_password:
            raise forms.ValidationError("Your passwords do not match")
        return repeat_password


    class Meta:
        model = User
        fields = ("username",)

class UserLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "name": "username",
        "placeholder": "Username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "type": "password",
        "name": "password",
        "placeholder": "Password",
        "required":"",
        "id":"id_password",
    }))
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username,password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError("Login or password is uncorrect")
        return super().clean()