import sys
from whoosh.fields import *
from whoosh.index import open_dir

class Reader:
    def __init__(self, index_path):
             self.index_path = index_path
             if not index.exists_in(self.index_path):
                    print "Not existing index"
                    sys.exit(1)
                    
    def search(self, search_word):
             ix_read = open_dir(self.index_path)
             with ix_read.searcher() as searcher:
                  query = QueryParser("content", ix_read.schema).parse(search_word)
                  results = searcher.search(query)
                  print(results[0])         
