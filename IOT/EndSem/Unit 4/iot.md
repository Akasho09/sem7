## 1. Introduction to Internet of Things (IoT)
- The Internet of Things refers to a network of physical objects (“things”) embedded with sensors, software, and connectivity that enable them to collect, exchange, and act on data.
- Devices communicate with each other without human intervention, creating smart environments.

### IOT :
- “A dynamic, global network infrastructure where physical and virtual objects have unique identities, can communicate using standard protocols, and have the ability to sense, process, and exchange data.”

#### Key ideas:
1. Devices (“things”) are identifiable.
2. They connect and communicate autonomously.
3. They sense the environment and act on data.

## IOT componenets :
1. Sensors and Actuators :
- These are the “things” in IoT that collect data.
- They monitor physical conditions of the environment.
- atuators are used to give output like led or motor etc.
- Types of sensors:
Temperature sensor
Motion sensor
Light sensor (LDR)
Humidity sensor
Gas sensor
Pressure sensor
Proximity sensor

2. Connectivity :
- wired or wireless 
![](image.png)

3. IOT Cloud or 

4. IOT Analytics and data Management / Data Processing

5. User interface .

## 3. Characteristics of IoT
1. a) Connectivity
Devices connect through WiFi, Bluetooth, Zigbee, 5G, etc.

2. b) Sensing
Sensors collect real-time data (temperature, motion, humidity, etc.).

3. c) Intelligence
Devices analyze data (local or cloud-based) to make decisions.

4. d) Scalability
IoT networks can support millions of devices.

5. e) Heterogeneity
Different devices, platforms, and technologies work together.

6. f) Interoperability
Different manufacturers’ devices can exchange data using standard protocols.

7. g) Security
Ensuring confidentiality, integrity, and authentication of data.


### 4. IoT Standards
- IoT needs global standards to ensure interoperability. Major standard bodies include:

1. a) IEEE
Standards for communication (e.g., 802.15.4 for low-power networks).

2. b) IETF
Protocols like IPv6, 6LoWPAN, CoAP.

3. c) ITU-T
Global telecom standards for IoT architecture.

4. d) ISO/IEC
Security and device management standards.

5. e) OneM2M
Standard for machine-to-machine (M2M) communication.

## 5. IoT Protocols
Protocols define how devices communicate.
They operate at different layers:

1. a) Application Layer Protocols
- MQTT – lightweight publish/subscribe protocol for low-power devices.
- CoAP – for simple devices over UDP.
- HTTP/HTTPS – used when web communication is required.

2. b) Network Layer Protocols
- IPv6 – large address space.
- 6LoWPAN – IPv6 over low-power wireless networks.

3. c) Communication/Link Layer Protocols
- WiFi – high bandwidth.
- Bluetooth / BLE – short-range communication.
- Zigbee – mesh networking for low-power sensors.
- NFC – very short range.
- LoRaWAN – long-range, low-power communication.


## 6. IoT Communication Models
- These represent patterns of how data flows between devices.

1. a) Device-to-Device (D2D)
Devices communicate directly (e.g., Bluetooth).

2. b) Device-to-Cloud (D2C)
Devices send data to cloud servers for storage/processing.

3. c) Device-to-Gateway (D2G)
Device communicates with a gateway, which then connects to the cloud.

4. d) Back-End Data Sharing Model
Cloud data is shared among multiple servers or analytics platforms.

## 7. IoT Communication APIs
- APIs allow IoT devices and applications to exchange data.

1. a) RESTful APIs
- Use HTTP (GET, POST, PUT, DELETE) for communication.

2. b) WebSocket API
For real-time, two-way communication (live IoT dashboards).

3. c) MQTT APIs
Publish–subscribe communication between devices and brokers.

4. d) CoAP APIs
Lightweight API using request–response over UDP.

5. e) Vendor-specific APIs
APIs provided by cloud platforms such as:
AWS IoT
Azure IoT Hub
Google Cloud IoT

## 8. IoT Applications
1. A. Home (Smart Home Applications)
- Smart homes use IoT to automate household activities.

Examples:
- Smart lighting
- Smart thermostats
- Smart locks
- Voice-controlled assistants
- Energy management

2. B. City (Smart City Applications)
- IoT makes cities more efficient and livable.

Examples:
Smart traffic management
Smart streetlights
Smart waste management
Smart parking systems
Public safety and surveillance