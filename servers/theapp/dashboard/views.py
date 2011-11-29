from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required
from models import Couch

@login_required
@render_to('dashboard.html')
def dashboard(request):
  "The user dashboard"
  c=Couch()
  json=c.query_by_user(request.user.pk)
  return {"transactions":json}
