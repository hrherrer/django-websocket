from channels import Group
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http


@channel_session_user_from_http
def ws_connect(message):
    if message.user.pk:
        print("Connected:", message.user)
        message.reply_channel.send({"accept": True})
        Group('user-%s' % message.user.pk).add(message.reply_channel)


@channel_session_user
def ws_receive(message):
    print(message.user)


@channel_session_user
def ws_disconnect(message):
    print("Disconnected:", message.user)
    Group('user-%s' % message.user.pk).discard(message.reply_channel)
