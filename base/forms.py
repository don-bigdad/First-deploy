from django import forms
from base import models


class ReservationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "type": "type",
            "name": "name",
            "class": "form-control",
            "id": "name",
            "placeholder": "Your Name",
            "data - rule": "minlen:4",
            "data - msg": "Please enter at least 4 chars",

        })
    )
    mail = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        "type": "email",
        "class": "form-control",
        "name": "email",
        "id": "email",
        "placeholder": "Your Email",
        "data - rule": "email",
        "data - msg": "Please enter a valid email",
    })
                           )
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        "type": "text",
        "class": "form-control",
        "name": "phone",
        "id": "phone",
        "placeholder": "Your Phone",
        "data - rule": "minlen:4",
        "pattern":"[0-9]{11}",
        "title":"Wrong number,length of phone number must be 11",
        "data - msg": "Please enter at least 4 chars",
    })
                            )
    date = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        "type": "text",
        "name": "date",
        "class": "form-control",
        "id": "date",
        "placeholder": "Date",
        "data-rule": "minlen:4",
        "data - msg": "Please enter at least 4 chars",
    })
                    )
    time = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        "type": "text",
        "class": "form-control",
        "name": "time",
        "id": "time",
        "placeholder": "Time",
        "data-rule": "minlen:4",
        "data - msg": "Please enter at least 4 chars",
    })
                           )
    number_of_people = forms.IntegerField(widget=forms.NumberInput(attrs={
        "type": "number",
        "class": "form-control",
        "name": "people",
        "id": "people",
        "placeholder": "# of people",
        "data - rule": "minlen:1",
        "data - msg": "Please enter at least 1 chars",
    })
    )
    text = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": "5",
        "placeholder": "Message",
    })
                           )

    class Meta:
        model = models.ReservationForm
        fields = ('name', "mail", "phone", "date", "time", "number_of_people", "text")


class Contact(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "type": "text",
            "name": "name",
            "class": "form-control",
            "id": "name",
            "placeholder": "Your Name",
            "required": ""
        })
    )
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "type": "email",
        "class": "form-control",
        "name": "email",
        "id": "email",
        "placeholder": "Your Email",
        "required": "",
    })
                            )
    subject = forms.CharField(max_length=70, widget=forms.TextInput(attrs={
        "type": "text",
        "class": "form-control",
        "name": "subject",
        "id": "subject",
        "placeholder": "Subject",
        "required": "",
    })
                              )
    text = forms.CharField(max_length=500,required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "name": "message",
        "rows": "5",
        "placeholder": "Message",
        "required": "",
    })
                           )

    class Meta:
        model = models.Contact
        fields = ('name', "email","subject","text")