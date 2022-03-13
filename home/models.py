from django.db import models
from twilio.rest import Client
# Create your models here.


class message(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    contact = models.PositiveIntegerField()
    email = models.EmailField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.contact >= 10:
            account_sid = 'ACc704a2d7d5aa87747aeb499632ee789d'
            auth_token = '77c9d73b4434adfa26f721a37b34bf02'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Congratulations {self.name}, We  did our project succesfully SUYOG, GRISHMA, SABIN, DIPESH",
                from_='+18788796403',
                to='+977-9814327222'
            )
        print(message.sid)
        return super().save(*args, **kwargs)