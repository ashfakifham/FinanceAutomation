import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

today = str(date.today())
year, month, date = today.split('-')
filename = '{}-{}'.format(month, year)

class acc_auto:
    def __init__(self,data):
        self.data = pd.read_csv(data)
        self.cat1="PURCHASE"
        plt.close("all")

    """
    Helper function to calculate the remaining balance
    """
    def balance(self):
        Balance = self.data['Amount'].sum()
        return Balance
    """
        Helper function to calculate expenses
    """
    def expenses(self):
        expenses = self.data.loc[self.data['Amount'] < 0, 'Amount'].sum()
        return expenses

    def clean(self):
        self.data.drop('Cheque#',1, inplace=True)
        self.data.drop('Date-Posted', 1, inplace=True)
        self.data.rename(columns={'Effective-Date': "Date"}, inplace=True)


    def income(self):
        income = 0
        expenses = self.data.loc[self.data['Amount'] > 0, 'Amount'].sum()
        return expenses

    def summary_exp(self):
        self.data['Info'] = ""
        new = self.data["Description"].str.split(" ", n=1, expand=True)
        self.data['Info']=new[0]
        groups = self.data.groupby("Info")['Amount'].sum()
        plt.figure(figsize=(10,20))
        figure = groups.plot(x='Info', y = 'Amount', kind = 'bar')
        for p in figure.patches:
            figure.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
        plt.savefig("Summary Of Expenses-"+ filename + ".pdf")
        plt.close("all")

    def grouped_expenses(self):
     pie_data = self.data[['Category', 'Amount']]
     pie_data.drop(pie_data[pie_data['Amount'] > 0].index, inplace=True)
     pie_data['Amount'] = pie_data['Amount'].apply(lambda x: x * -1)
     pie_data2 = pie_data.groupby("Category")['Amount'].sum()
     figure2 = pie_data2.plot.pie()
     figurename= filename
     plt.savefig("Grouped Expenses-"+ filename + ".pdf")
     plt.close()









