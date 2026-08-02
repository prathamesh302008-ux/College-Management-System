from django import forms

from .models import Faculty


class FacultyForm(forms.ModelForm):

    class Meta:

        model = Faculty

        fields = [

            "faculty_id",

            "first_name",

            "last_name",

            "email",

            "phone",

            "department",

            "qualification",

            "joining_date",

            "photo",

        ]

        widgets = {

            "joining_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

        }