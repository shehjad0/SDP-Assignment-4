from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        widgets = {
            'task_assign_date' : forms.NumberInput(attrs={'type': 'date'}),
            'categories': forms.CheckboxSelectMultiple(),
        }