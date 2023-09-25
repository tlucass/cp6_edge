import numpy as np
import requests
import matplotlib.pyplot as plt

url = "http://46.17.108.113:8666/STH/v1/contextEntities/type/Lamp/id/urn:ngsi-ld:Lamp:001/attributes/luminosity?lastN=50"

payload = {}
headers = {
    'fiware-service': 'smart',
    'fiware-servicepath': '/'
}

response = requests.get(url, headers=headers, data=payload)

if response.status_code == 200:
    data = response.json()['contextResponses'][0]['contextElement']['attributes'][0]['values']


    luminosity_values = [entry['attrValue'] for entry in data]
    timestamps = [entry['recvTime'] for entry in data]


    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, luminosity_values, marker='o', linestyle='-')
    plt.xlabel('Tempo')
    plt.ylabel('Luminosidade')
    plt.title('Luminosidade ao longo do tempo')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
else:
    print(f"A solicitação HTTP falhou com o código de status: {response.status_code}")