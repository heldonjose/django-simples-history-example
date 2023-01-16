from django.utils.translation import gettext as _


class CourseStatusChoices(object):
    STATUS_DRAFT = 'draft'
    STATUS_ACTIVE = 'active'
    STATUS_FINISHED = 'finished'
    STATUS = (
        (STATUS_DRAFT, _('Rascunho')),
        (STATUS_ACTIVE, _('Ativo')),
        (STATUS_FINISHED, _('Finalizado')),

    )
