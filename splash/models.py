from django.db import models
from django.utils.translation import gettext_lazy as _

class MyModel(models.Model):
    boolean_field = models.BooleanField(default=False)
    integer_field = models.IntegerField(max_value=100)
    char_field = models.CharField(max_length=100)
    decimal_field = models.DecimalField(max_digits=4, decimal_places=1, default=0.0)
    date_field = models.DateField(auto_now_add=True)

    class ChoiceFieldChoices(models.IntegerChoices):
        CHOICE_ZERO = 0, _("Choice Zero")
        CHOICE_ONE = 1, _("Choice One")
        CHOICE_TWO = 2, _("Choice Two")
    choice_field = models.IntegerField(choices=ChoiceFieldChoices.choices)


    def __str__(self):
        return f"{self.boolean_field}: {self.integer_field}: {self.char_field}: {self.choice_field} : {self.decimal_field} : {self.date_field}"

    def save(self, *args, **kwargs):
        super(MyModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["char_field"]
        verbose_name = "MyModel"
        verbose_name_plural = "MyModels"
