from django import forms
from .models import Student



class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = [

            "enrollment_no",
            "first_name",
            "last_name",
            "email",
            "phone",
            "course",
            "semester",
             "photo",

        ]


        widgets = {


            "enrollment_no": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Enter Enrollment No"
                }
            ),


            "first_name": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Enter First Name"
                }
            ),


            "last_name": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Enter Last Name"
                }
            ),


            "email": forms.EmailInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Enter Email"
                }
            ),


            "phone": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Enter Phone"
                }
            ),


            "course": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Enter Course"
                }
            ),


            "semester": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Enter Semester"
                }
            ),

        }