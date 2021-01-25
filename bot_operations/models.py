from django.db import models


from django.db import models
from django.utils import timezone


class ChatBotRequest(models.Model):
    uuid = models.CharField(max_length=36, unique=True)
    transId = models.CharField(max_length=50, default='')
    operation = models.CharField(max_length=12, default='')

    # New 3 fields
    is_active = models.BooleanField(default=False)
    change_credentials = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    lang = models.CharField(max_length=12, default='FR')
    ussd_code = models.CharField(max_length=4, default='')

    status = models.CharField(max_length=50, default='')
    msisdn = models.CharField(max_length=50, default='')
    expeditor_name = models.CharField(max_length=200, default='')
    destinator_name = models.CharField(max_length=200, default='')
    destination_number = models.CharField(max_length=12, default='')
    transaction_code = models.CharField(max_length=12, default='')
    bundle_code = models.CharField(max_length=6, null=True, blank=True)
    bundle_category = models.CharField(max_length=6, null=True, blank=True)
    invoice_number = models.CharField(max_length=15, null=True, blank=True)
    contract_number = models.CharField(max_length=15, null=True, blank=True)
    phone_list = models.CharField(max_length=250, default='')
    amount = models.IntegerField(default=0)
    fees = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    destinator_full_name = models.CharField(max_length=12, default='')
    # For tracking airtimes operations
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    menu_step_name = models.CharField(max_length=50, default='')
    menu_step = models.CharField(max_length=50, default='')
    status = models.CharField(max_length=50, default='')
    start_session_time = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    end_session_time = models.DateTimeField(null=True, editable=False, blank=True)
    # TODO find a way to change status automatically after 1 minute of inactivity

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.status = 'open'
            self.start_session_time = timezone.now()
            self.end_session_time = (self.start_session_time + timezone.timedelta(seconds=7))
        self.update_at = timezone.now()
        self.end_session_time = (self.start_session_time + timezone.timedelta(seconds=7))
        return super(ChatBotRequest, self).save(*args, **kwargs)

    def __str__(self):
        return self.uuid