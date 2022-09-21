# include <stdio.h>
# define ll long long

ll mod(ll a,ll b){
	if (a>=0){
		return a%b;
	}
	else{
		return (b-(-a%b))%b;
	}
}
