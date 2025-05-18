from zeep import Client
from zeep.transports import Transport
from zeep.wsse.username import UsernameToken

# WSDL URL of a real SOAP 1.2 API
wsdl = 'http://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL'

# Create a SOAP client
client = Client(wsdl=wsdl)

# Call the NumberToWords operation
response = client.service.NumberToWords(ubiNum=123)

print("Response from API:", response)
