# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 19:11:47 2025

@author: Pedro
"""
from classes.gclass import Gclass

class Author(Gclass):

    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    att = ['_id', '_authors_name', '_nationality', '_birth_year', '_royalty_percentage']
    des = ['Id', 'Name', 'Nationality', 'Birth Year', 'Royalty']

    def __init__(self, id, name, nationality, birth_year, royalty):
        super().__init__()
        id = Author.get_id(id)
        self._id = id
        self._authors_name = name
        self._nationality = nationality
        self._birth_year = int(birth_year)
        self._royalty_percentage = float(royalty)

        Author.obj[id] = self
        Author.lst.append(id)

    
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, value):
        self._birth_year = int(value)

    @property
    def royalty(self):
        return self._royalty

    @royalty.setter
    def royalty(self, value):
        self._royalty = float(value)
        
    
