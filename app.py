from speedtest import Speedtest


s = Speedtest()
server = s.get_best_server()
server_name = server['name']
server_url = server['url']

print(f"Server URL: {server_url}")
print(f"Server Location: {server_name}")

print(f"Ping: {s.results.ping} ms")
print(f"Download: {s.download()} Mbps")
print(f"Upload: {s.upload()} Mbps")



