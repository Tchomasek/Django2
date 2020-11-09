from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    #email = forms.EmailField()
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'id'
        ]

    '''def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "cfe" in title:
            raise forms.ValidationError('error')
        return title'''

    '''def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("z"):
            raise forms.ValidationError('error')
        return email'''


class RawProductForm(forms.Form):
    id = forms.IntegerField()
    title = forms.CharField(label='')
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
                                                                            'placeholder': 'placeholder',
                                                                            'cols': 120
        }))
    price = forms.DecimalField(initial=0)
