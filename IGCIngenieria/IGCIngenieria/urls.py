"""IGCIngenieria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from formulario import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import (logout_then_login, LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView ,PasswordResetCompleteView)



# Generamos los Path para hacer las llamadas en las url segun la vista que corresponda
urlpatterns = [
    path('admin/', admin.site.urls),   
    path('formulario/',include('formulario.urls')),
    path('contacto/', include('formulario.urls')),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_then_login, name="logout"),
    
    path('', include('formulario.urls')),    
    path('oauth/', include('social_django.urls', namespace='social')),
        
    path('recuperaClave/',
        PasswordResetView.as_view(template_name='password_reset_form.html'),
        name='password_reset'),
    path('recuperaClave/done',
        PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    path('recuperaClave/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('recuperaClave/complete',
        PasswordResetDoneView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    path('api/', include('Api1.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)