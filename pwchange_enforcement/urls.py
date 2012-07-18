from django.conf.urls import patterns, include, url
from pwchange_enforcement.forms import PasswordChangeEnforcementForm

urlpatterns = patterns('',
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', 
                                {'template_name':'registration/password_change_enforcement_form.html',
                                 'password_change_form': PasswordChangeEnforcementForm
                                 },
                                name='password_change_enforcement'),
)
