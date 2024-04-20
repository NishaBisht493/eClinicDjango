from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name = "home"),
    path('contactus/', views.contactus, name = "contactus"),
    # path('aboutus/', views.aboutus, name = "aboutus"),
    path('error404/', views.errorpage, name = "errorpage"),
    path('blog-details/', views.blog_details, name = "blog"),
    path('portfolio_details/', views.portfolio_details, name = "portfolio"),
    path('doctors/', views.doctors_details, name = "doctors"),
    path('login/', views.login_page, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('signup/', views.signup_page, name = "signup"),
    path('appointment/', views.appointment, name = "appointment"),
]
handler404 = "eclinic_app.views.handler404"
