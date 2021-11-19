# zeffo_roundoff project 

TechStack Used:
    Framework: Django = 3.2.9
    Language: Python = 3.9.6
    DB: MySql
    API: REST 
    IDE: Pycharm
    

Data in DB: Data present in the database is a prepoulated data using prepopultaing_data_in_db function from user_history_contr.py file

Database Details: Two tables namely 
                   1. UserSettings - Used to store deatils of the user such has user_id, round_up value and multipler value which will be set by the user 
                   2. Transactions - Used to store all the transactions details done by the user such has user_id, transaction_date, merchant_name, transaction_money


Users Present in DB: 
                    1. user_id  round_up  multiplier
                        1001      20        1
                        1002      50        2   
                        1003      100       5
                        
                        
All Transactions Done by Users:
                                1001: 12 transaction on 14th Nov and 10 transactions on 15th
                                1002: 8 , 5 and 7 transactions on 13th, 14th and 15th respectively
                                1003: 0 (No transactions had been done)
                                
         
REST API details: "zeffo/z0/user_transactions/history/"
Inputs Of API: user_id: integer
               since_date: date in format YYYY-M-D
               
Outputs Of API: count_of_transactions: Total number of transaction done 
                Transaction_list: transaction_date, merchant_name, transaction_money, rounded_amount
 
 
Commands To Run Project:

1. create a python virtual environment
2. pip install the requirements file given
3. run command: python manage.py runserver

