# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 16:00:04 2025

@author: Pedro
"""
from classes.gclass import Gclass
from classes.book import Books
from classes.awards import Awards

class Books_Awards(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    
    att = ['_id', '_awards_id', '_books_id', '_year']
    
    header = 'BookAwards'
    
    des = ['Id', 'Awards Id', 'Books Id', 'Year']
    
    def __init__(self, id, awards_id, books_id, year):
        super().__init__()
        
        awards_id = int(awards_id)
        books_id = int(books_id)
        
        if awards_id in Awards.lst:
            
            if books_id in Books.lst:
            
                id = Books_Awards.get_id(id)
                self._id = id
                self._awards_id = awards_id
                self._books_id = books_id
                self._year = int(year)
                
                Books_Awards.obj[id] = self
                Books_Awards.lst.append(id)
                
            
        #     else:
        #         print('Invalid Books Id')

        # else:
        #     print('Invalid Awards Id')
            
            
    
    @property
    def id(self):
        return self._id
    
    @property
    def awards_id(self):
        return self._awards_id
    
    @awards_id.setter
    def awards_id(self, value):
        if value in Awards.lst:
            self._awards_id = value
        else:
            print('Invalid Awards Id')
    
    @property
    def books_id(self):
        return self._books_id
    
    @books_id.setter
    def books_id(self, value):
        if value in Books.lst:
            self._books_id = value
        else:
            print('Invalid Books Id')
    
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = int(value)
    
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = int(value)
