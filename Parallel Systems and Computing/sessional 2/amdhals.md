## AMDHALS LAW 
![alt text](<Screenshot 2025-11-07 at 3.47.31 PM.png>)

### Question :  Regular mode and Enhanced mode 
![alt text](image.png)

- T(a)= serial/R + parellel/nR ; R = execution rate in regular mode .
- integrate wrt da  / (b-a)
- Ravg = 1/Tavg.
- Speed up = Ravg / R.

## Gustafsons Law:
- The speedup of a program using multiple processors can increase linearly with the number of processors, if the problem size scales with the number of processors.
- states that if the problem size increses parellel size also increses but not sequential . => sequential doesnt become bottleneck .
- Amdhal assumes fixed problem size .
- Speeed Up = n+(1-n)s.
  - s = sequential . 
  - n = improveent factor.


## ☀️ Sun and Ni’s Law (Scaled Speedup Model)
- Sun and Ni’s Law is a generalization of both Amdahl’s Law and Gustafson’s Law.
- It provides a more realistic model of parallel speedup by taking into account both problem size and the number of processors — not assuming either one is fixed.
- Amdahl’s Law assumes fixed workload → pessimistic view.
- Gustafson’s Law assumes scaled workload → optimistic view.
- Sun and Ni’s Law combines both:
> It assumes the problem size may grow with the number of processors, but not necessarily linearly( y=g(x))
> Speed up = a+(1-a)*(g(n))/(a+(1-a)*(g(n)/n));

- if g(n)=1 => fixed prob size => Amdhals law.
- 


