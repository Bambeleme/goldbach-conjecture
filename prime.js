const isPrime = (n) => {
    if (n <= 1) return false;
    for (let i = 2; i <= n - 1; i++)
        if (n % i == 0) return false;
    return true;
}

//console.log(isPrime(70));
//console.log(isPrime(23));

const listprimes = (limit) => {
    console.log("Berechnung der Primzahlen bis " + limit)
    n = [0, 0, 1, 1] 
    c = 0
    while (n.length <= limit-1) {
        n.push(0, 1);            
    }
    
    for (let i = 2; i <= limit**(0.5)+1; i++) {
        if (n[i] != 0) {
            for (let j = i * i; j < limit + 1; j+=i){
                n[j] = 0
            }            
        }
    }
    for (let i = 2; i <= limit; i++){
        if (n[i]!=0){
            c += 1
            p = i
            //console.log("nummer " + c + " " + n + " Länge: " + n.length)
            //console.log(p + " ist Primzahl bis " +i)
        }
    }
    console.log("Es gibt " + c + " Primzahlen im Bereich bis "+ limit)
    return n;
}
console.log(listprimes(2));