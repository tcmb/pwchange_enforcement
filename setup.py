from distutils.core import setup

setup(name='PWChange_Enforcement',
      version='0.1.0',
      description='Password change enforcement addon to django.contrib.auth',
      long_description='Simple addition to the standard django.contrib.auth password change form, enforcing that the password is actually changed.',
      author='Florian Ilgenfritz',
      author_email='flo@turchochargedmonkeybrain.net',
      license='Public Domain',
      platforms=['All'],
      url='https://github.com/tcmb/pwchange_enforcement',
      packages=['pwchange_enforcement'],
      data_files=[('pwchange_enforcement/templates/registration', ['pwchange_enforcement/templates/registration/password_change_enforcement_form.html'])]
     )