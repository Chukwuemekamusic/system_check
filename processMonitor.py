import psutil
import time

def main():
    count = 0
    while True:
        if count == 0:
            cpuUsage = psutil.cpu_percent(1,False)
            pids = psutil.pids()
            numOfProcesses = len(pids)
            print(f"CPU percentage usage: \t\t{cpuUsage}")
            print(f"Number of processes running on Computer: {numOfProcesses}")
            print()
        else: 
            cpuUsage = cpuUsage2
            numOfProcesses = numOfProcesses2
            print()

        
        time.sleep(20)

        cpuUsage2 = psutil.cpu_percent(1,False)
        numOfProcesses2 = len(psutil.pids())
        print(f"CPU percentage usage: \t\t{cpuUsage2}")
        print(f"Number of processes running on Computer: {numOfProcesses2}")

        checkProcesses(numOfProcesses, numOfProcesses2)
        checkCpu(cpuUsage, cpuUsage2)

        count += 1



def checkProcesses(process1, process2):
    if process2 > process1:
        print(f"There are {process2-process1} more processes running than before")
    elif process2 < process1:
        print(f"There are {process1-process2} less processes running than before")
    else: print("Processes are the same number")

# def checkCpu2(usage1, usage2):
#     count = 0 # we will use to check if any process is over 1%
#     if usage2 > (usage1+10):
#         for process in psutil.process_iter():
#             p = process.as_dict()
#             if p["cpu_percent"]>1:
#                 print("pid " +str(p["pid"]) +  " \tis using over 1%  " +" of the CPU at " + str(p["cpu_percent"]) +" %")
#                 count += 1
#         if count == 0:
#             print("No process is using over 1%" + " of the CPU")


def checkCpu(usage1, usage2):
    count = 0 # we will use to check if any process is over 1%
    procOverOnePercent = [] # list to store processes over 1%
    if usage2 > (usage1+10):
        for process in psutil.process_iter():
            p = process.as_dict()
            if p["cpu_percent"]>1:
                procOverOnePercent.append(p["name"])
                #print("pid " +str(p["pid"]) +  " \tis using over 1%  " +" of the CPU at " + str(p["cpu_percent"]) +" %")
                count += 1
        if procOverOnePercent:
            print("processes using over 1%:")
            for name in procOverOnePercent:
                print("\t", name)
        if count == 0:
            print("No process is using over 1%" + " of the CPU")



if __name__ == "__main__":
    main()

    