from websocket.settings import HOST


def constants(request):
    return {
        'HOST': HOST,
    }
