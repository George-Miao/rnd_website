"""rnd_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import board_profiles_view, member_directory_view, individual_profile_view, UpdateProfile

app_name = 'Profiles'
urlpatterns = [
    path("board/", board_profiles_view, name="board_view"),
    path("", member_directory_view, name="member_directory_view"),
    path("<user>/", individual_profile_view, name="memberProfile"),
    path("<user>/edit", UpdateProfile.as_view(), name="edit_profile")
    # path("",user_entry_view,name="entry_view"),
    # path("register/",UserCreateView.as_view(),name="user_create_view"),
    # path("login/",UserLoginView.as_view(),name="login"),
    # path("memberhome",user_landing_view,name="authenticated_homepage")
    # #path("login/",User)
    #path('',user_profile_detail_view,name="user_profile"),
    #path('home/',home_view,name="home"),
    # path('',user_list_dynamic_link,name='user_link'),
    # path('<int:id>/',user_profile_dynamic_view,name="user_dynamic"), ## can use diff types than int
    # path('<int:id>/delete/',user_profile_delete_view,name="user_delete"),
    # path('list_view/',user_list_view,name='user_list'),
]
