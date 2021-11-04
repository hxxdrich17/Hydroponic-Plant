import ModuleDHT11

class Check:

    def Check_DHT(self, stat=False):
        global min_temp, max_temp, min_humid
        dht = DHT()
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
        dht = DHT()
        temp, humid = dht.Data()
        # TODO: depends on water level, not humidity
        # if (name == "humid"):
        #     if (humid > num and humid >= min_humid):
        #         return True
        #     elif (humid <= num and humid < min_humid):
        #         return False

        if (name == "min_temp"):
            if (temp > num and temp >= min_temp):
                return True
            elif (temp <= num and temp < min_temp):
                return False

        # if (name == "max_temp"):
        #     if (temp < num and temp < max_temp):
        #         return True
        #     elif (temp >= num and temp >= max_temp):
        #         return False

    def __init__(self):
        global min_temp, max_temp, min_humid
        f = open("Settings\Config.txt", "r", encoding="UTF-8")
        param = f.readlines()
        min_temp = int(param[0].split("Minimum temperature = ")[1].split("\n")[0])
        max_temp = int(param[1].split("Maximum temperature = ")[1].split("\n")[0])
        min_humid = int(param[2].split("Minimum humidity = ")[1].split("\n")[0])
        f.close()

            
