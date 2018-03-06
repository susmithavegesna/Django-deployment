from django import template

register = template.Library()

def cutfn(value,arg):
    # Cuts out all values of arg from string
    return value.replace(arg,'')

register.filter('cutkey',cutfn)
