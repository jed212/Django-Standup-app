from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import standup, comments


@csrf_exempt
def Updates(request):
    latest_standup_list = standup.objects.order_by('-pub_date')[:5]
    comments_list = comments.objects.order_by('-pub_date')[:5]
    context = ({'latest_standup_list': latest_standup_list},{'comments_list': comments_list})
    return render(request, 'standup/index.html', context)


