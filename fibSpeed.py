import time
import xlsxwriter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibbonacci2(n):
    fibNumbers = [0,1]
    for i in range(2,n+1):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    return fibNumbers[n]


def timing(n):
    startTime1 = time.time()
    fib(n)
    endTime1 = time.time() - startTime1

    startTime2 = time.time()
    fibbonacci2(n)
    endTime2 = time.time() - startTime2

    return [endTime1, endTime2]

def compareFibs(testVal):
    times = []
    for fibVal in range(7): # Tests from 5 -> 35
        testTimes = []
        for test in range(testVal): # Number of tests you want to run for an average
            testNum = (fibVal+1)*5 # Works out the number of fib you want 5-> 35
            testTimes.append(timing(testNum)) # [time1, time2, time3]
            timeFib = [0, 0] # Holds times for each function
            for i in range(len(testTimes)): # Each function
                for x in range(len(testTimes[i])): 
                    timeFib[x] += testTimes[i][x] # Adds the time each time to it
        times.append([timeFib[0]/testVal, timeFib[1]/testVal]) # Works out an average
    return times # Returns all the times

def saveFibToxlsx(timeData):
    fileLocation = "/home/minimech/Documents/FibTimes.xlsx"
    workbook = xlsxwriter.Workbook(fileLocation)
    worksheet = workbook.add_worksheet("TimingTableSheet")

    row = 0
    col = 1

    worksheet.write(0,0, " ")
    worksheet.write(1,0, "Fib1: ")
    worksheet.write(2,0, "Fib2: ")

    for i in range(len(timeData)):
        worksheet.write(row, col, (i+1)*5)
        col += 1
    
    row = 1
    col = 1

    for i in range(len(timeData)):
        for x in range(len(timeData[i])):
            worksheet.write(row+x, col, timeData[i][x])
        col += 1

    workbook.close()

    df = pd.read_excel(fileLocation)
    print(df)

def plot(timeData):
    xpoints = np.array([5,10,15,20,25,30,35])
    ypoints = [np.array([]), np.array([])]

    for x in range(len(timeData)):
        for i in range(len(timeData[x])):
            ypoints[i % 2] = np.append(ypoints[i % 2], [timeData[x][i]])

    plt.subplot(1, 3, 1)

    plt.plot(xpoints, ypoints[0], 'r')
    plt.plot(xpoints, ypoints[1], 'g')

    plt.title("Functions combined")
    plt.ylabel("Time taken")
    plt.xlabel("Nth Term")

    plt.subplot(1,3,2)
    plt.plot(xpoints, ypoints[0], 'r')

    plt.title("Function fib")
    plt.ylabel("Time taken")
    plt.xlabel("Nth Term")

    plt.subplot(1,3,3)
    plt.plot(xpoints, ypoints[1], 'g')

    plt.title("Function fibonacci2")
    plt.ylabel("Time taken")
    plt.xlabel("Nth Term")

    plt.suptitle("Time taken to find nth term of fibbonacci")
    plt.show()

def menu():
    menuInput = ""
    while menuInput != "q":
        menuInput = input("What would you like to do: \n1.) Draw table\n2.) Draw a graph\n3.) Draw graph and table\nOr enter 'Q' to quit\n==> ")
        menuInput = menuInput.lower()
        if menuInput != "q":
            if menuInput == "1" or menuInput == "2" or menuInput == "3":
                while True:
                    try:
                        testValue = int(input("How many times would you like it to be tested: "))
                        break
                    except:
                        print("Pleae enter an integer")
                times = compareFibs(testValue)
                if menuInput == "1":
                    saveFibToxlsx(times)
                elif menuInput ==  "2":
                    plot(times)
                elif menuInput == "3":
                    saveFibToxlsx(times)
                    plot(times)
                print("\n")
            else:
                print("Please enter '1','2','3' or 'q'\n")

if __name__ == "__main__":
    menu()