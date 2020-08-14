    #!/usr/bin/python

import csv
import sys
import webbrowser

### Open database file ###
with open(sys.argv[1]) as csv_list:
    csv_list_opened = csv.reader(csv_list)

    ### parse through rows of data to find expired passwords ###
    for row in csv_list_opened:
        file_row = []                                   #create blank list to load csv file row
        file_row = row                                  #add row from csv_file_opened to file_row
        number_of_days_string = file_row[2].split()[0]
        number_of_days_int = int(number_of_days_string)
        
        if number_of_days_int < 20:
            recipient = file_row[0] + "@knockinc.com"
            subject = 'Password Expires in ' + number_of_days_string
            subject = subject.replace(' ', '%20')
            body = "this is the body of the e-mail. You have " + number_of_days_string + " do so now or face certain death."
            body = body.replace(' ', '%20')
            webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body, new=1)

            # print(recipient)
            # print(subject)
