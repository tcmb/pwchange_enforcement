# coding: utf-8
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import ValidationError
from django.utils.translation import ugettext, ugettext_lazy as _

class PasswordChangeEnforcementForm(PasswordChangeForm):
    """
    A form that lets the user change his/her password and
    enforces that the new password is different from the old one. 
    """
    error_messages = dict(PasswordChangeForm.error_messages, **{
        'password_unchanged': _("Most likely you just wanted to see what happens when you enter your old password three times. Now go ahead and change it already.")
    })

    def clean(self):
        """Enforcing that new password is different from old password"""
        old_password = self.cleaned_data.get('old_password', None)
        new_password = self.cleaned_data.get('new_password2', None)
        if old_password and new_password and old_password == new_password:
            # we could update self._errors here to show the error on the 'new_password' field,
            # but as the error really applies to all fields, we raise it as a form error.
            raise ValidationError(self.error_messages['password_unchanged'])
        return self.cleaned_data
        

