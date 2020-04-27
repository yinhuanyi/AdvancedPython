# coding: utf-8
"""
@Author: Robby
@Module name: company.py
@Create date: 2020-04-27
@Function: 
"""

class Company:
    def __init__(self, employee: list):
        self.employee = employee

    def __str__(self):
        return ','.join(self.employee)

    __repr__ = __str__

company = Company(['Robby', 'Merry'])
company
print(company)
