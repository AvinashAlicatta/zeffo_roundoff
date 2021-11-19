from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from roundoff.controller.user_history_contr import past_transactions


@csrf_exempt
@api_view(['GET'])
def transaction_history(request):
    user_id = request.data["user_id"]
    since_date = request.data["since_date"]
    total_transactions = past_transactions(since_date, user_id)

    return JsonResponse(total_transactions, safe=False, status=200)
