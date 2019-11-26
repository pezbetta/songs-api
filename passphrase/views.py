from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import check_list_passphrases


@api_view(['POST'])
def basic_passphrase(request):
    passphrases = request.body.decode('UTF-8').split('\n')
    print(passphrases)
    return Response(
        {
            'valid_passphrase': check_list_passphrases(passphrases)
        }
    )


@api_view(['POST'])
def advance_passphrase(request):
    passphrases = request.body.decode('UTF-8').split('\n')
    print('advance')
    print(passphrases)
    return Response(
        {
            'valid_passphrase': check_list_passphrases(passphrases, checks_anagrams=True)
        }
    )
