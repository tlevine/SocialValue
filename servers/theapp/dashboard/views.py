from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required
from models import Archive

@login_required
@render_to('dashboard.html')
def dashboard(request):
  "The user dashboard
  transactions=[a. Archive.objects.filter(owner=request.user)
  return {"transactions":transactions}
