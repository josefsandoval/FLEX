from django.shortcuts import redirect


# view to make home page a login page
def redirect_to_login(request):
    return redirect('/app/login')
