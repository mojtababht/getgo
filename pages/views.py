from django.shortcuts import render,redirect
from django.views.generic import TemplateView ,View,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import *
from .forms import *
from django.contrib import messages
from account.models import *
from django.urls import reverse_lazy


# Create your views here.
class HomeView(TemplateView):
    template_name = 'Home.html'

class AboutView(TemplateView):
    template_name = 'About.html'

class ContactView(TemplateView):
    template_name='Contact.html'

# class OrderView(TemplateView):
#     template_name='Order.html'

class OrderView(View):
    def get(self , request):
        reqform=RequestForm()
        pacform=PackageForm()
        addressform=AddressForm()
        return render(request,'Order.html',{'reqform':reqform,'pacform':pacform,'addressform':addressform})

    def post(self, request):
        user=request.user
        weight=request.POST.get('weight')
        slat=float(request.POST.get('slat'))
        slong=float(request.POST.get('slong'))
        dlat=float(request.POST.get('dlat'))
        dlong=float(request.POST.get('dlong'))
        price=request.POST.get('price')
        typer=request.POST.get('type')
        package=Package(weight=weight)
        package.save()
        sAddress=Address(lat=slat,long=slong)
        sAddress.save()
        dAddress=Address(lat=dlat,long=dlong)
        dAddress.save()
        req=Request(user=user,package=package,type=typer,sAddress=sAddress,dAddress=dAddress,price=price)
        req.save()
        messages.success(request,'درخواست شما با موفقیت ثبت شد')
        return redirect('home')




class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'profile.html'

#fix submit button
class ProfileInfoView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'profileInfo.html')

    def post(self,request):
        user=request.user
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.save()
        return redirect('profileInfo')


class ProfileStatusView(LoginRequiredMixin,TemplateView):
    template_name = 'profileStatus.html'


# class SignInStaffView(TemplateView):
#     template_name = 'signinStaff.html'
#

class SignInStaffView(View):
    def get(self,request):
        return render(request,'signinStaff.html')
    def post(self,request):
        phone_no=request.POST.get('phone_no')
        email=request.POST.get('email')
        nationalId=request.POST.get('nationalId')
        address=Address(formated=request.POST.get('address'))
        address.save()
        experience=request.POST.get('experience')
        avatar=request.FILES.get('avatar')
        licence=request.FILES.get('licence')
        try:
            user=CustomUser.objects.get(phone_no=phone_no)
            driverInfo=DriverInfo(email=email,nationalId=nationalId,address=address,experience=experience,avatar=avatar,licence=licence,user=user)
            driverInfo.save()
            messages.success(request,'ثبت نام با موفقیت انجام شد')
            return redirect('home')
        except:
            messages.error(request,'ابتدا باید حساب کاربری بسازید')
            return redirect('signInStaff')


#
class ProfileStaffView(UserPassesTestMixin,TemplateView):
    template_name = 'profileStaff.html'
    def test_func(self):
        return self.request.user.is_driver




class ProfileStaffStatusView(UserPassesTestMixin,TemplateView):
    template_name = 'profileStaffStatus.html'
    def test_func(self):
        return self.request.user.is_driver
        
def reqSended(request,id):
    if request.method=="POST":
        req=Request.objects.get(id=id)
        req.sended=True
        req.save()
        return redirect('profileStaffStatus')

class ProfileStaffInfoView(UserPassesTestMixin,View):
    def get(self, request):
        return render(request, 'profileStaffInfo.html')

    def post(self, request):
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        return redirect('profileInfo')

    def test_func(self):
        return self.request.user.is_driver

class ProfileStaffNewReqView(UserPassesTestMixin,TemplateView):
    template_name = 'profileStaffNewReq.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        requests=Request.objects.filter(accepted=False)
        # if self.request.GET
        context['requests']=requests
        return context

    def test_func(self):
        return self.request.user.is_driver

def reqAccept(request,id):
    if request.method=='POST':
        req=Request.objects.get(id=id)
        req.accepted=True
        req.driver=request.user
        req.save()
        return redirect('profileStaffNewReq')


    
class ProfileManagerInfo(UserPassesTestMixin,View):

    def get(self, request):
        return render(request, 'profileManagerInfo.html')

    def post(self, request):
        user = request.user
        user.phone_no=request.POST.get('phone_no')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        return redirect('profileInfo')
    
    
    def test_func(self):
        return self.request.user.is_superuser



class ProfileManagerStatus(UserPassesTestMixin,TemplateView):
    template_name='profileManagerStatus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["requests"] =Request.objects.all() 
        return context
    

    def test_func(self):
        return self.request.user.is_superuser

class ProfileManagerVol(UserPassesTestMixin,TemplateView):
    template_name='profileManagerVol.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        drinfo=DriverInfo.objects.all()
        context["drreqs"] =CustomUser.objects.filter(driverinfo__accepted=None,driverinfo__in=drinfo)
        return context

    def test_func(self):
        return self.request.user.is_superuser
    

class DetailsOfVol(UserPassesTestMixin,DetailView):
    model=DriverInfo
    template_name='detailsOfVol.html'

    def test_func(self):
        return self.request.user.is_superuser


def acceptDriver(request,id):
    if request.method=='POST':
        drinfo=DriverInfo.objects.get(id=id)
        user=drinfo.user
        drinfo.accepted=True
        user.is_driver=True
        drinfo.save()
        user.save()
    return redirect('profileManagerVol')

def denyDriver(request,id):
    if request.method=='POST':
        drinfo=DriverInfo.objects.get(id=id)
        drinfo.accepted=False
        drinfo.save()
    return redirect('profileManagerVol')