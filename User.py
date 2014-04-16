import os
import pwd

class User:
    def __init__(self, number_id):
        self.user_id = number_id
        
    def name(self):
        return pwd.getpwuid(os.getuid()).pw_name
    
    def home(self):
        return pwd.getpwuid(os.getuid()).pw_home
    
    
