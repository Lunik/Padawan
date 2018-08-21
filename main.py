from time import sleep

from dnslib.server import DNSServer

from lib.resolver import Resolver

if __name__ == '__main__':
    resolver = Resolver()
    servers = [
        DNSServer(resolver, port=5053, address='localhost', tcp=True),
        DNSServer(resolver, port=5053, address='localhost', tcp=False),
    ]

    for s in servers:
        s.start_thread()

    try:
        while 1:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        for s in servers:
            s.stop()