from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required
from models import Couch
from django.http import HttpResponse

@login_required
@render_to('dashboard.html')
def dashboard(request):
  "The user dashboard"
  return {}

@login_required
def transactions(request):
  "The user's transactions archive"
  c=Couch()
  json=c.query_by_user(request.user.pk)
  jsonp='document.getElementById("transactions").innerHTML=_.jsonreport(\'%s\');' % json
  return HttpResponse(jsonp)
