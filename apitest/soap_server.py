from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap12
from spyne.server.wsgi import WsgiApplication

class MyService(ServiceBase):
    @rpc(Integer, _returns=Unicode)
    def number_to_words(ctx, number):
        words = {
            1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 500: "Five Hundred"
        }
        return words.get(number, "Unknown")

application = Application(
    [MyService],
    tns='http://example.com/soap',
    in_protocol=Soap12(validator='lxml'),
    out_protocol=Soap12()
)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print("SOAP server running at http://127.0.0.1:8000/")
    server = make_server('127.0.0.1', 8000, WsgiApplication(application))
    server.serve_forever()
