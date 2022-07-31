import speedtest

test = speedtest.Speedtest()

print('Loading best server . . .')
test.get_servers()
print('Choosing best server . . .')
best = test.get_best_server()

print(f"Found: {best['host']} located in {best['country']}")

download_speed = test.download()
upload_speed = test.upload()
ping = test.results.ping

print(f"Download result: {download_speed / 1024 / 1024:.2f} Mbit/s")
print(f"Upload result: {upload_speed / 1024 / 1024:.2f} Mbit/s")
print(f"Ping result: {ping:.2f}")