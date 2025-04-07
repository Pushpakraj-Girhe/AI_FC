lm=3
lc=3
rm=0
rc=0
while True:
    if(rm==3 and rc==3):
        print("Win....!")
        break
    elif (lc > lm and lm > 0)or (rc > rm and rm > 0):
        print("Cannible eats Missionary")
        break
    while True:

        print("LM : ",lm,"\t\t RM",rm)
        print("=============================")
        print("LC : ",lc,"\t\t RC",rc)

        print("Left To Right")
        um=int(input("Enter Missionary : "))
        uc=int(input("Enter Cannable : "))

        if(um+uc <= 2) and (uc+um > 0) and (lm-um >= 0) and (lc-uc >= 0):
            lm=lm-um
            lc=lc-uc
            rm+=um
            rc+=uc
            break
        else:
            print('Invalid Input...!')

    if(rm==3 and rc==3):
        print("Win....!")
        break
    elif (rc > rm and rm > 0) or (lc > lm and lm > 0):
        print("Cannible eats Missionary")
        break
    
    while True:
        print("LM : ",lm,"\t\t RM",rm)
        print("=============================")
        print("LC : ",lc,"\t\t RC",rc)

        print("Right To Left")
        um=int(input("Enter Missionary : "))
        uc=int(input("Enter Cannable : "))

        if(um+uc <= 2) and (uc+um > 0) and (rm-um >= 0) and (rc-uc >= 0):
            rm=rm-um
            rc=rc-uc
            lm+=um
            lc+=uc
            break
        else:
            print('Invalid Input...!')
