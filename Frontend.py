import Backend as bk


my_data = bk.acc_auto("acchis.csv")
my_data.clean()
my_data.summary_exp()
my_data.grouped_expenses()








