
import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = data
    
    def mean(self):
        return sum(self.data) / len(self.data)
    
    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2-1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]
    
    def mode(self):
        c = Counter(self.data)
        mode_freq = max(c.values())
        return [k for k, v in c.items() if v == mode_freq]
    
    def range(self):
        return max(self.data) - min(self.data)
    
    def variance(self):
        mean = self.mean()
        return sum((x - mean)**2 for x in self.data) / (len(self.data) - 1)
    
    def standard_deviation(self):
        return math.sqrt(self.variance())
    
    def minimum(self):
        return min(self.data)
    
    def maximum(self):
        return max(self.data)
    
    def count(self):
        return len(self.data)
    
    def percentile(self, p):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        k = (n - 1) * (p / 100)
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            return sorted_data[int(k)]
        else:
            d0 = sorted_data[int(f)] * (c - k)
            d1 = sorted_data[int(c)] * (k - f)
            return d0 + d1
    
    def frequency_distribution(self):
        c = Counter(self.data)
        total = sum(c.values())
        return {k: v/total for k, v in c.items()}

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) 
print('Sum: ', data.sum()) 
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range() 
print('Mean: ', data.mean()) 
print('Median: ', data.median()) 
print('Mode: ', data.mode())
print('Standard Deviation: ', data.std()) 
print('Variance: ', data.var()) 
print('Frequency Distribution: ', data.freq_dist()) 



class PersonAccount:
    def __init__(self,firstname,lastname,incomes,expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    def total_income(self):
        self.tot_income = sum(incomes)
    def total_expenses(self):
        self.tot_expenses = sum(expenses)
    def account_info(self):
        print(f'The account name is: {self.firstname} {self.lastname}','\n')
        print(f'The total income is: {self.tot_income}')
        print(f'The total expenses is: {self.tot_expenses}')
    def add_income(self,add):
        self.incomes += add
    def add_expense(self,plus):
        self.expenses += plus
    def account_balance(self):
        return f'The current account balance is: {total_income()} - {total_expenses()}'
    
