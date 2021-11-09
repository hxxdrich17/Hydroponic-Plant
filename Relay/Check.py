import ModuleDHT11
import configparser


class Checks:

    def Check_DHT(self, stat=False):
        global min_temp, max_temp, min_humid
        dht = ModuleDHT11.DHT()
        temp, humid = dht.Data()

        if (temp < min_temp):
            return "min_temp", temp

        elif (temp > max_temp):
            return "max_temp", temp

        if (humid < min_humid):
            return "humid", humid

        if (stat == True):
            return temp, humid

    def Normalized(self, name, num):
        global min_temp, max_temp, min_humid
        dht = ModuleDHT11.DHT()
        temp, humid = dht.Data()
        # TODO: depends on water level, not humidity (done)

        if (name == "max_temp"):
            if (temp < num and temp < max_temp):
                return True
            elif (temp >= num and temp >= max_temp):
                return False

    def __init__(self):
        global min_temp, max_temp, min_humid
        config = configparser.RawConfigParser()
        config.read("D:\OneDrive\hxxdrich17-PC\Coding\Hydro Project\Settings\Config.conf")  # TODO: Linux path
        min_temp = config.getint("cfg", "Minimum_temperature")
        max_temp = config.getint("cfg", "Maximum_temperature")
        min_humid = config.getint("cfg", "Minimum_humidity")
