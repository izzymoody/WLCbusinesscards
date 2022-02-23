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

    lines = data.readlines()
  

    this_line = lines[4] #string for person 
    this_line = this_line.split(',') #split makes it an array 
    #print(this_line[3]) # indexing now selects field from fourm 
   
    #i was thinking if we manually write the indexes of the info we need then select 
    # it in the for loop ex email = 3 so we can say this_line[email]
    email = 3
    #this for loop works 
    for line in range(len(lines)):
        this_line = lines[line].split(',')
        for field in range(len(this_line)):
            if line >= 3:
                if field == email:
                    print(this_line[email])
            
    

    return 0 

def field_maker(parameter):

    return 0 

def main():
    filename = "FormSubmissions.csv"
    html_maker(filename)
    return 0

if __name__ == '__main__':
    main()
