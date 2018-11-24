from django.db import models
from datetime import datetime
# Create your models here.
now_time = datetime.now()
class message(models.Model):
    # We will have 4 store, who sent the msg, who was it sent to, time, message itself
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    body = models.TextField()
    time = models.DateTimeField(default=now_time)

    def shorterBody(self):
        if len(self.body) >= 35:
            return self.body[:35]+'...'
        else:
            return self.body

    def prettyTime(self):
        return self.time.strftime('%X')
