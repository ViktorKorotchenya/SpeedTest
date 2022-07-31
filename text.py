import speedtest

speed = speedtest.Speedtest()
download_speed = speed.download()
upload_speed = speed.upload()

print(f'Скорость входящего соединения {download_speed}')
print(f'Скорость исходящего соединения {upload_speed}')