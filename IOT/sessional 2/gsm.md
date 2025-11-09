## 


##  Channels used in GSM 
| Type                      | Purpose                                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **1️⃣ Physical Channels** | Actual radio frequencies and time slots used for transmission                                                   |
| **2️⃣ Logical Channels**  | Functional divisions of information (like signaling, control, and user data) carried over the physical channels |

1. Physical Channels
- A physical channel in GSM is defined by:
 - A carrier frequency (200 kHz bandwidth)
 - A time slot within a TDMA (Time Division Multiple Access) frame
- Each GSM carrier supports 8 time slots — numbered TS0 to TS7 — forming 8 physical channels.
- 🕒 Frame duration: 4.615 ms
- ⏱ Slot duration: 577 µs
- Each slot can carry one logical channel (e.g., voice or signaling).

2. Logical channels 
- are the different types of data or signaling information transmitted over the physical channels.
| Category                      | Purpose                                    |
| ----------------------------- | ------------------------------------------ |
| **A. Traffic Channels (TCH)** | Carry **user data (voice or SMS)**         |
| **B. Control Channels (CCH)** | Carry **signaling and system information** |

- types : 

1.  Traffic Channels 
    - Traffic channels are used for carrying user information like voice, SMS, or data.

    | Type                      | Description                      | Data Rate          |
    | ------------------------- | -------------------------------- | ------------------ |
    | **Full-Rate TCH (TCH/F)** | Carries one full voice call      | 13 kbps            |
    | **Half-Rate TCH (TCH/H)** | Two users share one time slot    | 6.5 kbps each      |
    | **TCH/Data**              | For circuit-switched data or fax | 2.4, 4.8, 9.6 kbps |

2. Control Channels (CCH)
Control channels manage network access, synchronization, and handover.
They are divided into three main types:
- 1️⃣ Broadcast Channels (BCH)
 - Used by the base station (BTS) to broadcast information to all mobiles in the cell.
| Channel                            | Function                                                               |
| ---------------------------------- | ---------------------------------------------------------------------- |
| **FCCH (Frequency Correction CH)** | Helps mobile tune to BTS frequency                                     |
| **SCH (Synchronization CH)**       | Provides timing and frame synchronization                              |
| **BCCH (Broadcast Control CH)**    | Broadcasts cell info (e.g., network ID, cell ID, frequency list, etc.) |

- 2️⃣ Common Control Channels (CCCH)
Used for communication between the mobile station (MS) and the base station (BTS) during call setup.
| Channel                          | Function                                      |
| -------------------------------- | --------------------------------------------- |
| **PCH (Paging Channel)**         | Used by BTS to alert mobile for incoming call |
| **RACH (Random Access Channel)** | Used by mobile to request access (uplink)     |
| **AGCH (Access Grant Channel)**  | BTS assigns a dedicated channel to mobile     |

- 3️⃣ Dedicated Control Channels (DCCH)
 - Used after a channel is assigned — to manage an active connection.
| Channel                                          | Direction       | Function                                                |
| ------------------------------------------------ | --------------- | ------------------------------------------------------- |
| **SDCCH (Standalone Dedicated Control Channel)** | Uplink/Downlink | Used for call setup, location update, authentication    |
| **SACCH (Slow Associated Control Channel)**      | Uplink/Downlink | Sends periodic info like signal strength, power control |
| **FACCH (Fast Associated Control Channel)**      | Uplink/Downlink | Carries urgent signaling (e.g., during handover)        |
- 🧠 Note: FACCH temporarily steals a traffic channel slot (TCH) when needed for fast signaling.

- 
![alt text](image-3.png)