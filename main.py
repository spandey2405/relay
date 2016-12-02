from RelayFunction import RELAY
def application(env, start_response):
    response = "LED Functions"

    if env['REQUEST_URI'] == "/1/on":
        response = RELAY(PIN="IN1", ON=True).switch
        response = "Red Led Has Turned On"

    elif env['REQUEST_URI'] == "/1/off":
        response = RELAY(PIN="IN1", OFF=True).switch
        response = "Red Led Has Turned Off"
    else:
        response = "LED Function not valid"

    start_response('200 OK', [('Content-Type', 'text/html')])
    return response