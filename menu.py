import psutil
import platform

def main():
    while True:
        request = menu()

        print()
        match request:
            case '1': cpuPercentUsage()
            case '2': ramUsed()
            case '3': osDetails()
            case '4': statusComputer()
            case '5': break
            case _: print("CHOOSE A NUMBER FROM THE LIST!!!")
        print()
    

def menu(): #function for the menu
    menu = (input("choose a number from the menu:\n"
    +"1. Each CPU percentage usage after 10 seconds\n"
    +"2. RAM being used in GB\n"
    +"3. Name and version of Operating System\n"
    +"4. Check whether Computer is busy or not\n"
    +"5. Exit\n\n")).strip()
    
    return menu


def cpuPercentUsage():
    #percentage usage over 10 seconds
    percentUsage = psutil.cpu_percent(10,True)
    for i in range(len(percentUsage)):
        percentUsage[i]
        print(f"CPU {i+1} usage is currently {percentUsage[i]}%")


def ramUsed():
    memoryUsage = psutil.virtual_memory()
    usedMemory = memoryUsage.used

#convert bytes to GB
    usedMemory_gb = usedMemory/pow(2,30)

    print(f"The amont of RAM currently used is {usedMemory_gb} GB")


def osDetails(): #need to check if it works same way in Linux or MACOS
    print("Name of OS: " + platform.system())
    print("Version of OS: " + platform.version())


def statusComputer():
    cpuUsage = psutil.cpu_percent(1,False)
    ramUsage = psutil.virtual_memory().percent
    print(ramUsage)
    if cpuUsage >50 and ramUsage>50:
        print("Computer is currently busy")
    else: print("Computer is not busy")
    
def exit():
    exit





main()

