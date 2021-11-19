from roundoff.models import Transactions, UserSettings
from datetime import datetime, timedelta, date
import random


def past_transactions(since_date, user_id, no_of_transactions=20):

    try:
        records = UserSettings.objects.get(user_id=user_id)
    except UserSettings.DoesNotExist:
        return {"comment": "given user_id does not exist"}

    received_date = datetime.strptime(since_date, "%Y-%m-%d").date()
    date_of_first_transaction = get_first_date_of_transaction(user_id)
    date_limit = date_of_first_transaction - timedelta(days=1)
    count_of_transactions = 0
    transactions_list = list()

    if received_date < date_of_first_transaction:
        return {"comment": "No transactions are found previous to this date"}

    if records_present:
        while count_of_transactions < no_of_transactions and received_date > date_limit:
            records = Transactions.objects.filter(transaction_date=received_date, user_id_id=user_id).values()
            transactions_list.extend(records)
            count_of_transactions += len(records)
            received_date -= timedelta(days=1)

        final_transaction_list = []
        for record in transactions_list:
            transaction_date_obj = record["transaction_date"]
            transaction_date_str = transaction_date_obj.strftime("%Y-%m-%d")
            merchant_name = record["merchant_name"]
            transaction_money = record["transaction_money"]
            rounded_amount = round_off_calculation(transaction_money, user_id)

            final_transaction_list.append({"transaction_date": transaction_date_str, "merchant_name": merchant_name,
                                           "transaction_money": transaction_money, "rounded_amount": rounded_amount})

        return {"count_of_transactions": count_of_transactions, "transactions_history": final_transaction_list}
    else:
        return count_of_transactions, {"comment": "No Transactions found previous to this date"}


def round_off_calculation(transaction_money, user_id):

    user_round_off = UserSettings.objects.get(user_id=user_id)
    user_roundup = user_round_off.round_up
    user_multiplier = user_round_off.multiplier
    roundoff_amount = (user_roundup * round(transaction_money / user_roundup)) * user_multiplier

    return int(roundoff_amount)


def records_present(received_date, user_id):
    records = Transactions.objects.filter(transaction_date=received_date, user_id_id=user_id).values()
    if len(records) != 0:
        return True


def get_first_date_of_transaction(user_id):
    records = Transactions.objects.filter(user_id_id=user_id).order_by('-id')[0]
    record_date = records.transaction_date
    return record_date


# def populating_dummy_data_in_db():
#     user_id = int(1002)
#     transaction_date = "2021/11/13"
#     received_datetime = datetime.strptime(transaction_date, '%Y/%m/%d')
#     my_date_obj = received_datetime.date()
#
#     for count in range(9):
#         merchant_number = random.randint(1, 10)
#         merchant_name = "merchant_" + str(merchant_number)
#         transaction_money = random.randint(1, 1000)
#         record = Transactions.objects.create(user_id=user_id,
#                                              transaction_date=my_date_obj,
#                                              merchant_name=merchant_name,
#                                              transaction_money=transaction_money)
#         record.save()

