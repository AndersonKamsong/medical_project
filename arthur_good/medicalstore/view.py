from django.http import JsonResponse
import json

def debug_headers(request):
    headers = {}
    for key, value in request.META.items():
        if key.startswith('HTTP_') or key in ['REMOTE_ADDR', 'SERVER_NAME', 'SERVER_PORT']:
            headers[key] = value
    return JsonResponse({
        'received_host': request.META.get('HTTP_HOST', 'NOT_SET'),
        'all_headers': headers
    })