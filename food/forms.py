from django import forms
from food.models import Food


class FoodCreationForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name']

    def save(self, commit=True):
        new_food = Food.objects.create(
            name=self.cleaned_data.get('name'),
        )
        return new_food


class FoodChangeForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name']