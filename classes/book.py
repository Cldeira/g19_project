# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:48:58 2025

@author: Pedro
"""
from classes.gclass import Gclass

class Books(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    
    att = ['_books_id', '_books_title', '_genre', '_publication_year']
    
    des = ['Id', 'Title', 'Genre', 'Publication Year']
    
    def __init__(self, id, title, genre, publication_year):
        super().__init__()
        
        id = Books.get_id(id)
        self._books_id = id
        self._books_title = title
        self._genre = genre
        self._publication_year = int(publication_year)
        
        Books.obj[id] = self 
        Books.lst.append(id) 
    
    @property
    def id(self):
        return self._books_id
    
    @property
    def title(self):
        return self._books_title
    
    @title.setter
    def title(self, value):
        self._books_title = value
    
    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, value):
        self._genre = value
    
    @property
    def publication_year(self):
        return self._publication_year
    
    @publication_year.setter
    def publication_year(self, value):
        self._publication_year = int(value)
        
        

