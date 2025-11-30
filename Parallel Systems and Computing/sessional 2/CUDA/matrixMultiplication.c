#include <stdio.h>
#include <cuda.h>

#define N 256 

int main () {
    int size = N*N*sizeof(int);

    int *A , *B , *C ;
    int *dA , *dB , *dC ;

    // allocate host memory
    A = (int*)malloc(size);
    B = (int*)malloc(size);
    C = (int*)malloc(size);

     // initialize matrices
    for(int i = 0; i < N*N; i++) {
        A[i] = 1;
        B[i] = 2;
    }

        // allocate device memory
    cudaMalloc((void**)&dA, size);
    cudaMalloc((void**)&dB, size);
    cudaMalloc((void**)&dC,size);

        // copy data to device
    cudaMemcpy(dA,A,size,cudaMemoryHostToDevice);
    cudaMemcpy(dA,A,size,cudaMemoryHostToDevice);

    // launch kernel
    matMul<<<grid,block>>>(dA,dB,dC,N);
    
        // copy result back
    cudaMemcpy(C, dC, size, cudaMemcpyDeviceToHost);

    cudaFree(dA); cudaFree(dB); cudaFree(dC);
    free(A); free(B); free(C);

    return 0;

}