from annoying.decorators import render_to

@render_to('dashboard.html')
def dashboard(request):
  return {}
