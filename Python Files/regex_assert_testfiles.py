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

dir = dir + "\\" + "Lib"
#print(dir)
counter_total = 0
counter_assert = 0
check = 0

#dir = dir + "\\" + "Lib\\unittest"
#print(dir)
#dir = os.chdir('/Lib/unittest')

for path, subdirs, files in os.walk(dir):
    for filename in files:
        count = 0
        if ((filename.__contains__('test')==True)):
            if (filename.endswith(".py") or filename.endswith(".c")):
                counter_total = counter_total+1
                path_of_file = path + "\\" + filename
                file1 = open(path_of_file, 'r+',encoding='latin-1')
                read_line = file1.readlines()
                for line in read_line:
                    if (re.search("self[.]assert.*", line)):
                        check = 1 
                        count = count + 1
                
                if(check == 1):
                    counter_assert += 1
                check = 0

                #print("filename", filename, "count of lines", count)
                #'BTColumnCollection.header'
                #BTColumnCollection.header = ["Filname", "Count"]
                #if(count != 0):
                lst.append([filename,count])
not_assert = counter_total - counter_assert
print("Total No of Test Files",counter_total)
print("Total No of Files containing Assert statements",counter_assert)
print("Total No of Files not containing Assert statements",(not_assert))

#lst1.append([filename,count])
lst1.append(["Total_Files",counter_total])
lst1.append(["Assert_Files",counter_assert])
lst1.append(["Not_Assert_Files",not_assert])
df1 = pd.DataFrame(lst1,columns=['Type_of_Files','Count'])
df1.to_csv(r'count_total_2_final.csv')


df = pd.DataFrame(lst,columns=['Filename','Count'])

df.to_csv(r'count_assert_2_final.csv')


#print(df)
            


