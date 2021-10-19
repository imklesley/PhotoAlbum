from django.forms.models import ModelForm
from .models import Photo


class AddPhoto(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
