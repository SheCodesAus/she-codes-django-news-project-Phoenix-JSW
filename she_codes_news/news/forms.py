from django import forms
from django.utils import timezone
from django.forms import ModelForm, SplitDateTimeField, SplitDateTimeWidget

from .models import NewsStory, Category
from .models import NewsStory

class StoryForm(ModelForm):
    pub_date = SplitDateTimeField(
        widget=SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        ),
        label="Published on"
    )
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image', 'story_category', 'content']
        labels = {'image': "Image URL"}
        widgets = {
            'pub_date': forms.DateInput(
                format = ('%m/%d/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'category': forms.ModelMultipleChoiceField(
                widget = forms.SelectMultiple,
                queryset = Category.objects.all()
            ),
        }