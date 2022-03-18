
#it will open a file
log_file = open("um-server-01.txt")

#def a function to show what listed

def generate_sales_reports(log_file):
    for line in log_file:

#Remove any white spaces at the end of the string
        line = line.rstrip()

        day = line[0:3]
    
        if day == "Mon":
            print(line)


generate_sales_reports(log_file)
