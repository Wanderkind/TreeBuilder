import std.stdio;


// ADJUST MAXIMUM LENGTH OF WORD IF NECESSARY

char[] word(){

    char[101] s;
    scanf("%s", &s);
    ulong trim;

    foreach(i; 0..102){
        if (s[i] == '\0'){
            trim = i;
            break;
        }
    }

    return s.dup[0..trim];
}

void main(){

    while(true){
        writeln(word() == "yes" ? "good" : "bad");
    }
}
