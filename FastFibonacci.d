import std.stdio;
import std.algorithm;


bool[] bin (long n) {
    
    bool[] ans;
    long k = 1;
    int c = 1;
    while (k < n) {
        k <<= 1;
        c++;
    }

    while (c) {
        if (n >= k) { 
            ans ~= true;
            n -= k;
        }
        else{
            ans ~= false;
        }
        k >>= 1;
        c--;
    }

    return ans.reverse;
}

long[4] mul (long[4] a, long[4] b) {
    return [
        a[0]*b[0] + a[1]*b[2],
        a[0]*b[1] + a[1]*b[3],
        a[2]*b[0] + a[3]*b[2],
        a[2]*b[1] + a[3]*b[3]
    ];
}

long l (long n) {
    
    long[4] l = [1, 1, 1, 0];
    long[4] L = [1, 0, 0, 1];
    bool[] B = bin(n);
    foreach (i; 0..B.length) {
        if (i) {l = mul(l[0..4], l[0..4]);}
        if (B[i]) {L = mul(L[0..4], l[0..4]);}
    }

    return L[1];
}
