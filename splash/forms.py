from django import forms

from .models import MyModel
from .widgets import BaseInputSelectMultiple

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)

class FormOne(BaseForm):
    multiple_choice_field = forms.ModelMultipleChoiceField(
        label="Multiple Choice Field Label",
        required=False,
        choices=["MULTIPLE_CHOICE_FIELD_CHOICES"]
    )
    custom_widget_field = forms.MultipleChoiceField(
        label="Custom Widget Field Label",
        required=False,
        choices=["CUSTOM_WIDGET_FIELD_CHOICES"],
        widget=BaseInputSelectMultiple,
    )

    class Meta:
        model = MyModel
        fields = (
            "boolean_field",
            "integer_field",
            "char_field",
            "decimal_field",
            "date_field",
            "choice_field",
        )

    def __init__(self, *args, **kwargs):
        super(FormOne, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned = super().clean()

        return cleaned

    def clean_char_field(self):
        char_field = self.cleaned_data.get("char_field")

        if char_field.startswith("A"):
            raise forms.ValidationError("Can't start a field with 'A'!")
        
        return char_field

    def save(self, *args, **kwargs):
        my_model = super(MyModel, self).save(*args, **kwargs)

        return my_model
