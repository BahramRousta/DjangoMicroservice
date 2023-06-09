from django import forms
import requests
from .models import Product


class ProductForm(forms.ModelForm):
    category = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('category_id',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = self.get_category_choices()

    def get_category_choices(self):
        try:
            response = requests.get('http://127.0.0.1:8000/category/api/categories_list/')
            categories = response.json()
            return [(c['id'], c['title']) for c in categories]
        except requests.exceptions.RequestException as e:
            # Log the error or display a user-friendly message
            print(f"Error retrieving categories: {e}")
            return []

    def save(self, commit=True):
        product = super().save(commit=False)
        product.category_id = int(self.cleaned_data['category'])
        if commit:
            product.save()
        return product