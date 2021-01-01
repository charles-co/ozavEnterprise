from django import forms
from django.core.mail import send_mail, send_mass_mail
from pagedown.widgets import AdminPagedownWidget
from products.models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineField
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, Div
from captcha.fields import ReCaptchaField

class ProductBodyForm(forms.ModelForm):
    description = forms.CharField(widget=AdminPagedownWidget)

    class Meta:
        model = Product
        fields = "__all__"