const isPrime = (n) => {
    if (n <= 1) return false;
    for (let i = 2; i <= n - 1; i++)
        if (n % i == 0) return false;
    return true;
}

console.log(isPrime(70));
console.log(isPrime(23));

const listprimes = (limit) => {
    n = [0, 0] 
    c = 0
    while (n.length <= limit) {
        n.push(1);    
    }
    for (let i = 2; i <= limit**(0.5); i++) {
        if (n[i] != 0) {
            for (let j = i * i; j < limit + 1; j+=i){
                n[j] = 0
            }            
        }
    }
    for (let i = 1; i < n.length; i++){
        if (n[i]!=0){
            c += 1
            p = i
            //console.log(p + " ist Primzahl " + c) 
        }
    }
    
    console.log("Es gibt " + c + " Primzahlen im Bereich bis "+ limit)
    return true;
}
console.log(listprimes(10**8));




/*
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
        for i in range(1,x):
                if n[i]!=0:
                    c += 1
                    p = i
                    #print(i, "is prime")
        print("Limit:",x,"\nLargest:",p,"\nPrimes:",c)
        return n
*/
