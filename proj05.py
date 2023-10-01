"""
    Project 5 
    
    Algorithm
        runs main file
            Prompt for a file
            input file 
            check if file is valid else ask again
        takes file and reads each line
            ignores all lines that the location arent in the states list
            ignores all lines that the variety isnt All GE Varieties
            creates a dictionary
        displays a sorted formated table with using the data in the dictionary
             
"""

#Use these constants to format your output table
HEADER_FORMAT = "{:<20s}{:>10s}{:>6s}{:>10s}{:>6s}" #state, max year, max value, min year, min value in this order
DATA_FORMAT = "{:<20s}{:>10s}{:>6d}{:>10s}{:>6d}"   #state, max year, max value, min year, min value in this order

STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def open_file():
    '''
    Asks for the file and holds it in "file_name"
    while file_name is not empty
    trys if it can open file_name
    if can returns the fp and breaks the loop
    else gives an error asks for another file_name and loops until a valid file_name is given or ""
    '''
    file_name = input("Enter a file: ")
    while file_name != "stop":
        try:
            fp = open(file_name)
            return fp
            break
        except:
            print("\nError in file name: {}. Please try again.".format(file_name))
            file_name = input("Enter a file: ")

def read_file(fp):
    '''
    takes a file pointer
    for each line in the file
    sets each neccicary column to a variable
    checks if the state is in states list
    checks if the variety is "All GE Varieties
    if true passes to make_dict with the pre written dictionary, state, crop, year, and value
    repeats for all remaining lines in fp
    Returns the final version of the dictionary
    '''
    fp.readline() #skips header
    GE_crops_dict = {} #created dictionary to add values to here so it is not replaced later
    for line in fp:
        line_lst = line.strip().split(',')
        state = line_lst[0]
        crop = line_lst[1]
        variety = line_lst[3]
        year = int(line_lst[4])
        value = line_lst[6]
        if state.strip().title() in STATES:
            if variety.title().strip() == "All Ge Varieties":
                GE_crops_dict = make_dict(GE_crops_dict, state, crop, year, value)
    return GE_crops_dict

def make_dict(dictt, state, crop, year, value):
    '''
    takes a dictionary, state, crop, year, value
    checks if crop is in dictionary if not adds crop, state, year, value
    if state is not in dictionary adds state, year, value to pre existing crop
    else adds year value tuple to state list
    returns the dictionary with values added
    '''
    if not crop in dictt.keys():
        dictt[crop] = {state: [(year, value)]}
    if not state in dictt[crop].keys():
        dictt[crop][state] = [(year, value)]
    else:
        dictt[crop][state].append((year, value))
    return dictt

def max_value( year_val_lst ):
    ''' 
    takes a list of tuples (year, value)
    sets max value to 0
    for each tuple in the list
    checks if value can be and interger and if it is larger then max value
    if so sets max year to year in the tuple and max value to value in the current tuple
    else passes to next value
    Returns max year and max value
    '''
    max_val = 0
    for cur_tup in year_val_lst:
        try:
            if int(cur_tup[1]) > max_val:
                max_year = cur_tup[0]
                max_val = int(cur_tup[1])
        except:
            pass
    return max_year , max_val

def min_value( year_val_lst ):
    '''
    takes a list of tuples (year, value)
    sets min value to 1000
    for each tuple in the list
    checks if value can be and interger and if it is smaler then min value
    if so sets min year to current year in the tuple and min value to value in the current tuple
    else passes to next value
    Returns min year and min value
    '''
    min_val = 1000
    for cur_tup in year_val_lst:
        try:
            if int(cur_tup[1]) < min_val:
                min_val = int(cur_tup[1])
                min_year = cur_tup[0]
        except:
            pass
    return min_year, min_val

def print_file(dictt):
    ''' 
    takes a dictionary
    prints a table
    for each crop in dictionary
    prints a header with the crop name then a formated header 
    for each state in the current crops dictionary sorted in alphabetical order
    passes through max_value to find max year and value
    passes through min value to find min year and value
    prints a formated State, max year , max value , min year, min val
    '''
    for crop in sorted(dictt.keys()):
        print("\nCrop: {}".format(crop))
        print(HEADER_FORMAT.format("State", "Max Year", "Max", "Min Year", "Min"))
        for state in sorted(dictt[crop].keys()):
            max_year , max_val = max_value(dictt[crop][state])
            min_year , min_val = min_value(dictt[crop][state])
            print(DATA_FORMAT.format(state, str(max_year), max_val, str(min_year), min_val))

    
def main():
    ''' 
    gets a file pointer using open_file()
    makes a dictionary passing the file pointer through read_file
    passes the dictionary into print file to print the data into a table
    '''
    data_file = open_file()
    dictonary = read_file(data_file)
    print_file(dictonary)
    

if __name__ == "__main__":
    main()