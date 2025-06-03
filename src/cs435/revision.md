Revision Part 1: Cryptography

1. Classical crypto

Understand the four types of attacks considered in classic cryptanalysis
Understand the working of the shift cipher, substitution cipher and how they are broken
Understand the working of the Vigenere cipher, and able to elaborate steps to break this cipher, using the Kasiski test and the index of coincidence

2. Stream cipher

Understand the definition of “perfect secrecy” and the proof for one-time pad
Understand the two-time pad attack against the one-time pad, and why it works
Understand the relation between one-time pad and stream cipher
Understand how the stream cipher used in DVD CSS is broken

3. Block cipher I

Able to draw the Feistel Network for DES (sufficient for drawing one round)
Understand the invertible design of Feistel Network and why it’s invertible
Understand the brute-force attack against DES and work factors
Understand the weakness of using double encryption in DES and why it can’t
provide the expected 112-bit security
Able to elaborate Triple DES and its variants with respective security levels

4. Block cipher II

Understand the basic difference between DES and AES designs (no need to memorize details in AES)
Able to draw the modes of operation for ECB, CBC, CFB, OFB and CRT
Understand why ECB is insecure
Understand the padding scheme for CBC: when to add pad, and when to remove it.
Understand the properties of CBC, CFB, OFB and CRT in terms of parallelism, recovery of error and synchronization.

5. Hash

Understand the theoretical abstraction of hash as a random oracle
Understand the practical requirements for designing a secure hash
Understand the birthday paradox and its implication on the hash design
Understand why collision in the hash is dangerous
Able to draw the Merkle-Damgard construction, and able to prove the theorem
Understand the Davies-Meyer construction in building a compression function
Understand applications of hash, in particular, for protecting the passwords and mining cryptocurrencies

6. MAC

Understand the definition of a secure MAC
Able to elaborate on how to use MAC to protect the integrity of OS files
Able to describe how to construct a MAC using CBC
Understand why H(k, m) is not a secure construction
Understand the timing attack against the HMAC implementation in the (old) Keyczar library and able to describe countermeasures
Understand the importance of authenticated encryption and able to describe how the encryption-only mode in IPSec can be broken

7. Key agreement


Understand how the Merkle Puzzles scheme works and the complexities
Understand how the Diffie-Hellman key exchange works and the complexities
Understand the difference between passive and active attacks, and how the Diffie-Hellman protocol can be broken by an active attacker.
Understand that the Diffie-Hellman protocol is unauthenticated, and addressing the active attack requires an “authenticated” key exchange protocol
Understand the attacks against EKE and SPEKE

8. Public key encryption (*)

Able to describe the textbook RSA encryption scheme including key generation, encryption, and decryption
Understand why the textbook RSA encryption is insecure and able to elaborate attacks

9. Digital signature

Understand the definition of a secure digital signature and the difference from MAC
Able to describe the textbook RSA signature scheme 
Understand the attacks against the textbook RSA signature scheme
Able to describe the Schnorr identification scheme and the Schnorr signature scheme
Understand why the Schnorr identification scheme satisfies the completeness, soundness and zero-knowledge properties
Understand the importance of the random number being random in Digital Signature Standard



Revision Part 2: System Security


1. Security basics

Understand the CIA triad
Understand different types of threats
Able to organize threats into an attack tree
Understand the difference between security engineering and other engineering disciplines

2. Users and security

Understand the importance of knowing users in security
Understand how phishing attacks work and what human weaknesses are exploited
Able to elaborate defense against phishing attacks, and limitations
Understand what CAPTCHA is for, why it is invented, and the difference between the Turing test and CAPTCHA
Understand various attacks against CAPTCHA and why they worked

3. Software security - buffer overflow

Understand stack layout (text, data, BSS segments, heap, stack)
Understand how the frame pointer (ebp) is used to indicate memory address
Understand steps of injecting malicious code in buffer overflow
Able to describe two techniques to improve the chance of successfully jumping to malicious code (filling NOP, spraying RT)
Understand how the StackGuard works and why it works

3. Software security - format string vulnerability

Understand how printf() works with a format string and optional arguments
Understand the root cause for the format string vulnerability (user input can’t be trusted to be used as a format string)
Able to describe how an attacker may use format string vulnerability to print data on the stack
Able to describe how an attacker may use format string vulnerability to overwrite data in memory

Can the StackGuard technique be used to prevent the format string vulnerability?

3. Software security - Race condition

Able to describe a TOCTTOU attack with an example
Understand the Set-UID Concept (real vs effective UID)
Able to describe how Set-UID works, e.g., passwd
Able to describe how to use race condition to write to passwd
Understand the magic string in passwd:
test:U6aMy0wojraho:0:0:test:/root:/bin/bash

4. Web security - cross-site request forgery

Understand the difference between same-site and cross-site requests
Understand how the cookie is often used in maintaining authentication
Able to describe how a CSRF attack works GET/POST requests
Understand the fundamental course of CSRF
Understand the countermeasures against CSRF and limitations (referrer header, same-site cookie, secret token)

4. Web security - cross site scripting (XSS) attack

- Understand the difference between CSRF and XSS
- Able to distinguish non-persistent (reflected) vs persistent XSS attacks
- Understand how an XSS worm can self-replicate
- Understand the fundamental problem in XSS (mixing up code and data)
- Able to describe countermeasures (filtering, encoding, CSP)
- 
- Can the Secret Token used to prevent CSRF also be used to prevent XSS?

4. Web security - SQL injection

- Understand the use of SQL comment (#) in SQL injection
- Understand the use of special words (OR, DROP) in SQL injection
- Understand the fundamental cause (mixing data and code)
- Understand filtering/encoding based countermeasures
- Understand Prepared Statement countermeasure
  
To prevent SQL injection, a developer implements a filter at the client web page
using Javascript to remove any special character found in the entered data, such
as apostrophe, characters for comments, and keywords reserved for SQL
statements. Is this an effective countermeasure?

1. Network Security - Packet sniffing and spoofing

- Understand the promiscuous mode for NIC
- Understand the monitor mode for Wi-Fi (concepts of channels)
- Understand how to spoof a packet and why root privilege is needed

6. Network security - TCP attacks

- Understand TCP 3-way handshake protocol
- Understand SYN flood attack how it exhausts the TCB queue
- Understand SYN cookie and how it addresses the SYN flood attack
- Understand TCP reset attack
- Understand TCP session hijacking attack

6. Network security - Firewall

- Understand the goal of a firewall
- Understand three types of firewalls (packet filter, stateful, proxy)
- Able to describe ways to evade a firewall (ssh, VPN)

6. Network security - DNS attacks (*)

- Understand how DNS works
- Understand DNS attacks at different points and their effects (local DNS files, local DNS server and DNS authoritative server)
- Understand local DNS cache poisoning attack
- Understand the challenge of remote DNS cache poisoning attack and how the Kaminsky attack overcame it
- Understand DNS rebinding attack and how it can bypass the same-origin policy



