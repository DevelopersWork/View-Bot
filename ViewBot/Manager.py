from colorama import Fore, init, Style, Back
import time
import random
import threading


class Manager:
    def __init__(self, proxy, valuesTable={}):
        self.intro = "LIVESTREAM VIEW BOT"
        self.min = 3
        self.max = 15
        self.run = False
        self.__objects = {
            "proxy": proxy
        }
        self.__resetValues(valuesTable)

        self.PARALLEL = 35

    def __resetValues(self, valuesTable={}):
        self.__values = {
            "threads": 0,
            "idle": 0,
            "active": 0,
            "success": 0,
            "proxies": 0,
            "watching": 0
        }
        self.__critical = 0

    def get(self, name):
        while self.__critical > self.PARALLEL:
            time.sleep(random.randint(0, self.min))

        if name in self.__values.keys():
            return self.__values[name]
        return ""

    def increment(self, name):
        while self.__critical > self.PARALLEL:
            time.sleep(random.randint(0, self.min))

        self.__critical += 1
        if name in self.__values.keys():
            self.__values[name] += 1
        self.__critical -= 1
    
    def setWatching(self, value):
        while self.__critical > self.PARALLEL:
            time.sleep(random.randint(0, self.min))

        self.__critical += 1
        name = 'watching'
        if name in self.__values.keys():
            self.__values[name] = value
        self.__critical -= 1

    def decrement(self, name):
        while self.__critical > self.PARALLEL:
            time.sleep(random.randint(0, self.min))

        self.__critical += 1
        if name in self.__values.keys():
            self.__values[name] -= 1
        self.__critical -= 1

    def criticalSection(self):
        while self.__critical > self.PARALLEL:
            time.sleep(random.randint(0, self.min))
        self.__critical += 1
        __result = ((self.__values["threads"] * self.PARALLEL) // 100) > self.__values["watching"]
        self.__critical -= 1
        return __result

    def print(self, printIntro = True):

        self.__values["proxies"] = self.__objects["proxy"].getProxiesCount()

        if printIntro:
            print(Fore.MAGENTA + self.intro + Style.RESET_ALL + "\n")
            print(Back.WHITE + Style.BRIGHT + Fore.LIGHTBLUE_EX +
                f" REMAKE BY Developers@Work " + Style.RESET_ALL + "\n")
        print(Fore.WHITE + f"BOTS: "+str(self.__values["threads"])+"\n")
        print(Fore.GREEN + f"ACTIVE: "+str(self.__values["active"])+"\n")
        print(Fore.YELLOW + f"IDLE: "+str(self.__values["idle"])+"\n")
        print(Fore.CYAN + f"SUCCESS: "+str(self.__values["success"])+"\n")
        print(Fore.RED + f"PROXIES: "+str(self.__values["proxies"])+"\n")
        print(Fore.BLUE + f"WATCHING: "+str(self.__values["watching"])+"\n")
        print(Style.RESET_ALL)

    def printService(self):
        while self.run:
            self.print()
            time.sleep(random.random(self.min, self.max))


"Manager"
