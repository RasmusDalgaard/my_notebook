import csv
import argparse

def print_file_content(file):
    with open(file) as fileObject:
        reader = csv.reader(fileObject)
        for row in reader:
            print(row + '\n')

def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as fileObject:
        for element in lst:
            fileObject.write(element + '\n')

#Rewrite the function so that it gets an arbitrary number of strings instead of a list
####################
#def write_list_to_file(output_file, *arg):
    #with open(output_file, 'w') as fileObject:
        #for element in arg:
            #fileObject.write(element + '\n')

def read_csv(input_file):
    with open(input_file) as fileObject:
        reader = csv.reader(fileObject)
        list = []
        for row in reader:
            list.append(row)
        print(list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A program reads csv files")
    parser.add_argument('filepath', help='The location of the csv file')
    parser.add_argument('--file file_name', help='The file to write to')
    args=parser.parse_args()
    
    if args.file != None:
        read_csv(args.filepath)
    else:
        print_file_content(args.path)