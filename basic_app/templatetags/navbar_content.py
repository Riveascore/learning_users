from django import template
register = template.Library()

@register.simple_tag(name="get_navbar_items")
def get_navbar_items(value=5):
  navbar_links = [ 
    { 'text': 'Home', 'url_key': 'index' },
    { 'text': 'Admin', 'url_key': 'admin:index' }
  ] 
  
  return navbar_links

@register.simple_tag(name="get_register_item")
def get_register_item():
  return { 'text': 'Register', 'url_key': 'basic_app:register' }

@register.simple_tag(name="get_login_item")
def get_login_item():
  return { 'text': 'Login', 'url_key': 'basic_app:login' }

@register.simple_tag(name="get_logged_in")
def get_logged_in():
  return False
