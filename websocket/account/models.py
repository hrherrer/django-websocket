from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

import qrcode
import io
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse_lazy
from websocket.settings import HOST


# Create your models here.


class QRCode(models.Model):
    user = models.ForeignKey('auth.User', verbose_name=u'Usuario')
    qr_code = models.ImageField(upload_to='qrcodes', blank=True, null=True, )

    create_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)

    def get_absolute_url(self):
        return reverse_lazy('share:qr_code', args=[self.pk])

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=25,
            border=0,
        )
        qr.add_data(str(HOST) + str(reverse_lazy('share:profile', args=[self.user.pk])))
        qr.make(fit=True)

        img = qr.make_image()

        buffer = io.BytesIO()
        img.save(buffer)

        filename = "qr-code-%s.png" % self.pk

        filebuffer = InMemoryUploadedFile(buffer, None, filename, 'image/png', buffer.__sizeof__(), None)
        self.qr_code.save(filename, filebuffer)


class Scan(models.Model):
    qr_code = models.ForeignKey('QRCode', verbose_name=u'Código QR')
    ip = models.CharField(max_length=30, verbose_name=u'Dirección Ip')
    browser = models.CharField(max_length=50, verbose_name=u'Navegador')
    os = models.CharField(max_length=50, verbose_name=u'Sistema Operativo')
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date']

    def get_create_date_as_string(self):
        return self.create_date.strftime("%b. %-d, %Y, %-H:%M %p.")


@receiver(post_save, sender=QRCode)
def post_create_qr(sender, instance, **kwargs):
    if instance.qr_code.name is None:
        print('generate qr code')
        instance.generate_qr_code()


@receiver(post_save, sender=User)
def post_create_user(sender, instance, **kwargs):
    if not instance.qrcode_set.all():
        print('create qr Object')
        qr = QRCode.objects.create(user=instance)
