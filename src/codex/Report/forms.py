from django .forms import ModelForm
from .models import Report

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['title','author','schools','categories','subjects','regions','report']
