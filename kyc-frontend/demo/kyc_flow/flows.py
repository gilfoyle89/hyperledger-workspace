import os
from django.utils.translation import ugettext_lazy as _

from viewflow import flow, frontend, lock
from viewflow.base import this, Flow
from viewflow.flow import views as flow_views


from .models import KYCSubmitProcess


@frontend.register
class KYCFlow(Flow):
    """
    KYC Flow

    This process demonstrates KYC Case approval/rejection request flow.
    """
    process_class = KYCSubmitProcess
    process_title = _('KYC Submission')
    process_description = _('This process demonstrates KYC Submission flow.')

    lock_impl = lock.select_for_update_lock

    summary_template = _("KYC Approval for '{{process.first_name}}'")

    start = (
        flow.Start(
            flow_views.CreateProcessView,
            fields=['text','first_name','last_name','email'],
            task_title=_('New KYC Case'))
        .Permission(auto_create=True)
        .Next(this.decide)
    )

    decide = (
        flow.View(
            flow_views.UpdateProcessView, fields=['approved','rejected'],
            task_title=_('KYC Decision'),
            task_description=_("KYC Case Decision required"),
            task_result_summary=_("KYC Case was {{ process.approved|yesno:'Approved,Rejected' }}"))
        .Permission(auto_create=True)
        .Next(this.check_approve)
    )

    check_approve = (
        flow.If(
            cond=lambda act: act.process.approved,
            task_title=_('Approval check'),
        )
        .Then(this.send)
        .Else(this.end)

    )

    # assign_back = (
    #     .Assign( lambda act: act.process.created_by),
    # )

    send = (
        flow.Handler(
            this.send_hello_world_request,
            task_title=_('Send message'),
        )
        .Next(this.end)
    )

    end = flow.End(

        task_title=_('End'),

    )

    def send_hello_world_request(self, activation):
        with open(os.devnull, "w") as world:
            world.write(activation.process.first_name)
