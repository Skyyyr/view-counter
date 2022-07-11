import random

from django.shortcuts import render


users = {}


def home(request):
    user_id = request.COOKIES.get('user_id')
    user = users.get(user_id)

    if not user:
        user_id = str(random.randint(1000, 9999))

        users[user_id] = {
            'visit_count': 1
        }
    else:
        users[user_id]['visit_count'] += 1

    response = render(request, 'pages/index.html', users[user_id])
    response.set_cookie('user_id', user_id)

    return response
