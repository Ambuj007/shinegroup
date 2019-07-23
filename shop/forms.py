from django import forms
from .Lists import PRODUCT_CHOICES, SPEAKER, STORAGE_SPEC, SPEAKER_TYPE, STORAGE, CAMERA_SPEC, BRAND, SMALL_STORAGE, KB_MOUSE, UPS, USER, ANTIVIRUS, PRINTER, COMP_PERIPHERALS, DVR_SMPS, CAMERA, CCTV
from django.contrib.auth import authenticate


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    subject = forms.CharField(required=False, max_length=100)
    sender = forms.EmailField(required=False)
    phone = forms.CharField(required=False, max_length=13)
    message = forms.CharField(required=False, max_length=200, widget=forms.Textarea(
        attrs={'rows': 4, 'cols': 40}))


class StockForm(forms.Form):
    item_class = forms.CharField(label='It Is', required=False, widget=forms.Select(
        attrs={'class': 'input-sm'}, choices=sorted(PRODUCT_CHOICES, reverse=False)))
    brand = forms.CharField(required=False, widget=forms.Select(
        choices=sorted(BRAND, reverse=False)))
    item_type = forms.CharField(max_length=120, label='Type',  required=False)
    speaker = forms.CharField(label='Type', required=False, widget=forms.Select(
        choices=sorted(SPEAKER, reverse=False)))
    storage = forms.CharField(label='Type', required=False, widget=forms.Select(
        choices=sorted(STORAGE, reverse=False)))
    cctv = forms.CharField(label='Item', required=False, widget=forms.Select(
        choices=sorted(CCTV, reverse=False)))
    camera = forms.CharField(label='Type', required=False, widget=forms.Select(
        choices=sorted(CAMERA, reverse=False)))
    dvr_smps = forms.CharField(
        label='Type', required=False, widget=forms.Select(choices=DVR_SMPS))
    comp_peripherals = forms.CharField(label='Type', required=False, widget=forms.Select(
        choices=sorted(COMP_PERIPHERALS, reverse=False)))
    kb_mouse = forms.CharField(label='Specification', required=False, widget=forms.Select(
        choices=sorted(KB_MOUSE, reverse=False)))
    ups = forms.CharField(label='Type', required=False, widget=forms.Select(
        choices=sorted(UPS, reverse=False)))
    antivirus = forms.CharField(label='Type', required=False, widget=forms.Select(
        choices=sorted(ANTIVIRUS, reverse=False)))
    printer = forms.CharField(label='Type', required=False, widget=forms.Select(
        choices=sorted(PRINTER, reverse=False)))
    item_specification = forms.CharField(
        max_length=120, label='Specification',  required=False)
    user = forms.CharField(label='Specification',
                           required=False, widget=forms.Select(choices=USER))
    camera_spec = forms.CharField(label='Specification', required=False, widget=forms.Select(
        choices=sorted(CAMERA_SPEC, reverse=False)))
    storage_spec = forms.CharField(
        label='Specification', required=False, widget=forms.Select(choices=STORAGE_SPEC))
    small_storage = forms.CharField(
        label='Specification', required=False, widget=forms.Select(choices=SMALL_STORAGE))
    speaker_type = forms.CharField(label='Specification', required=False, widget=forms.Select(
        choices=sorted(SPEAKER_TYPE, reverse=False)))
    model_no = forms.CharField(max_length=120, required=False)
    purchase_price = forms.DecimalField(max_digits=10, decimal_places=2)
    selling_price = forms.DecimalField(max_digits=10, decimal_places=2)

    def clean(self, *args, **kwargs):
        selling_price = self.cleaned_data.get("selling_price")
        purchase_price = self.cleaned_data.get("purchase_price")
        if selling_price <= purchase_price:
            raise forms.ValidationError("Ismein Tera Ghata")
        return super(ProductView, self).clean(*args, **kwargs)


class LoginForm(forms.Form):
    username = forms.CharField(label='User', required=True)
    password = forms.CharField(
        label='Password', required=True, widget=forms.PasswordInput())

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("User does not exists.")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")

            if not user.is_active:
                raise forms.ValidationError("User is not active")
        return super(LoginForm, self).clean(*args, **kwargs)


class NoticeForm(forms.Form):
    notice = forms.CharField(required=False, max_length=100)


class DemandForm(forms.Form):
    item = forms.CharField(required=True, max_length=100)
    quantity = forms.IntegerField(required=True, min_value=1)
