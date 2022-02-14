import argparse
import os

def get_file_names(folderpath, out='output.txt'):
    with open(out, 'w') as fileObject:
        for file in os.listdir(folderpath):
            fileObject.write(file + '\n')


def get_all_file_names(folderpath, out='output.txt'):
    with open(out, 'w') as fileObject:
        for rootPath, currentDir, files in os.walk(folderpath):
            for file in files:
                fileObject.write(file + '\n')  

def print_line_one(folderpath):
    for file in os.listdir(folderpath):
        with open(file) as fileObject:
            print(fileObject.readline())

def print_emails(folderpath):
    for file in os.listdir(folderpath):
        with open(file) as fileObject:
            for line in fileObject.readlines():
                if '@' in line: print(line)

def write_headlines(folderpath, out='output.txt'):
    with open(out, 'w') as fileObj:
        for file in os.listdir(folderpath):
            if file.endswith('.md'):
                with open(file) as fileObject:
                    for line in fileObject.readlines():
                        if line.startswith('#'):
                            fileObj.write(line + '\n')
                        

if __name__ == '__main__':
    #get_file_names('/home/jovyan/my_notebook/week2', 'output.txt')
    #get_all_file_names('/home/jovyan/my_notebook/week1', 'output.txt')
    #print_line_one('/home/jovyan/my_notebook/week2/weeklyExercise')
    #print_emails('/home/jovyan/my_notebook/week2/weeklyExercise')
    write_headlines('/home/jovyan/notebooks', 'output.txt')

        