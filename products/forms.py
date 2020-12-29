from django import forms
from django.core.mail import send_mail, send_mass_mail
from pagedown.widgets import AdminPagedownWidget
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout
from products.models import Product
from crispy_forms.helper import FormHelper
# from crispy_forms import css_id
from crispy_forms.bootstrap import InlineField
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, Div
from captcha.fields import ReCaptchaField
class ProductBodyForm(forms.ModelForm):
    description = forms.CharField(widget=AdminPagedownWidget)

    class Meta:
        model = Product
        fields = "__all__"

class ContactPostForm(forms.Form):
    name = forms.CharField(max_length=25, required=True, 
        widget=forms.TextInput(attrs={'class': '', 'style': 'height:40px;font-size:20px;'}), 
        label='<i class="fas fa-user"></i> Name'
    )
    email = forms.EmailField(required=True, 
        widget=forms.TextInput(attrs={'class': '', 'style': 'height:40px;font-size:20px;'}),
        label='<i class="fas fa-envelope-square"></i> E-mail'
    )
    phone_number = forms.CharField(max_length=11, 
        widget=forms.NumberInput(attrs={'type': 'tel', 'class': '', 'style': 'height:40px;font-size:20px;'}), 
        label='<i class="fas fa-phone"></i> Phone Number'
    )   
    message = forms.CharField(required=True, 
        widget=forms.Textarea(attrs={'class': '', 'style': 'font-size:20px;', 'rows': '5'}),
        label='<i class="fas fa-comment"></i> Your Message'
    )
    captcha = ReCaptchaField()


    def __init__(self, *args, **kwargs):
        super(ContactPostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        # 
        self.helper.layout = Layout(
            Div(
                Div(
                    'name',
                    css_class = "col-md-5 p-0"),
                Div(
                    'email',
                    css_class = "col-md-5 p-0"),
                css_class = "row no-gutters p-0 justify-content-md-between",
            ),
           'phone_number',
           'message',
           'captcha',
        )