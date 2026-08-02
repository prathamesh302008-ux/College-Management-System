from django import forms

from .models import Attendance


class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = "__all__"

        widgets = {

            "student": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "attendance_date": forms.DateInput(
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

            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),

        }