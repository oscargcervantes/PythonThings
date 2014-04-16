import os

class Dir_Reader:
    def __init__(self, path):
        self.path = path

    def read(self):
        files_found = ''
        for dirname, dirnames, filenames in os.walk('/home/oscargcervantes/Issues_Servers'):
             # print path to all subdirectories first.
             #for subdirname in dirnames:
              #    print os.path.join(dirname, subdirname)

             # print path to all filenames.
             for filename in filenames:
                  files_found += os.path.join(dirname, filename) + "\n"
                  #print os.path.join(dirname, filename)
             
             if '.git' in dirnames:
                  # don't go into any .git directories.
                  dirnames.remove('.git')
        
        return files_found
