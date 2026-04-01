//el mismo programa del SRP pero procurando
// incluir DIP

#include <iostream>
using namespace std;

// Abstracción
class SequenceCalculator {
public:
    virtual int calculate(int N) = 0;
    virtual ~SequenceCalculator() {}
};

// Implementación concreta
class TriangularCalculator : public SequenceCalculator {
public:
    int calculate(int N) override {
        return (N * (N + 1)) / 2;
    }
};

// Módulo de alto nivel
class DotCounter {
private:
    SequenceCalculator& calculator;

public:
    DotCounter(SequenceCalculator& calc) : calculator(calc) {}

    int count(int N) {
        int sum = 0;
        for (int i = 1; i <= N; i++) {
            sum += calculator.calculate(i) * 3;
        }
        return sum;
    }
};

int main() {
    int N;
    cin >> N;

    TriangularCalculator calculator;
    DotCounter counter(calculator);

    cout << counter.count(N) << endl;

    return 0;
}