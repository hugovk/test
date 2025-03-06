import asyncio.windows_events
import socket

ip = asyncio.windows_events.IocpProactor()
sock = socket.socket(type=socket.SOCK_DGRAM)
ip.connect(sock, None)
