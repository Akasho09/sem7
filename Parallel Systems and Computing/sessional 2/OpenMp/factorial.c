#include <stdio.h>
#include <omp.h>

int main() {
    int N, i;
    long long factorial = 1;

    printf("Enter a number: ");
    scanf("%d", &N);

    // Parallel multiplication using reduction
    #pragma omp parallel for reduction(*:factorial)
    for (i = 1; i <= N; i++) {
        factorial *= i;
        printf("Thread Num : %d & curr Val : %lld \n" , omp_get_thread_num() ,factorial );
    }

    printf("Factorial of %d is %lld\n", N, factorial);

    return 0;
}
