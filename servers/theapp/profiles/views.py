from annoying.decorators import render_to

@render_to('profile.html')
def profile(request):
  return {}
