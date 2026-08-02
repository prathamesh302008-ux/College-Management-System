from django import forms

from .models import Notice


class NoticeForm(forms.ModelForm):

    class Meta:

        model = Notice

        fields = "__all__"

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4
                }
            ),

            "notice_date": forms.DateInput(
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