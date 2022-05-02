import os
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
df = pd.DataFrame()
lst = []
lst1 = []

dir = os.getcwd()


Total_assert = 0
Total_debug = 0

#table = BeautifulTable()
avoid = "test"
for path, subdirs, files in os.walk(dir):

    for filename in files:
        count = 0
        count_assert = 0
        if (filename.endswith(".py") or filename.endswith(".c")):

            if (filename.__contains__('test')==False):

                path_of_file = path + "\\" + filename
                file1 = open(path_of_file, 'r+',encoding='latin-1')
                read_line = file1.readlines()
                for line in read_line:
                            #if (line.lstrip().startswith('#') or line.lstrip().startswith('')):
                            #    continue
                    if (re.search("self[.]assert.*", line)):
                        count_assert = count_assert + 1
                    if (re.search("self[.]debug.*", line) or re.search(".*debug.*", line)):
                        count = count + 1
                        

                       
                lst.append([filename,count,path_of_file[50:]])
                lst1.append([filename,count_assert,path_of_file[50:]])

                
df = pd.DataFrame(lst,columns=['Filename','Count','Path'])
df_assert = pd.DataFrame(lst1,columns=['Filename','Count','Path'])

df.to_csv(r'count_3_debug.csv')
df_assert.to_csv(r'count_3_assert.csv')






   
            
        
            
    
        

    
            


