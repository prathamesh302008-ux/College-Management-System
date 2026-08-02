from django import forms

from .models import Fee


class FeeForm(forms.ModelForm):

    class Meta:

        model = Fee

        fields = "__all__"

        widgets = {

            "student": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "total_fee": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "paid_fee": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "payment_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

        }