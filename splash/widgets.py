from django.forms import CheckboxSelectMultiple


class BaseInputSelectMultiple(CheckboxSelectMultiple):
    template_name = "components/forms/base_input_select_multiple.html"

    # class Media:
    #     js = ("path/to/javascript.js",)
