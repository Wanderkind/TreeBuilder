import std.stdio;
import std.algorithm;
import std.math;
//import std.conv;
//import std.numeric;
//import std.range;
import std.array;
//import std.bigint;
//import std.string;


int[] add(int[] a, int[] b){

    ulong A = a.length;
    ulong B = b.length;
    int[] k = [], ans;

    if(A<B){
        foreach(_; 0..B-A){
            k ~= 0;
        } 
        a = k ~ a;
    }
    else{
        foreach(_; 0..A-B){
            k ~= 0;
        }
        b = k ~ b;
    }
    
    int v;
    int m = cast(int)max(A,B);
    foreach(i; 0..m){
        v = m-i-1;
        ans ~= a[v]+b[v];
    }
    
    ans.reverse;
    return ans;
}

int[] mul(int[] a, int[] b){

    ulong A = a.length;
    ulong B = b.length;
    int[] ans;
    ulong l = A+B-1;
    foreach(_; 0..l){
        ans ~= 0;
    }

    int q;
    foreach(i; 0..B){
        q = b[B-1-i];
        foreach(j; 0..A){
            ans[l-1-i-j] += q*a[A-1-j];
        }
    }
    
    return ans;
}

int[] fin(int[] a, int[] b){

    ulong A = a.length;
    ulong B = b.length;
    int[] ans, c, k;

    foreach(i; 0..A){
        c = [1];
        foreach(_; 0..i){
            c = mul(c, b);
        }
        
        k = [];
        foreach(j; c){
            k ~= a[A-1-i]*j;
        }

        ans = add(ans, k);
    }

    return ans;
}

int[] rem(int[] a, int[] b){

    ulong A = a.length;
    ulong B = b.length;
    
    int[] k, c;
    c = a[0..B];
    foreach(i; 0..A-B+1){
        k = [];
        foreach(j; b){
            k ~= -c[i]*j;
        }
        c = add(c, k);
        if(i<A-B){
            c ~= a[B+i];
        }
    }

    foreach(_; 0..A-1){
        if (!c[0]){
            c = c.remove(0);
        }
    }

    return c;
}

bool divides(int[] a, int[] b){
    return rem(a, b) == [0];
}

bool dyn(int[] a){
    return divides(fin(a, [1, 0, -2]), a);
}
