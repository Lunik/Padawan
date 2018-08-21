from dnslib import QTYPE, RCODE
from dnslib import NS, SOA, TXT, PTR

from .record import Record
from .config import Config

CONFIG = Config()

class Resolver:
    def __init__(self):
        self.zones = {}

    def resolve(self, request, handler):
        reply = request.reply()

        if request.q.qtype == QTYPE.PTR and CONFIG.ipv6_subnet in str(request.q.qname):
            for record in CONFIG.records['ok']:
                reply.add_answer(record.as_rr(request.q.qname))

            ipv6_digits = str(request.q.qname).replace(CONFIG.ipv6_subnet, '').replace('.', '')[::-1]
            code = CONFIG.record_pattern.replace(CONFIG.DIGIT_TAG, ipv6_digits)
            reply.add_answer(Record(PTR, code).as_rr(request.q.qname))
        else:
            reply.header.rcode = getattr(RCODE, 'NXDOMAIN')
            for record in CONFIG.records['ko']:
                reply.add_answer(record.as_rr(request.q.qname))

        return reply
