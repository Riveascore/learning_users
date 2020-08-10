def media_url(request):
  from django.conf import settings
  return {'media_url': 'media_url'}
  # navbar_links = [ 
  #   { 'text': 'Home', 'url_key': 'index' },
  #   { 'text': 'Admin', 'url_key': 'admin:index' }
  # ] 
  # register_item = { 'text': 'Register', 'url_key': 'basic_app:register' }
  # login_item = { 'text': 'Login', 'url_key': 'basic_app:login' }
  # logged_in = False
  
  # return {
  #   'navbar_links': navbar_links,
  #   'register_item': register_item,
  #   'login_item': login_item,
  #   'logged_in': logged_in
  # }
