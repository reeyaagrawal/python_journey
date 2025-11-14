// Write a program to count the number of positive and negative numbers in an array.
#include <iostream>
using namespace std;
int main() {
    int n;
    cout<<"enter no of element:";
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int pos=0,neg=0;
    for(int i=0;i<n;i++){
        if(arr[i]>=0){
            pos++;
        }else{
            neg++;
        }
    }
    cout<<"positive no:"<<pos<<"\tnegative no:"<<neg;
    return 0;
}