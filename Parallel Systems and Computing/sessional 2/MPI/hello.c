  #include <stdio.h>
  #include <mpi.h>
  #include <string.h>
  #define BUFFER_SIZE 32
  int main(int argc,char *argv[]){
    
      int rank , processes ;
      MPI_Init(&argc,&argv);
      MPI_Comm_size(MPI_COMM_WORLD,&processes);
      MPI_Comm_rank(MPI_COMM_WORLD,&rank);
      
      printf("%d : hello (p=%d) \n" , rank , processes);
      
      MPI_Finalize();
  }