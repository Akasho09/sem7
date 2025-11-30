#include <stdio.h>
#include <omp.h>

int main() {
    long long num_steps = 1000000;  // number of intervals
    double step = 1.0 / (double)num_steps;

    double pi = 0.0;

    // Parallelize the summation with reduction (+)
    #pragma omp parallel for reduction(+:pi)
    for (long long i = 0; i < num_steps; i++) {
        double x = (i + 0.5) * step;
        pi += 4.0 / (1.0 + x * x);   // correct formula
    }

    pi *= step;  // multiply by step OUTSIDE loop

    printf("PI = %.15f\n", pi);
    return 0;
}
