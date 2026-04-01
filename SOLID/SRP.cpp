// Codigo tomado de un ejercicio de programacion
// competitiva se crean dos funciones con una
// tarea unica, para no dejarlo todo en el main

#include <iostream>
using namespace std;

int count_dots(int N);
int first_n(int N);

int main() {
    int N;
    cin >> N;
    int dots = count_dots(N);
    cout << dots << endl;
    return 0;
}

int count_dots(int N) {

    int sum = 0;
    for(int i=1; i<=N; i++){
        int dots = first_n(i)*3;
        sum += dots;
    }
    return sum;
}

int first_n(int N) {

    int result = (N * (N+1))/2;
    return result;
}