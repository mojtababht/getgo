from .views import *
from django.urls import  path
urlpatterns = [
    path('' , HomeView.as_view() , name='home'),
    path('about/' , AboutView.as_view() , name='about'),
    path('contact/' , ContactView.as_view() , name='contact'),
    path('order/', OrderView.as_view() , name='order'),
    path('profile/' , ProfileView.as_view() , name='profile'),
    path('profileInfo/' , ProfileInfoView.as_view() , name='profileInfo'),
    path('profileStatus/' , ProfileStatusView.as_view() , name='profileStatus'),
    path('signinStaff/' , SignInStaffView.as_view() , name='signInStaff'),
    path('profileStaff/' , ProfileStaffView.as_view() , name = 'profileStaff'),
    path('profileStaffStatus/' , ProfileStaffStatusView.as_view() , name = 'profileStaffStatus'),
    path('profileStaffInfo/' , ProfileStaffInfoView.as_view() , name = 'profileStaffInfo'),
    path('profileStaffNewReq/' , ProfileStaffNewReqView.as_view() , name = 'profileStaffNewReq'),
    path('profileManagerInfo/' , ProfileManagerInfo.as_view() , name='profileManagerInfo'),
    path('profileManagerStatus/' , ProfileManagerStatus.as_view() , name="profileManagerStatus"),
    path('profileManagerVol/' , ProfileManagerVol.as_view() , name='profileManagerVol'),
    path('detailsOfVol/<int:pk>',DetailsOfVol.as_view() , name='detailsOfVol'),
    path('reqsended/<int:id>/',reqSended,name='reqsended'),
    path('reqaccept/<int:id>/',reqAccept,name='reqaccept'),
    path('acceptdriver/<int:id>/',acceptDriver,name='acceptdriver'),
    path('denydriver/<int:id>/',denyDriver,name='denydriver'),
]