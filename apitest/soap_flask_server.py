from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/soap', methods=['POST'])
def soap_service():
    # Get the incoming SOAP request
    xml_request = request.data.decode('utf-8')
    print("🔹 SOAP Request Received:\n", xml_request)

    # Extract value from request (optional: parse XML properly if needed)
    # For now, just simulate a static SOAP 1.2 response
    soap_response = """<?xml version="1.0" encoding="UTF-8"?>
    <soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <NumberToWordsResponse xmlns="http://example.com/soap">
          <NumberToWordsResult>One Hundred Twenty Three</NumberToWordsResult>
        </NumberToWordsResponse>
      </soap12:Body>
    </soap12:Envelope>"""

    return Response(soap_response, mimetype='application/soap+xml')

if __name__ == '__main__':
    print("🟢 SOAP 1.2 Server running on http://localhost:5000/soap")
    app.run(debug=True)
