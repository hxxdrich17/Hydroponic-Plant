from Relay import Setup
from Relay import Check
import datetime
import time
import configparser

config = configparser.RawConfigParser()
config.read("D:\OneDrive\hxxdrich17-PC\Coding\Hydro Project\Settings\Config.conf")  # TODO: Linux path
sec = config.getint("cfg", "Seconds_for_filling")

ck = Check.Checks()

RELAY = Setup.Relay(12, False)  # TODO: Single pump, not all (done)
RELAY1 = Setup.Relay(13, False)  # TODO: Initialize pin of cooler

class Relay:

    def Logs(self, id, num):
        date = str(datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S"))
        f = open("Logs\Logs.txt", "a", encoding="UTF-8")
        if (id == 1):
            f.write(f"[{date}] Заливка воды {sec} секунд. Причина: {num}% влажности.")
        if (id == 2):
            f.write(f"[{date}] Включение кулера для охлаждения. Причина: температура {num}°C.")
        f.close()

    def WaterPlant(self, relay, num):
        # TODO: id of relay (done)
        relay.on()
        time.sleep(sec)
        relay.off()
        Relay.Logs(1, num)

    def Cooler(self, relay, num):
        relay.on()
        while (ck.Normalized("max_temp", num) == False):
            pass
        relay.off()
        Relay.Logs(2, num)

    def Main(self):
        check, num = ck.Check_DHT()
        if (check == "humid"):
            Relay.WaterPlant(1, RELAY, num)
        if (check == "max_temp"):
            Relay.Cooler(1, RELAY1, num)
        # TODO: Temperature and level of water (done)

    def __init__(self):
        while True:
            time.sleep(1)
            Relay.Main(1)
