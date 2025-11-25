##  Variables
1. rank: ID of each MPI process (0,1,2,...)
2. size: total number of processes
3. num_steps: number of intervals for integration (more steps = more accuracy)
4. local_sum: partial sum computed by each process
5. total_sum: final sum (collected only by rank 0)
6. step: width of each interval = 1/num_steps

## 🧠 3. Initialize MPI
```c
MPI_Init(&argc, &argv);
MPI_Comm_rank(MPI_COMM_WORLD, &rank);
MPI_Comm_size(MPI_COMM_WORLD, &size);
```
- Starts MPI
- Gets each process’s rank
- Gets the total number of processes

   
## Divide work among processes
```c
for (i = rank; i < num_steps; i += size) {
    x = (i + 0.5) * step;
    local_sum += 4.0 / (1.0 + x * x);
}
```
- Each calculates its own partial sum.

## 🔽 6. Reduce partial sums to root (rank 0)
```yml
MPI_Reduce(&local_sum, &total_sum, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
```
- Combines all local_sum values into one total_sum
- Uses MPI_SUM operation
- Result is stored only in rank 0
    
## MPI_Finalize();
Shuts down MPI.