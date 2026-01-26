from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .formulairelogin import login
# Create your views here.
@login_required
def connection(request):
    return render(request,'authentification/profile.html', {'user': request.user})

def connection(request):
    if request.method == 'POST':
        form= login(request, data=request.POST)
        if form.is_valid():
            user= authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

        if user is not None:
            login(request, user)
            return redirect('acc')
        else:
            form= login()
        return render(request,'templates/login.html',{'form': form})

def deconnection(request):
    logout(request)
    return redirect('login')