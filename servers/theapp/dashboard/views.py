from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required
from models import Couch
from django.http import HttpResponse

c=Couch()

@login_required
@render_to('dashboard.html')
def dashboard(request):
  "The user dashboard"
  return {}

@login_required
def transactions(request):
  "The user's transactions archive"
  json=c.query_by_user(request.user.pk)
  jsonp='chainsaw(\'%s\');' % json
  return HttpResponse(jsonp,mimetype='text/javascript')

@login_required
def transaction(request,uuid):
  json=c.query_by_uuid(uuid)
  print json
  jsonp='chainsaw(\'%s\');' % json
  print jsonp
  return HttpResponse(jsonp,mimetype='text/javascript')

@login_required
@render_to('edit.html')
def edit(request,uuid):
  "Edit a transaction."
  return {"transaction_uuid":uuid}
