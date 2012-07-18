PASSWORD CHANGE ENFORCEMENT
===========================

Thank you for trying out this most useful and sensible django package. 

It's sole purpose is to add the behaviour of enforcing a change of password to
the password_change view of the django.contrib.auth package.

(This means that having django.contrib.auth in your INSTALLED_APPS is a requirement for using this.) 


Installation
------------
1. Put the package somewhere on your PYTHONPATH.
2. Include the pwchange_enforcement's urls into your urlconf. Make sure they
come BEFORE the auth package's urls in your urlconf.

Example:

urlpatterns = patterns('',
    
     url(r'^accounts/', include('pwchange_enforcement.urls')),
     url(r'^accounts/', include('django.contrib.auth.urls')),
)


3. Include the template directory from pwchange_enforcement in your TEMPLATE_DIRS setting.

That's it!


FEEDBACK
--------

Whether you like this little package or not, feedback is appreciated at flo@turbochargedmonkeybrain.net


LICENSE
-------

This package is released into the public domain. Spread it, or don't. ;)