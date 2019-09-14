from wifi import Cell, Scheme
import subprocess


def Search():
    wifilist = []
    cells = Cell.all('wlan0')
    for cell in cells:
        wifilist.append(cell)

    return wifilist


def setup_wifi(wifi_network: str, wifi_password: str):
    print(f"Configuring WiFi Network for: {wifi_network} with password: {wifi_password}")
    subprocess.run(f"wpa_passphrase \"{wifi_network}\" {wifi_password} > /etc/wpa_supplicant/wpa_supplicant.conf")    
    subprocess.run("wpa_cli -i wlan0 reconfigure")

#wifiNetworks = [cell.ssid for cell in Search()]