from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .utils import check_list_passphrases


@csrf_exempt
@require_POST
def basic_passphrase(request):
    passphrases = request.body.decode('UTF-8').strip().split('\n')
    return JsonResponse({
        'valid_passphrase': check_list_passphrases(passphrases)
    })


@csrf_exempt
@require_POST
def advance_passphrase(request):
    passphrases = request.body.decode('UTF-8').strip().split('\n')
    return JsonResponse({
        'valid_passphrase': check_list_passphrases(passphrases, checks_anagrams=True)
    })
