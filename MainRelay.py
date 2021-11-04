from Relay import Setup
from Relay import Check
import time

f = open("Settings\Config.txt", "r", encoding="UTF-8")
sec = int(f.readlines()[3].split("Seconds for filling = ")[1].split("\n")[0])
f.close()
RELAY = Setup.Relay(12, False)

class Relay:

    def Logs(self):
        f = open("Logs\Logs.txt", "a", encoding="UTF-8")
        # TODO: Logs
        f.close()

    def WaterPlant(self, relay):
        # TODO: id of relay
        relay.on()
        # while (ck.Normalized("humid", num) == False):
        #     pass
        time.sleep(sec)
        relay.off()

    def Cooler(self):
        # TODO: Cooler
        pass

    def Main(self):
        # time_keeper = TK.TimeKeeper(TK.TimeKeeper.get_current_time())
        # if (time_keeper.current_time == WATERING_TIME):
        #     WaterPlant(RELAY, SECONDS_TO_WATER)
        #     time_keeper.set_time_last_watered(TK.TimeKeeper.get_current_time())
        #     print("\nPlant was last watered at {}".format(time_keeper.time_last_watered))
        ck = Check()
        check, num = ck.Check_DHT()
        if (check == "humid"):
            Relay.WaterPlant(RELAY)
        # TODO: Temperature and level of water

    while True:
        time.sleep(1)
        main()