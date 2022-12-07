from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import standup, comments


@csrf_exempt
def Updates(request):
    latest_standup_list = standup.objects.order_by('-pub_date')[:5]
    comments_list = comments.objects.order_by('-pub_date')[:5]
    context = ({'latest_standup_list': latest_standup_list},{'comments_list': comments_list})
    return render(request, 'standup/index.html', context)

# @api_view(['GET'])
# def ApiOverview(request):
#     api_urls = {
#         'all_items': '/',
#         'Search by employee_name': '/?employee_name = name',
#         'Search by employee_id': '/?employee_id = id',
#         'Add': '/create',
#         'Update': '/update/pk',
#         'Delete': '/standup/pk/delete'
#     }
  
#     return Response(api_urls)
