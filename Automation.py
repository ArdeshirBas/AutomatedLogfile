# Monthly Usage Report Automation
# Version 1.2
# Date: Jan 29
# All rights reserved

Evt_file = 'C:/Users/Wave2Wave/Desktop/Logfiles 9-4-2020/SigleMode/SM9/log/LOGEVT.log'
succ_Oper = "CONNECTION OPERATION SUCCEEDED"
fail_Oper = "CONNECTION OPERATION FAILED"
disable = "DISABLED"
MatrixA = "1AW"
str1 = ""
month = input("Enter the month: ")
counter = fCount = MA = MB = dis = 0
with open(Evt_file) as fp:
    for line in fp:
        new = line.split()
        if not line.strip():
            print("=====================================This line is Blank=====================================")
        else:
            date = str(new[2:3])
            str1 = str(date).split("/")
            if str1[1] == month:
                if succ_Oper in line:
                    if MatrixA in line:
                        MA += 1
                    else:
                        MB += 1
                    counter += 1
                elif fail_Oper in line:
                    fCount += 1
                elif disable in line:
                    dis += 1
    print("Total is = " + str(counter))
    print("Matrix A = " + str(MA))
    print("Matrix B = " + str(MB))
    print("Failed operation: " + str(fCount))
    print("Disabled port: " + str(dis))