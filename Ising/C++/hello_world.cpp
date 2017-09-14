#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

const int size = 3; //this is a constant so that the lattice can be created.
int lattice [size];

int main ()
{
cout << size << endl;
cout << lattice[2] << endl;

vector< vector<int> > a;

//m * n is the size of the matrix

int m = 2, n = 4;
//Grow rows by m
a.resize(m);
for(int i = 0 ; i < m ; ++i)
   {
   //Grow Columns by n
   a[i].resize(n);
   }
//Now you have matrix m*n with default values

//you can use the Matrix, now
a[1][0]=1;
a[1][1]=2;
a[1][2]=3;
a[1][3]=4;
cout << a[1][1] << endl;
}
