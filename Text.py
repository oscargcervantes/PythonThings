import magic
 
class Text:
   'Class intended to read text files'
   def __init__(self, path):
       self.path = path 
   
   def read(self):
       fo = open(self.path, "r")
       try:
           read_string = fo.read()
       finally:    
           fo.close()
           return read_string
       
   def check(self):
       answer = magic.from_file(self.path)
       return answer
   
   def write(self, write_string):
       fo = open(self.path, "w")
       try:
           fo.write( write_string + "\n")
       finally:
           fo.close()
