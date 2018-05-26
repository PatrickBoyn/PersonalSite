from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    title = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        pass
