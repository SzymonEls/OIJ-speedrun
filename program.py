import time

#Plik 1 -----
plik_s = input("Ścieżka do pliku z danymi wejściowymi: ")

#usuwanie "Windowsowych" sleshy (zm. na odpowiednie)
for u in range(len(plik_s)):   
    if chr(92) == plik_s[u]:
        plik_s = plik_s[:u] + "/" + plik_s[u + 1:]

plik = open(plik_s)
plik_l = plik.readlines()
plik.close()

inp = plik_l[1]#----------

#Plik 2 -----
plik_s = input("Ścieżka do pliku z danymi wyjściowymi: ")

for u in range(len(plik_s)):   
    if chr(92) == plik_s[u]:
        plik_s = plik_s[:u] + "/" + plik_s[u + 1:]

plik2 = open(plik_s)
plik2_odp = plik2.readlines()
plik2.close()

#DANE WYJŚCIOWE - DO ZMIANY (czy int?)
ODP = int(plik2_odp[0])#---------
#DANE WYJŚCIOWE - DO ZMIANY

czas1 = time.time()#Stoper - start

#------
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
        #print("weszło" + str(T_caly_czas))#TU
        ost = T[u]
        ost_u = u + 1
        #print("u = " + str(u))#TU
        cykl = []
        cykl_czas = []
        
        while 1 == 1:
            #print("ost = " + str(ost))#TU
            #print("ost_u = " + str(ost_u))#TU
            cykl.append(ost)
            cykl_czas.append(ost_u)
            ost_u = ost
            ost = T[ost - 1]
            if ost_u in cykl_czas:
                break
            if cykl_czas[len(cykl_czas) - 1] == -2:
                T_caly_czas[ost_u - 1] = -2
                #print("odwołanie do nieopłacalnej")#TU
                odw_niep = True
                break
            
        if odw_niep != True:
            x = 0
            while x != len(cykl):
                #print(cykl_czas)#TU
                #print(x)
                #print(cykl)
                if T_caly_czas[cykl_czas[x] - 1] != -1:
                    teraz_nie = True
                    #print("wyjście")
                    break
                    

                if cykl_czas[x] in cykl:
                    1 == 1
                else:
                    #print(" uznaje za nieopłacalne")#TU
                    T_caly_czas[cykl_czas[x] - 1] = -2
                    del cykl[x]
                    del cykl_czas[x]
                    x = x - 1
                x += 1
        
        
            if teraz_nie != True:
                cykl_suma = sum(cykl_czas)
                #print("--")#TU
                for x in range(len(cykl)):
                    #print(cykl_czas[x])#TU
                    T_caly_czas[cykl_czas[x] - 1] = cykl_suma
        teraz_nie = False
        odw_niep = False

p_najw = 0
for b in range (len(T_caly_czas)):
    if T_caly_czas[b] > p_najw:
        p_najw = T_caly_czas[b]
#print(T_caly_czas)
wynik = p_najw
#------

#Podsumowanie
czas2 = time.time()
czas3 = czas2 - czas1

if wynik == ODP:
    print("Dobrze!!!")
    print("Czas: " + str(czas3))
    print("Odp: " + str(wynik))
else:
    print("Dobrze!!!")
    print("Czas: " + str(czas3))
    print("Odp: " + str(wynik))