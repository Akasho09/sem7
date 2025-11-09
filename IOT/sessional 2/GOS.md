## Trunking and Grade of services

### Trunking 
is a method of sharing a small number of communication channels (resources) among a large number of users, on the assumption that not all users will need the channel at the same time.

### ⚙️ 2. Grade of Service (GoS)
- The Grade of Service (GoS) is the probability that a call will be blocked or delayed due to all channels being busy.
- GoS = Probability that a call cannot be served immediately.
- It represents the quality of service offered by the network in terms of call accessibility.
OR ability of a user to acesses the trunk in the busieset hour .

> GoS = Number of blocked calls / Total number of call attempts

## 🧮 3. Trunking Theory (Erlang Models)
The relationship between trunking and GoS is mathematically modeled using Erlang formulas developed by A.K. Erlang.

1. set up time : 
- time required to allocate a channel to a requesting user .

2. Blocked/lost call : 
- call which cant be placed at time of reuqest , due to congestion .

3. Holding time : (H)
- duration of a typical call .

4. Traffic intensity : (A)
- Measure of channel time utilization , in erlangs. 

5. Load :
Traffic intensity across entire trunked radio systme , in erlangs. 

6. rEQUEST rRate : lamda
- Average no of call requests per unit time .

> Traffic intensity by each user : A' = lamda . H
> Total Traffic intensity => A = U.A' 
U = no of users 
> Intensity per channel => Ac = A/C
C = no of channels .


