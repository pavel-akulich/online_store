from django import forms

from catalog.models import Product, Version
from catalog.validators import validate_even


class ProductForm(forms.ModelForm):
    name = forms.CharField(validators=[validate_even],
                           label='Наименование продукта',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Впишите название',
                               }
                           ))

    description = forms.CharField(validators=[validate_even],
                                  label='Описание',
                                  widget=forms.Textarea(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder': 'Опишите ваш продукт',
                                      }
                                  ))

    class Meta:
        model = Product
        fields = ('name', 'description', 'photo', 'category', 'price',)
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Впишите цену'})
        }


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'version_number', 'version_name', 'is_active',)
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'version_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'version_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
