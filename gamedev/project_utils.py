from pprint import pprint as p



# #
# >>> p(ReportComment._meta.get_fields())
# #
# >>> model._meta.get_field('g')) is eval('UrlField'):
# #
# from django.db.models.fields import *
# if model._meta.get_field('g').__class__ is UrlField:
# #


def create_dummy_user():
    from django.test import Client
    c = Client()
    response = c.post('/login/', {'username': 'john', 'password': 'smith'})


def display_model_fields(form):
    p('displaying form fields for: '+str(form))
    for f in form._meta.get_fields():
        p('field: '+str(f.help_text)+' '+str(f.name)+'        | is_required: '+str(f))
        p('attr: ')
        p(dir(f))


def display_form_fields(form):
    p('displaying form fields for: '+str(form))
    fields_dict = form.declared_fields
    for f in fields_dict.values():
        p('field: '+str(f.help_text)+' '+str(f)+'        | is_required: '+str(f.required))
        p('attr: ')
        p(dir(f))
