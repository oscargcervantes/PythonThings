#!/usr/bin/env python
from PyPDF2 import PdfFileWriter, PdfFileReader
import magic
#import PyPDF2

class PDF:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
    
    def read(self):
        input1 = PdfFileReader(open(self.pdf_path, "rb"))
        pages = input1.getNumPages()
        #Implement for to read pdf pages
        #Iterate pages
        content = ''
        for i in range(0, input1.getNumPages()):
            #Extract text from page and add to content
            content += input1.getPage(i).extractText() #+ "/n"
            #content = input1.getPage(i).extractText()
            #Collapse whitespace
            content = " ".join(content.replace(u"/xa0", " ").strip().split())
        return content
        
    def write(self):
        print "write"
       
    def check(self):
        answer = magic.from_file(self.pdf_path)
        return answer
        
#output = PdfFileWriter()

    
