def baseRequestData(request):
    if request.headers.get('Content-Type') == 'application/json':
        data = request.get_json()
    else:
        data = request.form
    return data