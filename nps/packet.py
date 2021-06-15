

class Packet:
    def __init__(self, ip, tcp) -> None:
        self.ip_hdr = ip
        self.tcp_hdr = tcp