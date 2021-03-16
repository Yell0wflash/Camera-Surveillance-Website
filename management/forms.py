from django import forms
from .models import Camera
from .models import Location
from .models import CameraSurvelliance
from .models import Camerachoose

class CameraForm(forms.ModelForm):
    class Meta:
        model=Camera
        fields='__all__'

class LocationForm(forms.ModelForm):
    class Meta:
        model=Location
        fields='__all__'

class CameraSurvellianceForm(forms.ModelForm):
    class Meta:
        model=CameraSurvelliance
        fields='__al__'

class CamerachooseForm(forms.ModelForm):
    class Meta:
        model=Camerachoose
        fields='__all__'