from django import template
register = template.Library()

@register.simple_tag(name="navbar_items")
def navbar_items(value=5):
  navbar_links = [ 
    { 'text': 'Home', 'url_key': 'index' },
    { 'text': 'Admin', 'url_key': 'admin:index' }
  ] 
  
  return navbar_links

@register.simple_tag(name="register_item")
def register_item():
  return { 'text': 'Register', 'url_key': 'basic_app:register' }

@register.simple_tag(name="login_item")
def login_item():
  return { 'text': 'Login', 'url_key': 'basic_app:login' }

@register.simple_tag(name="logged_in")
def logged_in():
  return False
