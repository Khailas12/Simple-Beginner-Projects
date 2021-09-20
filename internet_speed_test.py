import speedtest


test = speedtest.Speedtest()

print('Loading server list..')
test.get_servers()

print('Opting a server')
best_server = test.get_best_server()

print(f"\nFound: {best_server['host']} Loacted in {best_server['country']}")


print('\nDownload test in progress...')
download_result = test.download()

print('\nUpload test in progress')
upload_result = test.upload()

ping_result = test.results.ping


print(f"\nDownload Speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"\nUpload Speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"\nPing Result: {download_result:.2f} ms")