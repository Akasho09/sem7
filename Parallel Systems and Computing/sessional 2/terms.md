## (i) GPU
- A GPU (Graphics Processing Unit) is a specialized electronic circuit designed to perform massively parallel computations.
- Originally used for graphics rendering, modern GPUs are general-purpose parallel processors used in:
    - Machine learning
    - Scientific simulations
    - Cryptography
    - Big-data analytics
- A GPU contains thousands of small cores that execute the same instruction on multiple data elements simultaneously (SIMD parallelism).
- Key Characteristics
    - Highly parallel architecture
    - Very high throughput
    - Ideal for floating-point operations
    - Used with programming models like CUDA, OpenCL

## CUDA
- CUDA (Compute Unified Device Architecture) is a parallel programming platform and API developed by NVIDIA.
- It allows programmers to write code (in C, C++, Python, etc.) that runs directly on NVIDIA GPUs for general-purpose computing (GPGPU).
- Features
    - Allows developers to launch thousands of threads in parallel
    - Supports GPU memory management
    - Provides libraries like cuBLAS, cuDNN
    - Used in AI, deep learning, simulations, image processing
- Why CUDA?
    - Easy to use
    - High performance on NVIDIA GPUs
    - Industry-standard for deep learning frameworks (TensorFlow, PyTorch, etc.)

## ✅ OPENMP
- OpenMP is an API for shared-memory parallel programming on multicore CPUs.
- It allows programmers to write parallel code using simple compiler directives (pragmas).
- ⭐ Key Features
    - Supports shared memory (all threads access the same memory space)
    - Parallelism through threads
    - Uses #pragma omp directives in C/C++ and Fortran
    - Easy to learn and incremental parallelism (add one pragma to parallelize a loop)
- ⭐ Example (Parallel For Loop)
    #pragma omp parallel for
    for(int i = 0; i < n; i++) {
        a[i] = a[i] * 2;
    }
- ⭐ Advantages
    - Simple to use
    - Low overhead for thread creation
    - Works best on multicore systems (single computer)
- ⭐ Where OpenMP is used
    - Scientific computing
    - Numerical simulations
    - Image processing
    - Matrix operations.

## ✅ MPI
- MPI (Message Passing Interface) is the standard for distributed-memory parallel programming.
- Unlike OpenMP, MPI works on multiple computers (nodes) connected via a network. Each process has its own private memory, and communication happens through explicit message passing.
![alt text](image-4.png)
- ⭐ Key Features
    - Supports distributed memory (cluster computing)
    - Uses processes, not threads
    - Communication using send and receive
    - Best suited for large-scale parallel applications on clusters/supercomputers
- ⭐ Example (Sending/Receiving Messages)
    - MPI_Send(&x, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
    - MPI_Recv(&y, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
- ⭐ Advantages
    - Scales to thousands of nodes
    - Portable across all HPC systems
    - High performance for distributed workloads
- ⭐ Where MPI is used
    - Weather forecasting
    - Molecular dynamics
    - Big-data analytics
    - Supercomputing applications



