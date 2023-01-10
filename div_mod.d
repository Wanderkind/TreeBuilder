import std.stdio;

int mod(int a, int b){
    return (a >= 0 ? a%b : (b-(-a%b))%b);
}
int div(int a, int b){
    return (a >= 0 ? a/b : (a+(-a%b))/b-1);
}
