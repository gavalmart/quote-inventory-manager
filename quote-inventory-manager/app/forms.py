from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm

from django.forms.utils import ErrorList
from .models import Customer, Maker, Provider, Hdd_Capacity, Nas_Accessory, Nas_Accessory_Category, Nas_Model

from crispy_forms.helper import FormHelper

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 


class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProviderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class MakerForm(ModelForm):
    class Meta:
        model = Maker
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(MakerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class HddCapacityForm(ModelForm):
    class Meta:
        model = Hdd_Capacity
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(HddCapacityForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False






































































class NasAccessoryCategoryForm(ModelForm):
    class Meta:
        model = Nas_Accessory_Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super.helper = FormHelper()
        super.helper.form_show_labels = False



class Nas_Accessory(ModelForm):
    class Meta:
        model = Nas_Accessory
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super.helper = FormHelper()
        super.helper.form_show_labels = False


class Nas_Model (ModelForm):
    class Meta:
        model = Nas_Model
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        super.helper = FormHelper()
        super.helper.form_show_labels = False