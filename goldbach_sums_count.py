##Goldbach Zerlegungen Funktionen

def isprime1opt(x):
        ##print ("CODE 1SM: Prime Single Mesh Opt")
        n = [0,0]
        c = 0
        for i in range(1,x):                
                n.append(1)
        for i in range(2,int(x**.5)+1,1):                               
                if n[i]!=0:
                        for j in range(i*i,x+1,i):
                                n[j]=0
               #print(n)
        for i in range(1,x):
                if n[i]!=0:
                    c += 1
                    p = i
                    #print(i, "is prime")
        print("Limit:",x,"\nLargest:",p,"\nPrimes:",c)
        return n

def GoldbachCon(x):
    import datetime
    import matplotlib.pyplot as plt
    a = datetime.datetime.now()
    print("GoldbachCon Time: ",a)

    s_k, s_m, s_g = [10],[12],[14]               #Listen kleiner, mittlerer und großers Summen
    S_k, S_m, S_g = [0], [0], [0]                #Anzahl der Zerlegungen

    n = isprime1opt(x+4)                         #Primzahlen abrufen
    n[3]=0                                       #"3" aus der Liste entfernen
    n_k, n_g =[],[]                              #Liste kleiner und großer Primzahlen
    
    for i in range(0,len(n),1):                  #Primzahliste in Werte umwandeln
        if n[i] == 1: n[i] = i
    for i in range(5,len(n),6):                  #Liste kleiner Primzahlen
        if n[i]!=0: n_k.append(n[i])
    for i in range(7,len(n),6):                  #Liste großer Primzahlen
        if n[i]!=0: n_g.append(n[i])
    for i in range(0,round(x/6)-2,1):            #Listen der 3 verschiedenen Summen auffüllen
        s_k.append(s_k[i] + 6)                   #und Anzahl der Zerlegungen Null setzen
        s_m.append(s_m[i] + 6)
        s_g.append(s_g[i] + 6)
        S_k.append(0)                           
        S_m.append(0)   
        S_g.append(0)

    #print(n,"\n",n_k,"\n",n_g)
        
    S_K=len(s_k)
    N_K=len(n_k)

    b = datetime.datetime.now()
    c = b-a
    print ("Pre Calculation Time: ", c.seconds, "seconds", c.microseconds, "microseconds")
    print ("---------------------------------------------------------------------------")

    
    for i in range (0,S_K,1):
        #k=0                                    ##TESTING SPEED
        #while n_k[k] < round(s_k[i]/2)+1:
        #    if s_k[i] - n[j] in n_k:
        #        S_k[i]+= 1
        #        k += 1        
        for j in range (5,round(s_k[i]/2)+1,6):
            if n[j]>0 and s_k[i] - n[j] in n_k:
                S_k[i]+= 1
        for j in range (5,round(s_m[i]/2)+1,6):        
            if n[j]>0 and s_m[i] - n[j] in n_g:
                S_m[i]+= 1
        for j in range (7,round(s_m[i]/2)+1,6):        
            if n[j]>0 and s_m[i] - n[j] in n_k:
                S_m[i]+= 1
        for j in range (7,round(s_g[i]/2)+1,6):        
            if n[j]>0 and s_g[i] - n[j] in n_g:
                S_g[i]+= 1
        #print ("Big GBS checked")
    
    c = datetime.datetime.now()
    d = c-a
    print ("Total Calculation Time: ", d.seconds, "seconds", d.microseconds, "microseconds")
    print ("---------------------------------------------------------------------------")

    #print (s_k,"\n",s_m,"\n", s_g)
    #print (S_k,"\n",S_m,"\n", S_g)
    
    plt.plot(s_k, S_k, "r-", linewidth=0.01, marker='o', markersize=0.1)
    #plt.show()
    plt.plot(s_m, S_m, "b-", linewidth=0.01, marker='o', markersize=0.1)
    #plt.show()
    plt.plot(s_g, S_g, "g-", linewidth=0.01, marker='o', markersize=0.1)
    plt.show()


