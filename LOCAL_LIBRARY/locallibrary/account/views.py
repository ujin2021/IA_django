from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user) # 가입한 유저로 로그인해준다.
        return redirect('index')

    else: 
        form = SignUpForm # 초기 signupform을 제공해줘서 다시 작성하게 해준다.
    return render(request, 'signup.html', {'form' : form})