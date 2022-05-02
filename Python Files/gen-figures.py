import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

## Question - 2 plots

dataset2 = pd.read_csv('CSV Files/count_assert_2_final.csv')

sort_dataset2 = dataset2.sort_values(by='Count')

sort_dataset2 = sort_dataset2

plt.figure(figsize=(16, 8), dpi=150)

plt.ylim(0, 1500,150)

#sort_dataset2.plot(x="Filename", y="Count", kind="bar")
plt.scatter(sort_dataset2['Filename'],sort_dataset2['Count'])

#plt.legend(["Count"], ncol=1, loc="upper left", bbox_to_anchor=(1,1))



ax = plt.gca()

ax.set_xlabel('Files', 
               fontweight ='bold')

ax.set_ylabel('Count', 
               fontweight ='bold')

ax.set_title('Count of Assert in Each File', 
               fontweight ='bold')



plt.xticks(x="Filename", label='')

ax.axes.xaxis.set_ticklabels([])

plt.tick_params(bottom=False)

plt.savefig('plot2_1_line.png',bbox_inches='tight')

#####################

#question -2 Total files

dataset2_2 = pd.read_csv('CSV Files/count_total_2_final.csv')
#print(dataset2_2)
plt.figure(figsize=(16, 8), dpi=150)


c=['red', 'blue', 'cyan']
dataset2_2.plot(x='Type_of_Files',
        kind='bar',
        stacked=True,
        legend=False,color = "steelblue")




#plt.bar(dataset2_2['Type_of_Files'], dataset2_2['Count'], color=['red', 'blue', 'cyan'])

plt.title("Total No of Test Files",fontweight ='bold')
plt.xlabel("Files",fontweight ='bold')
plt.ylabel("Count",fontweight ='bold')
#plt.legend(Type_of_Files)
#plt.show()
plt.savefig('plot2_total.png',bbox_inches='tight')



##########################

## question - 3 - assert


###############

dataset3_1 = pd.read_csv('CSV Files/count_3_assert.csv')

sort_dataset3_1 = dataset3_1
sort_dataset3_1.drop(sort_dataset3_1.index[sort_dataset3_1['Count'] == 0], inplace=True)



plt.figure(figsize=(16, 8), dpi=150)


#plt.scatter(sort_dataset3_1['Filename'],sort_dataset3_1['Count'],color = "green")
sort_dataset3_1.plot(x='Filename', y='Count', kind='bar')

plt.title("Count of Assert Statements in Production Files",fontweight ='bold')
plt.xlabel("Production Files",fontweight ='bold')
plt.ylabel("Count",fontweight ='bold')
 
plt.savefig('plot3_assert_bar.png',bbox_inches='tight')


# question -3 debug

dataset3_2 = pd.read_csv('CSV Files/count_3_debug.csv')

#sort_dataset3_2 = dataset3_2
sort_dataset3_2 = dataset3_2.sort_values(by='Count')
sort_dataset3_2.drop(sort_dataset3_2.index[sort_dataset3_2['Count'] == 0], inplace=True)

plt.figure(figsize=(16, 8), dpi=150)

plt.scatter(sort_dataset3_2['Filename'],sort_dataset3_2['Count'])
plt.legend(["Count"], ncol=1, loc="upper left", bbox_to_anchor=(1,1))
#sort_dataset3_2.plot(x='Filename', y='Count', kind='bar',color="green")
ax = plt.gca()

ax.set_xlabel('Production Files', 
               fontweight ='bold')

ax.set_ylabel('Count', 
               fontweight ='bold')

ax.set_title('Count of Debug Statements in Production Files', 
               fontweight ='bold')

plt.xticks(x="Filename", label='')

ax.axes.xaxis.set_ticklabels([])

plt.tick_params(bottom=False)

plt.savefig('plot3_debug_bar.png',bbox_inches='tight')


## Question - 4 Plots

dataset4 = pd.read_csv('CSV Files/files_cpython.csv')
 
dataset4['year_add'] = pd.DatetimeIndex(dataset4['DateWhenFileIsAddedToTheProject']).year
 
dataset4['month_add'] = pd.DatetimeIndex(dataset4['DateWhenFileIsAddedToTheProject']).month

plt.figure(figsize=(16, 8), dpi=150)

dataset4["contributors_year_wise"] = dataset4.groupby(["year_add"])["NumberOfAuthorsInvolved"].transform(sum)

dataset4 = dataset4.sort_values(by='year_add')

drop_duplicates = dataset4.drop_duplicates(subset=['year_add'])


drop_duplicates.plot(x='year_add', y='contributors_year_wise', kind='bar')

plt.title("Contributors Year - Wise",fontweight ='bold')
plt.xlabel("Years",fontweight ='bold')
plt.ylabel("Count",fontweight ='bold')

plt.savefig('plot4_1.png',bbox_inches='tight')



data = pd.read_csv('CSV Files/files_cpython_woauthornames.csv',  header=None)

file_added_date_number_of_modifications = {}
data = data[1:]
data = data[[1, 3]]
dict_files = data.to_dict()
years = {}

for i in dict_files[1].keys():
    if file_added_date_number_of_modifications.__contains__(dict_files[1][i].strip()[0:4]):
        years[dict_files[1][i].strip()[0:4]] += int(len(dict_files[1][i].strip()[0:4])/4)
        file_added_date_number_of_modifications[dict_files[1][i].strip()[0:4]] += len(dict_files[3][i].strip().split())

    else:
        file_added_date_number_of_modifications[dict_files[1][i].strip()[0:4]] = len(dict_files[3][i].strip().split())
        years[dict_files[1][i].strip()[0:4]] = int(len(dict_files[1][i].strip()[0:4])/4)

od = {}
for i in sorted(file_added_date_number_of_modifications.keys()):
    od[i] = file_added_date_number_of_modifications[i]


od_y = {}
for i in sorted(years.keys()):
    od_y[i] = years[i]

plt.figure(figsize=(16, 8), dpi=150)
plt.bar(range(len(od)), od.values(), tick_label = od.keys())
plt.tick_params(labelbottom=False)
plt.title("Number of files modified year wise")
plt.xlabel("Years 1990-2022")
#plt.show()
plt.savefig('plot4_2.png',bbox_inches='tight')



plt.figure(figsize=(16, 8), dpi=150)
plt.bar(range(len(od_y)), od_y.values(), tick_label = od_y.keys())
#plt.tick_params(labelbottom=False)
plt.title("Number of files added year wise")
plt.xlabel("Years 1990-2022")
plt.savefig('plot4_3.png',bbox_inches='tight')



