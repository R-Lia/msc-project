import EE
import extract
import json
import os


PATH_RAW_JSON="test/"
PATH_READABLE_JSON="readable/"

def create_readable_json(json_file):
    # Open the JSON file
    f = open('{}{}'.format(PATH_RAW_JSON,json_file))

    # Return the JSON object as a dictionnary
    data = json.load(f)

    inside_data = data['Transaction'][0]
    packet_string = inside_data['Packet']

    if extract.error_code != 25:
        readable = {
                'AssetId' : inside_data['AssetId'],
                'WaterSystemId' : inside_data['WaterSystemId'],
                'date' : extract.date(packet_string)[0],
                'hours' : extract.date(packet_string)[1],
                'card id' : extract.card_ID(packet_string),
                'Battery voltage (V)' : extract.voltage(packet_string),
                'usage counter': extract.usage_counter(packet_string),
                'operation' : extract.what_operation(packet_string),
                'start credit value (MITs)' : extract.start_credit_value(packet_string),
                'end credit value (MITs)' : extract.end_credit_value(packet_string),
                'liters (l)' : extract.liters(packet_string),
                'flow (l/s)' : extract.flow(packet_string) 
                }

    with open('{}{}.json'.format(PATH_READABLE_JSON, json_file), 'w', encoding='utf-8') as fi:
        json.dump(readable, fi, ensure_ascii=False, indent=4)

    # Close the file
    f.close()


# Execute the function on all the raw files that are not already in a readable form
for filename in os.listdir(PATH_RAW_JSON):
    
    # If the directory to store the readable JSON do not exist then create it
    if not os.path.exists(PATH_READABLE_JSON):
        os.makedirs(PATH_READABLE_JSON)

    if "{}.json".format(filename) not in os.listdir(PATH_READABLE_JSON):
        create_readable_json(filename)
