from django.shortcuts import render , redirect
from django.http import HttpResponse,JsonResponse
from .forms import LoginForm,AddVpnForm
from django.contrib.auth.decorators import login_required


from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

from .models import VpnModel
from rest_framework.decorators import api_view
from .serializers import VpnSerializer

# Create your views here.



# login view 
def signin_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    forms = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)
        user = authenticate(username = username , password = password)
        # print(user)
        if user is not None :
            login(request , user)
            messages.info(request, 'Login Successfull')
            return redirect('dashboard')

        messages.info(request, 'Something Went Wrong Check Your Username or Password')

        
    context = {'forms':forms}
    return render(request , 'signin.html' , context)


# logout view
@login_required(login_url='signin')
def signout_view(request):
    messages.info(request, 'Logout Successfull')
    
    logout(request)
    return redirect('signin')



# dashboard view
@login_required(login_url='signin')
def dashboard_view(request):

    allvpn = VpnModel.objects.all()
    
    context = {'allvpn' : allvpn}

    return render(request , 'dashboard.html' , context)


# add vpn  view
@login_required(login_url='signin')
def addvpn_view(request):

    forms = AddVpnForm()
    if request.method == 'POST':
        forms = AddVpnForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard')
        
    context = {'forms' : forms}
    return render(request , 'addvpn.html' , context)



# update view
@login_required(login_url='signin')
def update_view(request , id ):
    vpn = VpnModel.objects.get(id = id)
    if request.method == 'POST':
        hostname = request.POST.get('hostname')
        countryshort = request.POST.get('countryshort')
        username = request.POST.get('username')
        password = request.POST.get('password')
        config = request.POST.get('config')
        is_enable = request.POST.get('is_enable')
        if is_enable == 'on':
            is_enable = True
        if is_enable == None:
            is_enable = False

        # print(is_enable)
        # print(type(is_enable))

        # model = VpnModel(hostname = hostname , countryshort = countryshort , username = username , password = password )
        # model.save()

        vpn.hostname = hostname
        vpn.countryshort = countryshort
        vpn.username = username
        vpn.password = password
        vpn.config = config
        vpn.is_enable = is_enable
        vpn.save()

        return redirect('dashboard')

    context = {'vpn':vpn}
    return render(request , 'update.html' ,context)


@login_required(login_url='signin')
def delete_view(request , id):
    VpnModel.objects.get(id = id).delete()
    messages.info(request, 'Vpn Delete Successfully')

    return redirect('dashboard')




# api view 
@api_view(['GET'])
def vpnapi_view(request):

    if request.method == 'GET':
        all_vpn = VpnModel.objects.all()

        serializer = VpnSerializer(all_vpn , many=True)

        return JsonResponse(serializer.data , content_type = 'application/json' ,safe=False)
    
    return HttpResponse('Api Page')

