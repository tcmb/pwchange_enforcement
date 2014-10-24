PASSWORD CHANGE ENFORCEMENT
===========================

Thank you for trying out this most useful and sensible django package. 

It's sole purpose is to add the behaviour of enforcing a change of password to
the password_change view of the django.contrib.auth package.

(This means that having django.contrib.auth in your INSTALLED_APPS is a requirement for using this.) 


Installation
------------
This package is distributed using the distutils that come with python.

1. Unzip and untar the package in a suitable location:
gzip -d <package_name>
tar xf <tar_name>
2. Change into the folder that has been created
3. Execute the install script:
python setup.py install
4. Include the pwchange_enforcement's urls into your urlconf. Make sure they
come BEFORE the auth package's urls in your urlconf.

Example:

urlpatterns = patterns('',
    
     url(r'^accounts/', include('pwchange_enforcement.urls')),
     url(r'^accounts/', include('django.contrib.auth.urls')),
)


5. Include the template directory from pwchange_enforcement in your TEMPLATE_DIRS setting.
The setup script creates a template folder structure 'pwchange_enforcement/templates/registration/' and 
it will tell you where it created that.

That's it!


FEEDBACK
--------

Whether you like this little package or not, feedback is appreciated at flo@turbochargedmonkeybrain.net


LICENSE
-------

This package is released into the Public Domain. Spread it, or don't. ;)

MORE INFO
---------
This change was done on a branch that integrated directly with Pivotaltracker. w00t.

