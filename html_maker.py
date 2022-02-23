import csv

def html_maker(wildcatsync_fourm):
    
    #print()

    #with open(wildcatsync_fourm) as csvfile:
        #data = list(csv.reader(csvfile))
        #data = data[2:]
        #print(data)
       # col_names = {}
        #col_indexes = {}
        #headers = data[2]
        #headers = []
        #counter = 0
        #for i in range(len(data[0])):
           # col_names[data[0][i]]=i
           # col_indexes[i]= data[0][i]
    data = open(wildcatsync_fourm, 'r')

    #print(len(lines))
    lines = data.readlines()
    this_line = lines[4]
    #array = this_line.split(',')
    #print(array[5])
    #print(lines[3])
    email= 3

    # array = line.split(',')
    array = []
    for line in lines:
        array.append(line.split(','))


    
    for person in range(len(array)):
        print(array[person][3])

    return 0 

def field_maker(parameter):

    return 0 

def main():
    filename = "FormSubmissions.csv"
    html_maker(filename)
    return 0

if __name__ == '__main__':
    main()
