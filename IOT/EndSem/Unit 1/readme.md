## 1. Introduction to Mobile Computing and its Architecture
- Mobile computing = using portable computing devices (smartphones, tablets, laptops) that can access network services anytime, anywhere over wireless networks.
- Key features:
    - Mobility: User can move while still connected.
    - Wireless communication: Uses cellular, Wi-Fi, Bluetooth, etc.
    - Context awareness: Device can know location, network state, etc.
    - Resource constraints: Limited battery, CPU, bandwidth.
- Typical Mobile Computing Architecture.
- Mobile Device Layer
    - Smartphones, tablets, laptops with OS (Android, iOS, etc.).
    - Runs applications and user interface.
- Wireless Access Network
    - Cellular base stations (BTS/eNodeB/gNodeB), Wi-Fi APs.
    - Handles radio communication with mobile devices.
- Core Network
    - Mobile Switching Centre (MSC), SGSN/GGSN, packet core, HLR/HSS.
    - Functions: mobility management, call routing, authentication, billing.
- External Networks / Application Servers
    - Internet, corporate intranets, cloud servers, web services.
- The architecture ensures seamless handoff, security, and QoS while the user moves.

## 2. Basic Cellular System
- A cellular system divides the service area into many small regions called cells. Each cell has:
    - A Base Station (BS) with antennas and radio equipment.
    - A fixed number of radio channels (frequencies or time slots).
    - A Mobile Switching Centre (MSC) that connects many BSs and links them to PSTN/Internet.

## 3. Transmission Problems and Their Solutions in Cellular Systems
- Because radio propagation is wireless, several impairments occur:
1. (a) Path Loss
- Signal strength decreases with distance from base station.
- Solution: Use higher antenna heights, power control, cell planning.

2. (b) Shadowing (Slow Fading)
- Obstacles like buildings, hills cause large-scale variations.
- Solution: Cell planning, diversity techniques (multiple antennas, macro/micro cells).

3. (c) Multipath Fading (Fast Fading)
- Signal reaches receiver via many paths with different delays → constructive/destructive interference.
- Solution:
    - Equalization, spread spectrum, OFDM.
    - Diversity (space, frequency, time).
    - Interleaving and error-correcting codes.

4. (d) Interference
- Co-channel and adjacent-channel interference.
- Solution: Proper frequency planning, guard bands, sectoring.

5. (e) Noise
- Thermal noise, man-made noise.
- Solution: Filtering, coding, improving SNR by power control.

## 4. Cellular Geometry
- To cover a large area, cells must:
    - Fill space without gaps or overlaps, and
    - Be easy to model mathematically.
- An ideal shape for cells is the regular hexagon (often used in theory):
    - Hexagons tile the plane without gaps (unlike circles).
    - Distance between cell centers is equal.
    - Simplifies calculation of reuse distance and interference.
- Real cells are not perfectly hexagonal, but this model is used for frequency planning and capacity analysis.


## 5. Components of a Cellular Mobile Network
1. Mobile Station (MS)
- User’s handset + SIM.
- Provides voice/data interface to user.

2. Base Transceiver Station (BTS / eNodeB / gNodeB)
- Radio equipment and antennas.
- Handles air-interface with mobiles.

3. Base Station Controller (BSC) / Radio Network Controller (RNC)
- Controls multiple BTSs.
- Manages radio resources, handovers, power control.

4. Mobile Switching Centre (MSC)
- Switch for voice calls and SMS.
- Connects to PSTN and other MSCs.

5. Home Location Register (HLR) / Home Subscriber Server (HSS)
- Database storing subscriber profile, services, and current location.

6. Visitor Location Register (VLR)
- Temporary database for users currently in that MSC area.

7. Authentication Centre (AuC)
- Stores secret keys for authentication and encryption.

8. Equipment Identity Register (EIR)
- Database of valid/invalid device IMEIs.

9. Packet Core (e.g., SGSN/GGSN in 3G, EPC in 4G, 5GC in 5G)
- Handles data services and internet connectivity.

## 6. Concept of Frequency Re-use Channels
- Total available spectrum is limited. To serve many users:
    - Service area divided into cells.
    - Cells are grouped into clusters of size N (N = number of cells in a cluster).
    - Each cluster uses the full set of frequencies once.
    - The same frequencies are reused in another cluster far enough away so that interference is tolerable.
- Frequency Reuse Factor = 1 / N
- Smaller N → more reuse → higher capacity but more interference.

## 7. Cell Splitting
- When traffic increases in a busy area:
    - Original large cell is split into smaller cells (microcells, picocells).
    - Each small cell has its own base station and a subset of channels.
- Effects:
    - More cells → more channels per area → higher capacity.
    - Reduced transmitter power because cell radius is smaller.
    - Requires more base stations and more complex handoff management.
- Used in city centers, malls, airports, etc.

## 8. Sectoring and Clustering of a Cell
- Sectoring
    - Instead of one omni-directional antenna, the cell uses directional antennas to divide it into sectors (typically 3 sectors of 120° or 6 sectors of 60°).
    - Each sector has its own subset of frequencies and antenna.
    - Advantages:
    - Reduces co-channel interference because antenna focuses power in one direction.
    - Improves signal-to-interference ratio (SIR) and capacity.
- Clustering
    - A cluster is a group of N cells in which each frequency is used only once.
    - The same pattern of clusters is repeated across the network.
    - Cluster size N may be 3, 4, 7, 9, 12, etc., depending on interference requirements.
    - Clustering + sectoring help achieve good coverage and capacity with limited spectrum.

## 9. Co-channel Interference and System Capacity
- Co-channel Interference (CCI)
- Occurs when cells using the same frequency (co-channel cells) interfere with each other.
- These cells are separated by a distance D (reuse distance).
- Ratio D/R (reuse ratio) depends on cluster size N: D/R = roo(3N)
where
R = cell radius,
N = cluster size.
- Larger N → larger D/R → less CCI but fewer channels per cell (lower capacity).
- System Capacity
- Capacity = number of simultaneous calls/users the system can handle.
- Depends on:
- Total number of channels C available.
- Cluster size N.
- Number of cells M.
- Number of channels per cell: S = C/N.
- Total capacity in the system: S*M = C/N * M.

- To increase capacity:
- Reduce N (more reuse),
- Split cells (more cells M),
- Use sectoring, microcells, smart antennas, etc.

## 10. Trunking and Grade of Service (GoS)
Trunking Concept
- In telephony, many users share a common pool of channels called a trunk.
- Not all users call at the same time; therefore fewer channels than users are sufficient.
- Example: 1000 users may share 100 channels.
- Trunking theory uses Erlangs to model traffic:
- 1 Erlang = one channel continuously occupied for one hour.
- Grade of Service (GoS)
- GoS is a measure of quality of service in terms of call blocking or delay.
- Common definition:
- GoS=P(call is blocked or delayed)
- Example:
GoS = 0.02 means 2% of attempted calls are blocked during busy hour.
- For systems where blocked calls are cleared (no waiting), Erlang B formula is used to find required number of channels for given traffic and GoS.
- Designers select an acceptable GoS (e.g., 1–2% blocking) and then dimension the trunk size.

