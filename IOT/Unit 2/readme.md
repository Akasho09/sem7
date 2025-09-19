## GSM Architecture : 
GSM stands for Global System for Mobile Communications. It is a standard developed to describe protocols for second-generation (2G) digital cellular networks used by mobile phones.

- operates in 4 diff frequency regions 
- cell size in GSM n/w :
    - Macro
    - Micro
    - Pico : 
    - Umbrella

### 📌 Key Features of GSM
- Digital Technology
    - Unlike the earlier analog systems, GSM uses digital transmission for voice and data.

- SIM (Subscriber Identity Module)
    - Stores user identity, authentication, and network information.
    - Allows users to switch devices while keeping the same phone number and data.

- Frequency Bands
    - Operates in frequency bands such as 900 MHz, 1800 MHz, and 1900 MHz depending on the region.

- Data Services
    - Provides voice calls, SMS (Short Message Service), and limited data transmission (GPRS, EDGE).

- Roaming
    - Enables users to access mobile services across different networks and countries.

- Security
    - Encryption and authentication are built-in to protect calls and messages.

- Efficient Spectrum Use
    - Uses Time Division Multiple Access (TDMA) to allow multiple users to share the same frequency channel.

## GSM Architecture :
![alt text](image-1.png)

1. Mobile Station (MS)
The user's device (mobile phone) and SIM card.

2. Base Station Subsystem (BSS)
Handles communication between the mobile station and the network.

- Includes:
    - Base Transceiver Station (BTS) – Handles radio communication.
    - Base Station Controller (BSC) – Manages multiple BTS units and controls handovers.

3. Network and Switching Subsystem (NSS)
- Responsible for call routing, mobility management, and connection setup.

- Includes:
    - Mobile Switching Center (MSC) – The main controller for calls.
    - Home Location Register (HLR) – Database storing user information.
    - Visitor Location Register (VLR) – Temporarily stores information for roaming users.
    - AuC (Authentication Center) 
    - EIR (Equipment Identity Register) 

- Operation and Support Subsystem (OSS)
    - Provides maintenance, monitoring, and management tools.

### ✅ GSM Communication Process
1. The user initiates a call or sends data from the Mobile Station.
1. The signal is transmitted via the Base Transceiver Station.
1. The Base Station Controller manages radio resources and forwards the call to the Mobile Switching Center.
1. The Mobile Switching Center routes the call to its destination and manages user mobility.
1. Encryption and authentication occur between the network and the user's SIM card to ensure security.


### Major Interfaces
1. Um (Air Interface)
- The most critical interface since it connects the user's device to the network wirelessly.
- Supports encryption, authentication, and radio resource management.

2. Abis Interface
- Connects the BTS and BSC.
- Handles control signals and traffic data, like call setup and management.

3. A Interface
- Connects the BSC to the MSC.
- Manages call routing, signaling, and mobility handling.



