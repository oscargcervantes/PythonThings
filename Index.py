#!/usr/bin/env python
import os
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.index import open_dir
#from whoosh.qparser import QueryParser

#Parameters:
#index_path="/home/oscargcervantes/Desktop"
#schema = Schema(title=TEXT(stored=True), path=ID(unique=True), content=TEXT)

class Index:
     def __init__(self, index_path):
             self.index_path = index_path
             self.schema = Schema(title=TEXT(stored=True), path=ID(unique=True), content=TEXT(stored=True))
             if not os.path.exists(index_path):
                    os.mkdir(index_path)

     def create_index(self):
             ix = create_in(self.index_path, self.schema)
     
     def add_index(self, title, path, content):
             add_index = open_dir(self.index_path)        
             writer = add_index.writer()
             writer.add_document(title=u"First document", path=u"/a", content=u"This is the first document we've added!")
             writer.commit()
     
     def update_index(self, title, path, content):
             # Because "path" is marked as unique, calling update_document with path="/a"
             # will delete any existing documents where the "path" field contains "/a".
             update_index = open_dir(self.index_path)        
             writer = update_index.writer()
             writer.update_document(path=u"/a", content="Replacement for the first document")
             writer.commit()
     
     def delete_index(self,title, path, content):
             delete_index = open_dir(self.index_path)
             # Delete document by its path -- this field must be indexed
             delete_index.delete_by_term('path', u'/a/b/c')
             # Save the deletion to disk
             delete_index.commit()                   

