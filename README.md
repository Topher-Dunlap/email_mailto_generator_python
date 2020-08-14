# email_mailto_generator_python

You can use this by opening terminal and changing to the directory with this file or executing this script using the direct path
There will also need to be a CSV file in the same folder or path to said csv file. I have named the csv file list.csv.

The data in the csv will need to be formated as follows: 
`
user.name	2018.09.20	20 days remaining
user.name	2018.08.26	45 days remaining
user.name	2019.10.04	102 days remaining
user.name	2020.10.04	-2 days remaining
`

Each iteration of `user.name	YYYY.MM.DD	# days remaining` will need to have its own row.

If in directory and if csv is in the same directory this can be executed using the following command. `python script.py list.csv`
