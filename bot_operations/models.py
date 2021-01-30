from django.db import models


from django.db import models
from django.utils import timezone


class ChatBotRequest(models.Model):
    uuid = models.CharField(max_length=36, unique=True)
    transId = models.CharField(max_length=50, default='')
    operation = models.CharField(max_length=12, default='')
    status = models.CharField(max_length=50, default='')
    msisdn = models.CharField(max_length=50, default='')
    level = models.IntegerField(default=0)
    lang = models.CharField(max_length=12, default='FR')

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    department = models.CharField(max_length=50, default='')
    day = models.CharField(max_length=50, default='')
    hour = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=150, default='')
    gender = models.CharField(max_length=20, default='')
    medical_background = models.CharField(max_length=150, default='')
    ache_zone = models.CharField(max_length=150, default='')
    symptoms = models.CharField(max_length=150, default='')

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