from django import forms
from .models import Platform, RecordType, Record, Account, Post

class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name']
        
    def clean(self):
        cleaned_data = super().clean()
        # Convert fields to lowercase
        field1_lower = cleaned_data.get('name', '').lower()
        
        # Update cleaned_data with lowercase values
        cleaned_data['name'] = field1_lower        
        return cleaned_data


class RecordTypeForm(forms.ModelForm):
    class Meta:
        model = RecordType
        fields = ['type']

    def clean(self):
        cleaned_data = super().clean()
        # Convert fields to lowercase
        field1_lower = cleaned_data.get('type', '').lower()
        
        # Update cleaned_data with lowercase values
        cleaned_data['type'] = field1_lower        
        return cleaned_data


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['file_name', 'tags', 'type', 'source_platform', 'author', 'url', 'edited']


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['platform', 'name', 'suffix', 'creation_date']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['account', 'record', 'annotation', 'creation_date', 'platform_specific_reference']
