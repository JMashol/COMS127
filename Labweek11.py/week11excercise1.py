#Jacob Mashol 11/2/2022
#Lab week 11

from re import A


def calcAAA(a,b,c,d):
    AAA = a+b+c+d
    return AAA

def calcAAS(a,b,c,d):
    AAS = a+b+c-d
    return AAS

def calcAAM(a,b,c,d):
    AAM = a+b+c*d
    return AAM

def calcASM(a,b,c,d):
    ASM = a+b-c*d
    return ASM

def calcAMS(a,b,c,d):
    AMS = a+b*c-d
    return AMS

def calcASS(a,b,c,d):
    ASS = a+b-c-d
    return ASS

def calcAMM(a,b,c,d):
    AMM = a+b*c*d
    return AMM

def calcAMA(a,b,c,d):
    AMA = a+b*c+d
    return AMA

def calcASA(a,b,c,d):
    ASA = a+b-c+d
    return ASA

def calcSSS(a,b,c,d):
    SSS = a-b-c-d
    return SSS

def calcSSA(a,b,c,d):
    SSA = a-b-c+d
    return SSA

def calcSSM(a,b,c,d):
    SSM = a-b-c*d
    return SSM

def calcSAM(a,b,c,d):
    SAM = a-b+c*d
    return SAM

def calcSMA(a,b,c,d):
    SMA = a-b*c+d
    return SMA

def calcSMM(a,b,c,d):
    SMM = a-b*c*d
    return SMM

def calcSAA(a,b,c,d):
    SAA = a-b+c+d
    return SAA

def calcSAS(a,b,c,d):
    SAS = a-b+c-d
    return SAS

def calcSMS(a,b,c,d):
    SMS = a-b*c-d
    return SMS

def calcMMM(a,b,c,d):
    MMM = a*b*c*d
    return MMM

def calcMMA(a,b,c,d):
    MMA = a*b*c+d
    return MMA

def calcMMS(a,b,c,d):
    MMS = a*b*c-d
    return MMS

def calcMSA(a,b,c,d):
    MSA = a*b-c+d
    return MSA

def calcMAS(a,b,c,d):
    MAS = a*b+c-d
    return MAS

def calcMAM(a,b,c,d):
    MAM = a*b+c*d
    return MAM

def calcMSM(a,b,c,d):
    MSM = a*b-c*d
    return MSM

def calcMSS(a,b,c,d):
    MSS = a*b-c-d
    return MSS

def calcMAA(a,b,c,d):
    MAA = a*b+c+d
    return MAA

def main():

    print()

    a = int(input("Input 'a': "))
    b = int(input("Input 'b': "))
    c = int(input("Input 'c': "))
    d = int(input("Input 'd': "))

    print()

    numDict = {}
    numDict["AAA"] = calcAAA(a,b,c,d)
    numDict["AAS"] = calcAAS(a,b,c,d)
    numDict["AAM"] = calcAAM(a,b,c,d)
    numDict["ASM"] = calcASM(a,b,c,d)
    numDict["AMS"] = calcAMS(a,b,c,d)
    numDict["ASS"] = calcASS(a,b,c,d)
    numDict["AMM"] = calcAMM(a,b,c,d)
    numDict["AMA"] = calcAMA(a,b,c,d)
    numDict["ASA"] = calcASA(a,b,c,d)
    numDict["SSS"] = calcSSS(a,b,c,d)
    numDict["SSA"] = calcSSA(a,b,c,d)
    numDict["SSM"] = calcSSM(a,b,c,d)
    numDict["SAM"] = calcSAM(a,b,c,d)
    numDict["SMA"] = calcSMA(a,b,c,d)
    numDict["SMM"] = calcSMM(a,b,c,d)
    numDict["SAA"] = calcSAA(a,b,c,d)
    numDict["SAS"] = calcSAS(a,b,c,d)
    numDict["SMS"] = calcSMS(a,b,c,d)
    numDict["MMM"] = calcMMM(a,b,c,d)
    numDict["MMA"] = calcMMA(a,b,c,d)
    numDict["MMS"] = calcMMS(a,b,c,d)
    numDict["MSA"] = calcMSA(a,b,c,d)
    numDict["MAS"] = calcMAS(a,b,c,d)
    numDict["MAM"] = calcMAM(a,b,c,d)
    numDict["MSM"] = calcMSM(a,b,c,d)
    numDict["MSS"] = calcMSS(a,b,c,d)
    numDict["MAA"] = calcMAA(a,b,c,d)



    for cool, mac in numDict.items():
        print(cool, mac)

if __name__ == "__main__":
    main()
