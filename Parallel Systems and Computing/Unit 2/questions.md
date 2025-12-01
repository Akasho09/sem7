## Thriughput :
![alt text](image-12.png)

## 
![alt text](image-13.png)

![alt text](image-14.png)


## Optimal number of stages :
![alt text](image-15.png)
-  Total time = Ts+Td
              = T/k + Td.
- Total stages :  k+N-1.
> Total time = (k+N-1)*(T/k + Td).
- diff wrt k.

![alt text](image-19.png).

## Reservation table question :
- Columns 1–4: first use of F1
- Columns 5–8: F2 and F3 (overlapping)
- Columns 9–12: second use of F1

| Stage / Time | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| ------------ | - | - | - | - | - | - | - | - | - | -- | -- | -- |
| **S1** (F1)  | X |   |   |   |   |   |   |   | X |    |    |    |
| **S2** (F1)  |   | X |   |   |   |   |   |   |   | X  |    |    |
| **S3** (F1)  |   |   | X | X |   |   |   |   |   |    | X  | X  |
| **T1** (F2)  |   |   |   |   | X |   |   | X |   |    |    |    |
| **T2** (F2)  |   |   |   |   |   | X |   |   |   |    |    |    |
| **T3** (F2)  |   |   |   |   |   |   | X |   |   |    |    |    |
| **U1** (F3)  |   |   |   |   |   | X |   | X |   |    |    |    |
| **U2** (F3)  |   |   |   |   |   |   | X |   |   |    |    |    |
| **U3** (F3)  |   |   |   |   |   |   |   | X |   |    |    |    |
