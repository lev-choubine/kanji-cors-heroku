from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def kanji_request(request, kanji_id):
    response = requests.get(f'http://beta.jisho.org/api/v1/search/words?keyword={kanji_id}')
    kanji = response.json()
    return JsonResponse(kanji["data"], safe=False)