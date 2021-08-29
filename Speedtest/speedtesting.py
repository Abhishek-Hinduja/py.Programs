import speedtest

wifi = speedtest.Speedtest()
print('Wifi download speed is ', wifi.download())
print('Wifi Upload speed is ', wifi.upload())