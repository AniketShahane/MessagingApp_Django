from django.db import models
from datetime import datetime
# Create your models here.
class message(models.Model):
    # We will have 4 store, who sent the msg, who was it sent to, time, message itself
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    body = models.TextField()
    time = models.DateTimeField(default=datetime.now())

    def shorterBody(self):
        if len(self.body) >= 20:
            return self.body[:20]+'...'
        else:
            return self.body

    def prettyTime(self):
        return self.time.strftime('%X')
