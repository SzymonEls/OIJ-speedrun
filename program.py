inp = input()
T_chwil = inp.split(" ")
T = []
T_caly_czas = []
teraz_nie = False
odw_niep = False



for i in range(len(T_chwil)):
    T.append(int(T_chwil[i]))
    T_caly_czas.append(-1)

for u in range(len(T)):
    if T_caly_czas[u] == -1:
        print("weszło" + str(T_caly_czas))#TU
        ost = T[u]
        ost_u = u + 1
        print("u = " + str(u))#TU
        cykl = []
        cykl_czas = []
        
        while 1 == 1:
            print("ost = " + str(ost))#TU
            print("ost_u = " + str(ost_u))#TU
            cykl.append(ost)
            cykl_czas.append(ost_u)
            ost_u = ost
            ost = T[ost - 1]
            if ost_u in cykl_czas:
                break
            if cykl_czas[len(cykl_czas) - 1] == -2:
                T_caly_czas[ost_u - 1] = -2
                print("odwołanie do nieopłacalnej")#TU
                odw_niep = True
                break
            
        if odw_niep != True:
            x = 0
            while x != len(cykl):
                print(cykl_czas)#TU
                print(x)
                print(cykl)
                if T_caly_czas[cykl_czas[x] - 1] != -1:
                    teraz_nie = True
                    print("wyjście")
                    break
                    

                if cykl_czas[x] in cykl:
                    1 == 1
                else:
                    print(" uznaje za nieopłacalne")#TU
                    T_caly_czas[cykl_czas[x] - 1] = -2
                    del cykl[x]
                    del cykl_czas[x]
                    x = x - 1
                x += 1
        
        
            if teraz_nie != True:
                cykl_suma = sum(cykl_czas)
                print("--")#TU
                for x in range(len(cykl)):
                    print(cykl_czas[x])#TU
                    T_caly_czas[cykl_czas[x] - 1] = cykl_suma
        teraz_nie = False
        odw_niep = False
        
print(T_caly_czas)