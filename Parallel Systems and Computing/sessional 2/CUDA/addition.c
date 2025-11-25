// Program: Vector Addition using CUDA
// Each GPU thread adds one element of A and B to produce C

#include <stdio.h>
#include <cuda.h>

#define N 256   // Size of the vectors

// ------------------------------
// CUDA Kernel Function
// ------------------------------
global void vecAdd(int *A, int *B, int *C)
{
    int i = threadIdx.x;      // Thread index
    C[i] = A[i] + B[i];       // Perform addition
}

// ------------------------------
// Main Function
// ------------------------------
int main()
{
    int size = N * sizeof(int);

    // Host (CPU) arrays
    int A[N], B[N], C[N];

    // Device (GPU) pointers
    int *devA, *devB, *devC;

    // Initialize input arrays on host
    for(int i = 0; i < N; i++) {
        A[i] = i;
        B[i] = i * 2;
    }

    // Allocate memory on GPU
    cudaMalloc((void**)&devA, size);
    cudaMalloc((void**)&devB, size);
    cudaMalloc((void**)&devC, size);

    // Copy data from Host → Device
    cudaMemcpy(devA, A, size, cudaMemcpyHostToDevice);
    cudaMemcpy(devB, B, size, cudaMemcpyHostToDevice);

    // Launch Kernel: 1 block, N threads
    vecAdd<<<1, N>>>(devA, devB, devC);

    // Copy result from Device → Host
    cudaMemcpy(C, devC, size, cudaMemcpyDeviceToHost);

    // Free device memory
    cudaFree(devA);
    cudaFree(devB);
    cudaFree(devC);

    return 0;
}
