import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



class acc_auto:
    def __init__(self,data):
        self.data = pd.read_csv(data)
        self.cat1="PURCHASE"
        plt.close("all")

    """
    Helper function to calculate the remaining balance
    """
    def balance(self):
        Balance = 0
        Balance = self.data['Amount'].sum()
        return Balance
    """
        Helper function to calculate expenses
    """
    def expenses(self):
        expenses = 0
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

    def grouping(self):
        self.data['Category'] = ""
        new = self.data["Description"].str.split(" ", n=1, expand=True)
        self.data['Category']=new[0]
        groups = self.data.groupby("Category")['Amount'].sum()
        plt.figure(figsize=(10,20))
        figure = groups.plot(x='Category', y = 'Amount', kind = 'bar')
        for p in figure.patches:
            figure.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
        plt.savefig("fig.pdf")
        plt.close("all")

    #def pie(self):
     #   groups2 = self.data.groupby("Category")['Amount'].sum()
     #   figure2 = groups2.plot.pie(y='Amount')
     #   plt.savefig("pie.pdf")
     #   plt.close()









