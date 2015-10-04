from django import forms
from blog.models import Group, Comment, Apply


class GroupForm(forms.ModelForm):
   class Meta:
      model = Group
      fields = ['creator', 'status', 'name', 'group', 'content', 'image', 'numb', 'si', 'gu',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2}),
        }

class ApplicantForm(forms.ModelForm):
   class Meta:
      model = Apply
      fields = ['is_approved',]
