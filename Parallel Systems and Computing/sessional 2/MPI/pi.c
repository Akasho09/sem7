#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    int rank, size, i;
    long long num_steps = 100000000;  // Increase for more accuracy
    double step, x, local_sum = 0.0, total_sum = 0.0;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    step = 1.0 / (double)num_steps;

    // Each process calculates a part of the sum
    for (i = rank; i < num_steps; i += size) {
        x = (i + 0.5) * step;
        local_sum += 4.0 / (1.0 + x * x);
    }

    // Reduce all local sums to total_sum at root process (rank 0)
    MPI_Reduce(&local_sum, &total_sum, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    // Master computes final answer
    if (rank == 0) {
        double pi = total_sum * step;
        printf("Computed value of PI = %.15f\n", pi);
    }

    MPI_Finalize();
    return 0;
}
