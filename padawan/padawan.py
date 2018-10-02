from time import sleep

from dnslib.server import DNSServer

from .lib.resolver import Resolver
from .lib.config import Config

CONFIG = Config()

class Padawan:
    def __init__(self):
        resolver = Resolver()
        self.servers = [
            DNSServer(resolver, port=CONFIG.server['port'], address=CONFIG.server['address'], tcp=True),
            DNSServer(resolver, port=CONFIG.server['port'], address=CONFIG.server['address'], tcp=False),
        ]

    def start(self):
        for s in self.servers:
            s.start_thread()
        print("DNS server start on " + str(CONFIG.server['address']) + ":" + str(CONFIG.server['port']))

    def stop(self):
        for s in self.servers:
            s.stop()
        print("DNS server stop")
