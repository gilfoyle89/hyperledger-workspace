from django.db import models
from viewflow.models import Process, Task
from django.utils.translation import ugettext_lazy as _


class KYCSubmitProcess(Process):
    text = models.CharField(_('Message'), max_length=50)
    first_name = models.CharField(_('First Name'), max_length=150)
    last_name = models.CharField(_('Last Name'), max_length=150)
    email = models.CharField(_('E-Mail'), max_length=150)
    approved = models.BooleanField(_('Approve'), default=False)
    rejected = models.BooleanField(_('Reject'), default=False)

    class Meta:
        verbose_name = _("KYC Submit")
        verbose_name_plural = _('KYC Submit')
