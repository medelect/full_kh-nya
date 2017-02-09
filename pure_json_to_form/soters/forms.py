from django.forms import ModelForm
from soters.models import Dog, Author, Book
from django import forms
import json


#from models import Widget

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class MyForm(forms.Form):
    original_field = forms.CharField()
    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields

        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = forms.CharField()

class DynamicForm(forms.Form):

    def __init__(self, some_data, *args, **kwargs):
        super(DynamicForm, self).__init__(*args, **kwargs)
        for i, requisite in enumerate(some_data.requisites_list):
            regex = requisite['regexp']
            label = requisite['name']
            self.fields['requisite_%s' % i] = forms.RegexField(regex=regex, label=label)


class FieldHandler():
    formfields = {}
    
    def __init__(self, fields):
        for field in fields:
            options = self.get_options(field)
            f = getattr(self, "create_field_for_"+field['type'] )(field, options)
            self.formfields[field['name']] = f

    def get_options(self, field):
        options = {}
        options['label'] = field['label']
        options['help_text'] = field.get("help_text", None)
        options['required'] = bool(field.get("required", 0) )
        return options

    def create_field_for_text(self, field, options):
        options['max_length'] = int(field.get("max_length", "20") )
        return django.forms.CharField(**options)

    def create_field_for_textarea(self, field, options):
        options['max_length'] = int(field.get("max_value", "9999") )
        return django.forms.CharField(widget=django.forms.Textarea, **options)

    def create_field_for_integer(self, field, options):
        options['max_value'] = int(field.get("max_value", "999999999") )
        options['min_value'] = int(field.get("min_value", "-999999999") )
        return django.forms.IntegerField(**options)

    def create_field_for_radio(self, field, options):
        options['choices'] = [ (c['value'], c['name'] ) for c in field['choices'] ]
        return django.forms.ChoiceField(widget=django.forms.RadioSelect,   **options)

    def create_field_for_select(self, field, options):
        options['choices']  = [ (c['value'], c['name'] ) for c in field['choices'] ]
        return django.forms.ChoiceField(  **options)

    def create_field_for_checkbox(self, field, options):
        return django.forms.BooleanField(widget=django.forms.CheckboxInput, **options)

def get_form(jstr):
    fields=json.loads(jstr)
    fh = FieldHandler(fields)
    return type('DynaForm', (forms.Form,), fh.formfields )

def get_form2(jlst):
    fh = FieldHandler(jlst)
    return type('DynaForm', (forms.Form,), fh.formfields )
