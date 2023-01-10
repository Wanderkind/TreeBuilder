import std.stdio;


// ADJUST MAXIMUM LENGTH OF WORD IF NECESSARY

char[] word(){

    char[101] s;
    scanf("%s", &s);
    ulong trim;

    foreach(i; 0..101){
        if (s[i] == ' ' || s[i] == '\0'){
            trim = i;
            break;
        }
    }

    return s.dup[0..trim];
}

/*
string word(){

    char[101] s;
    scanf("%s", &s);
    ulong trim;

    foreach(i; 0..101){
        if (s[i] == ' ' || s[i] == '\0'){
            trim = i;
            break;
        }
    }

    return cast(string) s.dup[0..trim];
}
*/

void main(){

    while(true){
        writeln(word() == "yes" ? "good" : "bad");
    }
}
