# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 13:01:23 2025

@author: Pedro
"""

import sqlite3
from classes.author import Author


conn = sqlite3.connect('data/Publishing.db')
cursor = conn.cursor()

if conn:
    print("Conexão bem-sucedida ao banco de dados!")
else:
    print("Falha ao conectar ao banco de dados.")


from classes.author import Author
test_class = Author
ob = '302;Dawn Nelson;Canada;1994;1.8'
db = 'data/Publishing.db'
#Uncomment to test class Product
# from classes.product import Product
# test_class = Product
# ob='Product1;10.9;100'

#Uncomment to test class Customer_login
# from classes.customer import Customer
# test_class = Customer

#Uncomment to test class Order
# from classes.customerorder import ustomerOrder
# from classes.customer import Customer
# Customer.read('data/business.db')
# test_class = Order



#Reads the test_class.csv file
test_class.read('data/Publishing.db')
op = ''
while op != 'q':
    print('')
    print('Choose one letter for select the option')
    print('---------------')
    print('l - list')
    print('b - beginning')
    print('n - next')
    print('p - previous')
    print('e - end')
    print('---------------')
    print('i - insert')
    print('m - modify')
    print('r - remove')
    print('---------------')
    print('s - sort by attribute')
    print('f - find by attribute')
    print('---------------')
    print('q - quit')
    print('---------------')
    p = test_class.current()
    print(f'\n{p}')
    op = input('?')
    if op == 'b':
        test_class.first()
    elif op == 'n':
        test_class.nextrec()
    elif op == 'p':
        test_class.previous()
    elif op == 'e':
        test_class.last()
    elif op == 'i':
        p1 = None
        if len(test_class.lst) == 0:
            p = eval('test_class.from_string("' + ob + '")')
            p1 = p
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        atype = type(getattr(p, attrib))
        print('leave blank to auto-increment')
        id = input(f'{attrib[1:]} = ')
        if id == "":
            id = 0
        else:
            id = int(id)
        strarg = f'test_class({id}'
        for i in range(1, len(str_list)):
            attrib = str_list[i]
            atype = type(getattr(p, attrib))
            if atype == datetime.date or atype == str:
                value = input(f'{attrib[1:]} = ')
                strarg += f',"{value}"'
            else:
                value = atype(input(f'{attrib[1:]} = '))
                strarg += f',{value}'
        strarg += ')'
        if p1 != None:
            # test_class.lst = list()
            test_class.remove(getattr(p, str_list[0]))
        print(strarg)
        pobj = eval(strarg)
        attrib = str_list[0]
        code = getattr(pobj, attrib)
        obj=test_class.current(code)
        test_class.insert(code)

    elif op == 'm':
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        id = input(f'Record {attrib[1:]} = ') 
        if id != "":
            id = int(id)
            obj=test_class.current(id)
            print('Leave blank or new value to modify')
            for attrib in str_list[1:]:
                # attrib = str_list[i]
                value = input(f'{attrib[1:]} = ') 
                if value != "":
                    atype = type(getattr(p, attrib))
                    if atype == datetime.date:
                        setattr(obj, attrib, datetime.date.fromisoformat(value))
                    else:
                        setattr(obj, attrib, atype(value))
        # id = getattr(obj, test_class.att[0][1:])
        test_class.update(id)
    elif op == 'r':
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        atype = type(getattr(p, attrib))
        cod = atype(input(f'{attrib[1:]} = '))
        if cod in test_class.lst:
            print(test_class.obj[cod])
            print('Confirm that you want to delete the record (y/n)?', end='')
            if input().upper() == 'Y':
                test_class.remove(cod)
    elif op == 'l':
        for code in test_class.lst:
            print(test_class.obj[code])
    elif op == 's':
        # Sort products by attribute in ascending order
        attrib = input('sort by attribute name:')
        if '_' + attrib in list(p.__dict__.keys()):
            reverse = False
            if input('Reverse (False):'):
                reverse = True
            codep = p.id         # Keep the position
            test_class.sort(attrib, reverse)
            for code in test_class.lst:
                print(test_class.obj[code])
            test_class.current(codep)
    elif op == 'f':
        # Find objects with a given value in an attribute
        attrib = input('Attribute name:')
        if '_' + attrib in list(p.__dict__.keys()):
            atype = type(getattr(p, attrib))
            value = atype(input('Value:'))
            fobjs = test_class.find(value, attrib)
            if len(fobjs) > 0:
                test_class.current(fobjs[0].id)
                for obj in fobjs:
                    print(obj)

