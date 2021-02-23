# kanji-cors-heroku

# API ROUTER 

I buit this light application to enable my frontend React app to make API requests and bypass CORS restrictions. Thought building this out in Django and Python would be a nice challenge.<br/>

This is my automated path in home directory. Passing down "<kanji_id"> at the end of the url as a changing variable that will be built into the end of my React API request.
```py
path('api/<kanji_id>', views.kanji_request, name='kanji_request')
```

This is the automated API request from my views.py

```py
def kanji_request(request, kanji_id):
    response = requests.get(f'http://beta.jisho.org/api/v1/search/words?keyword={kanji_id}')
    kanji = response.json()
    return JsonResponse(kanji["data"], safe=False)
```

To remove CORS restrictions please add this line at the end of your settings file

```py
CORS_ORIGIN_ALLOW_ALL = True 
```
