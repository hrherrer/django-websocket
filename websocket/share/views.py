from django.contrib.auth.models import User
from django.views import generic
from channels import Group
from account.models import QRCode, Scan
from .services import get_client_ip

import json
import user_agents


# Create your views here.

class QRDetailView(generic.DetailView):
    model = QRCode
    template_name = 'share/qrcode_detail.html'


class UserProfileView(generic.DetailView):
    model = User
    template_name = 'share/profile_detail.html'

    def get(self, request, *args, **kwargs):
        ua = user_agents.parse(request.META['HTTP_USER_AGENT'])
        qr = self.get_object().qrcode_set.all().first()
        scan = Scan.objects.create(
            qr_code=qr,
            ip=get_client_ip(request),
            browser=ua.browser.family,
            os=ua.os.family,
        )

        send = {
            'type': 'view',
            'ip': scan.ip,
            'browser': scan.browser,
            'os': scan.os,
            'date': scan.get_create_date_as_string(),
        }
        send = json.dumps(send)

        Group('user-%s' % self.get_object().pk).send({'text': send})
        return super().get(request, *args, **kwargs)
