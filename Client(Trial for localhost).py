import requests
import time
import pandas as pd

data = pd.read_excel(r"trial.xlsx")

for name,file_type,container in zip(data['DocumentUniqueID'], data['FileType'], data['ContainerName']):

    data_to_be_sent = {
        'document_name' : f'{name}',
        'application_type' : f'{file_type}',
        'container_name' : f'{container}',
        'account_key' : ' ',
        'account_name' : ' ',
        'destination_container' : ' ',
        'log_connection_string' : 'connn_string_blocks'
    }

    url = "http://127.0.0.1:5000/ocr"
    #listt1 = []
    #for i in range(2000):
        #time.sleep(1)
    response = requests.post(url, data = data_to_be_sent)

    if response.status_code == 200:
        print(response.text)
        #listt1.append(response.text)
    else:
        print(f'error ----------------------------------------> {response.status_code}')
        
    #break
        
    #break
        