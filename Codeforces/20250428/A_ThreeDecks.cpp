#include<iostream>

using namespace std;

bool CanMoveToBeEqual(int a, int b, int c){
    int x=(a+b+c);
    if (x%3!=0 || c<a || c<b){
        return false;
    }
    int val =x/3;
    if(a>val || b>val){
        return false;
    }
    return true;
    }

    

int main(){
    int t;
    cin>>t;
    while (t){
        int a,b,c;
        cin>>a>>b>>c;
        bool res=CanMoveToBeEqual(a,b,c);
        if(res){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
        t--;
    }
}
