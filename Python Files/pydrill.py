import csv
from pydriller import Repository
import sys
import collections

sys.setrecursionlimit(1000000)
author_date = {}
authors_involved = {}
freq_modified = {}
folders = ['test', 'unittest']

def datesAuthorsFrequency():
    for commit in Repository('https://github.com/python/cpython').traverse_commits():
        for modified_file in commit.modified_files:
            if folderCheck(modified_file.new_path):
                if not author_date.keys().__contains__(modified_file.filename):
                    author_date[modified_file.filename] = commit.author_date

                if authors_involved.get(modified_file.filename) is None:
                    authors_involved[modified_file.filename] = {commit.author.name}
                else:
                    authors_involved.get(modified_file.filename).add(commit.author.name)

                if freq_modified.get(modified_file.filename) is None:
                    freq_modified[modified_file.filename] = {(commit.author_date)}
                else:
                    freq_modified.get(modified_file.filename).add((commit.author_date))



def folderCheck(file_path):
    return False if file_path is None else any(element in file_path for element in folders)

datesAuthorsFrequency()
author_date = collections.OrderedDict(sorted(author_date.items()))
authors_involved = collections.OrderedDict(sorted(authors_involved.items()))
freq_modified = collections.OrderedDict(sorted(freq_modified.items()))


def fileCheck(file_name):
    return author_date.__contains__(file_name) and authors_involved.__contains__(file_name) and freq_modified.__contains__(filename)


def changeDatePattern(dates_set):
    date_filemodified = ''
    for dup_date in dates_set:
        date_filemodified += '  ' + dup_date.date().strftime("%Y-%m-%d")

    return date_filemodified


with open('tem.csv', 'w', newline = '', encoding="utf-8") as file:
    headers = ['FileName', 'Date_FileAdded', 'NumberOfAuthorsInvolved', 'Date_FileModified']
    writer = csv.DictWriter(file, fieldnames = headers)
    writer.writeheader()
    for filename in authors_involved.keys():
        if fileCheck(filename):
            date_formatted = changeDatePattern(freq_modified[filename])
            file.write("%s, %s, %d, %s\n" % (filename, author_date[filename].date(),
                                                 len(authors_involved[filename]),
                                                 date_formatted))
    file.close()