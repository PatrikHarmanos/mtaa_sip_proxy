import socketserver
import time
import logging
import sipproxy

if __name__ == "__main__":
    sipproxy.HOST = input("Zadajte IP addresu: ")
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    sipproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (sipproxy.HOST, sipproxy.PORT)
    sipproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (sipproxy.HOST, sipproxy.PORT)
    server = socketserver.UDPServer((sipproxy.HOST, sipproxy.PORT), sipproxy.UDPHandler)
    server.serve_forever()
