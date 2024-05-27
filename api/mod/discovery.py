import asyncio
import errno
import socket
import sys

port = 5001

_ping = b"bulbsclientping0"
_pong = b"bulbsserverpong0"


async def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setblocking(False)
    s.bind(socket.getaddrinfo("0.0.0.0", port)[0][-1])
    while True:
        try:
            resp, ip = s.recvfrom(len(_ping))
            if resp == _ping:
                s.sendto(_pong, ip)
        except OSError as e:
            if e.args[0] != errno.EAGAIN:
                raise

        await asyncio.sleep_ms(200)


def server_blocking():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(socket.getaddrinfo("0.0.0.0", port)[0][-1])
    while True:
        resp, ip = s.recvfrom(len(_ping))
        if resp == _ping:
            s.sendto(_pong, ip)


def get_bulbs(timeout=0.2):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.settimeout(timeout)
    s.bind(socket.getaddrinfo("0.0.0.0", 0)[0][-1])
    s.sendto(_ping, socket.getaddrinfo("255.255.255.255", port)[0][-1])
    bulbs = []
    while True:
        try:
            resp, ip = s.recvfrom(len(_pong))
        except TimeoutError:
            return bulbs
        if resp == _pong:
            bulbs.append(ip[0])
            # micropython's recvfrom returns address and port in format different from cpython
            # bulbs.append(".".join(str(b) for b in ip[4:8]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    if sys.argv[1] in {"client", "c"}:
        print(get_bulbs())
    elif sys.argv[1] in {"server", "s"}:
        server_blocking()
    else:
        sys.exit(1)
    sys.exit()
