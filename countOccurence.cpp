// Write a program to count how many times a given number occurs in an array.
#include <iostream>
using namespace std;
int main() {
   int arr[5];
   int key;
   int  count=0;
   cout<<"enter 5 elements:";
   for(int i=0;i<5;i++){
       cin>>arr[i];
   }
   cout<<"enter element u want to search:";
   cin>>key;
   for(int i=0;i<5;i++){
     if(arr[i]==key)
     count++;
   }
   cout<<"occurence:"<<count;
    return 0;
}