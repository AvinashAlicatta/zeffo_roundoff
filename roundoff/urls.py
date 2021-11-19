from django.urls import path
from roundoff.views.users_history_view import transaction_history

urlpatterns = [
    path("zeffo/z0/user_transactions/history/", transaction_history, name="transaction_history"),
]
