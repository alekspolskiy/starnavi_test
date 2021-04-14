import sys
import jwt
from datetime import datetime, timedelta
from authentication.models import User
from .models import UsersPostsLikes


def get_user(request):
    user_id = jwt.decode(
        request.headers.get('Authorization').split(' ')[-1],
        options={"verify_signature": False}
    ).get('user_id')
    return user_id


def update_last_request(request):
    user = User.objects.filter(id=get_user(request)).first()
    user.update_last_request()
    return sys.stdout.write('Last request datetime updated')


def count_likes(date_from, date_to):
    date_from = datetime.strptime(date_from, '%Y-%m-%d')
    date_to = datetime.strptime(date_to, '%Y-%m-%d')
    date_from, date_to = date_from.date(), date_to.date()
    likes_dates = [
        like_date.date.date() for like_date in UsersPostsLikes.objects.all()
    ]
    delta = date_to - date_from
    days = [date_from + timedelta(days=day) for day in range(delta.days+1)]
    return {
        str(day): likes_dates.count(day) for day in days
    }
