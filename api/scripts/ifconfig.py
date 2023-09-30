import network

ap = network.WLAN(network.AP_IF)
sta = network.WLAN(network.STA_IF)

print()
print("AP")
print(f'ssid = {ap.config("essid")}, if = {ap.ifconfig()}')

print()
print("STA")
print(f'ssid = {sta.config("essid")}, status = {sta.status()}, if = {sta.ifconfig()}')