def gbs_is(s_k,S_k,n,n_k):
    for i in range (0,len(s_k),1):
        S_k[i]=0    
        for j in range (5,round(s_k[i]/2)+1,6):
            if n[j]>0 and s_k[i] - n[j] in n_k:
                S_k[i]+= 1
    return S_k

def gbs_ig(s_g,S_g,n,n_g):
    for i in range (0,len(s_g),1):
        S_g[i]=0    
        for j in range (7,round(s_g[i]/2)+1,6):
            if n[j]>0 and s_g[i] - n[j] in n_g:
                S_g[i]+= 1
    return S_g

def gbs_im(s_m,S_m,n,n_g,n_k):
    for i in range (0,len(s_m),1):
        S_m[i]=0
        for j in range (5,round(s_m[i]/2)+1,6):
            if n[j]>0 and s_m[i] - n[j] in n_g:
                S_m[i]+= 1
        for j in range (7,round(s_m[i]/2)+1,6):
            if n[j]>0 and s_m[i] - n[j] in n_k:
                S_m[i]+= 1
    return S_m
               
def GoldbachCon_Multi(x):
    import threading
    import time
    import datetime
    import matplotlib.pyplot as plt
    a = datetime.datetime.now()
    print("GoldbachCon_Multi Time: ",a)
    s_k, s_m, s_g = [10],[12],[14]               #Listen kleiner, mittlerer und großers Summen
    S_k, S_m, S_g = [0], [0], [0]                #Anzahl der Zerlegungen
    n = isprime1opt(x+4)                         #Primzahlen abrufen
    n[3]=0                                       #"3" aus der Liste entfernen
    n_k, n_g =[],[]                              #Liste kleiner und großer Primzahlen    
    for i in range(0,len(n),1):                  #Primzahliste in Werte umwandeln
        if n[i] == 1: n[i] = i
    for i in range(5,len(n),6):                  #Liste kleiner Primzahlen
        if n[i]!=0: n_k.append(n[i])
    for i in range(7,len(n),6):                  #Liste großer Primzahlen
        if n[i]!=0: n_g.append(n[i])
    for i in range(0,round(x/6)-2,1):            #Listen der 3 verschiedenen Summen auffüllen
        s_k.append(s_k[i] + 6)                   #und Anzahl der Zerlegungen Null setzen
        s_m.append(s_m[i] + 6)
        s_g.append(s_g[i] + 6)
        S_k.append(0)                           
        S_m.append(0)   
        S_g.append(0)
        
    S_K=len(s_k)
    N_K=len(n_k)    
    b = datetime.datetime.now()
    c = b-a
    print ("Pre Calculation Time: ", c.seconds, "seconds", c.microseconds, "microseconds")
    print ("---------------------------------------------------------------------------")

    t1=threading.Thread(target=gbs_is,args=(s_k,S_k,n,n_k,))
    t1.start()
    t2=threading.Thread(target=gbs_ig,args=(s_g,S_g,n,n_g,))
    t2.start()
    t2.join()
    t3=threading.Thread(target=gbs_im,args=(s_m,S_m,n,n_g,n_k))
    t3.start()
    t3.join()
    #gbs_is(s_k,S_k,n,n_k)
    #gbs_ig(s_g,S_g,n,n_g)   
    #gbs_im(s_m,S_m,n,n_g,n_k)
    
    c = datetime.datetime.now()
    d = c-a
    print ("Total Calculation Time: ", d.seconds, "seconds", d.microseconds, "microseconds")
    print ("---------------------------------------------------------------------------")
    
    plt.plot(s_k, S_k, "r-", linewidth=0.01, marker='o', markersize=0.1)
    plt.plot(s_m, S_m, "b-", linewidth=0.01, marker='o', markersize=0.1)
    plt.plot(s_g, S_g, "g-", linewidth=0.01, marker='o', markersize=0.1)
    plt.show()

   
GoldbachCon(1*10**5)
GoldbachCon_Multi(1*10**5)



