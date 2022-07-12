# msc-project

## tar_file.sh
Look into a folder and tar.gz all the files inside that folder. Store the created archive in a directory. Ideally it should run automatically, like every hour perhaps. 

## EE.py
a dictionnary of the meaning of the different event code (specific to the JSON data sent by the company)

## extract.py
Extract different elements of the 39bytes JSON packet. Not all values are extracted yet. 

## generate_readable_json.py
Function to generate a readable JSON out of the raw data packet in the received JSON. Ideally it should run automatically, like every hour perhaps. 


## Data specs 
Folder with the definition of the 39bytes packet

## Test 
Folder with 2 test data : 2 raw data received via the https endpoint to test the python and shell scripts on
