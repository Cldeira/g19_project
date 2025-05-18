# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:59:43 2025

@author: Pedro
"""

from classes.gclass import Gclass

class Awards(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    
    att = ['_awards_id', '_award_name']
    
    des = ['Id', 'Name']
    
    def __init__(self, id, name):
        super().__init__()
        
        id = Awards.get_id(id)
        self._awards_id = id
        self._award_name = name
        
        Awards.obj[id] = self 
        Awards.lst.append(id) 
    
    @property
    def id(self):
        return self._awards_id
    
    @property
    def name(self):
        return self._award_name
    
    @name.setter
    def name(self, value):
        self._name = value
