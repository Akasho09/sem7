#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    
    int ans = 1;       // Final factorial result (only correct on rank 0)
    int curr = 1;      // Local partial product for each process
    int size, rank;    // Total number of processes and current process ID
    int n;             // Number for which factorial will be computed

    // ------------------------- MPI INITIALIZATION -------------------------
    MPI_Init(&argc, &argv);                     // Start MPI environment
    MPI_Comm_size(MPI_COMM_WORLD, &size);       // Get number of processes
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);       // Get rank of this process

    // ------------------------- INPUT ON ROOT PROCESS -------------------------
    if (rank == 0) {
        printf("Enter n (compute n!): ");
        scanf("%d", &n);    // Only rank 0 takes input
    }

    // ------------------------- BROADCAST n TO ALL PROCESSES -------------------------
    // Every process must know the value of n, so we broadcast it from rank 0.
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);

    /*
        WORK DIVISION LOGIC:
        
        Each process multiplies numbers starting from:
            (rank + 1) and then jumps by 'size' each step.

        Example for n = 10 and size = 4:
            rank 0: 1, 5, 9
            rank 1: 2, 6, 10
            rank 2: 3, 7
            rank 3: 4, 8
    */

    // ------------------------- LOCAL PARTIAL FACTORIAL -------------------------
    for (int i = rank + 1; i <= n; i += size) {
        curr *= i;  // Multiply only assigned numbers
    }

    /*
        ------------------------- GLOBAL REDUCTION -------------------------
        MPI_Reduce collects all partial results (curr) from all processes,
        applies a reduction operator (MPI_PROD = multiplication),
        and stores the final result in 'ans' on the root process (rank 0).

        MPI_Reduce(
            sendbuf    → &curr
            recvbuf    → &ans (only valid on root)
            count      → 1 value per process
            datatype   → MPI_INT
            operator   → MPI_PROD (product)
            root       → 0
            communicator → MPI_COMM_WORLD
        );
    */
    MPI_Reduce(&curr, &ans, 1, MPI_INT, MPI_PROD, 0, MPI_COMM_WORLD);

    // ------------------------- PRINT RESULT (ONLY ROOT) -------------------------
    if (rank == 0) {
        printf("\nFactorial of %d = %d\n", n, ans);
    }

    // ------------------------- FINALIZE MPI -------------------------
    MPI_Finalize();   // End MPI environment
    return 0;
}
