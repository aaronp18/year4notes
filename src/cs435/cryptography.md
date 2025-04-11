# Elementary Cryptography

<equation-table>

| [Classical Cryptography](#classical-cryptography) |                                                                                     |
| ------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [Modular Arithmetic](#modular-arithmetic)         |                                                                                     |
| [Data Range](#data-range)                         |                                                                                     |
| [Cipher](#cipher)                                 | Crypotgraphic algorithm to encrypt and decrypt data                                 |
| [Key](#key)                                       | Ysed for encryption and decryption                                                  |
| [Keyspace](#keyspace)                             |                                                                                     |
| [Cryptanalysis](#cryptanalysis)                   |                                                                                     |
| [Types of Attack](#types-of-attack)               |                                                                                     |
| [Confusion](#confusion)                           | Obscures the relationship between plaintext and cipher text - IE substituing        |
| [Diffusion](#diffusion)                           | Dissipates reducnecy of plaintext by spreading out over the cipher text. IE tran... |
| [Substitution Cipher](#substitution-cipher)       | Monoalphabetic: replace each letter with another letter                             |
| [Shift Cipher](#shift-cipher)                     | ERR                                                                                 |
| [Vigenere Cipher](#vigenere-cipher)               |                                                                                     |

| [Stream Cipher](#stream-cipher)     |     |
| ----------------------------------- | --- |
| [Perfect Secrecy](#perfect-secrecy) |     |
| [Recurrence](#recurrence)           |     |
| [Weakness](#weakness)               |     |

</equation-table>

<div class="equations">

## Classical Cryptography

### Quick Maths

#### Modular Arithmetic
- a, b integars, and m is positive integer
- $a \equiv b \mod m$ if m divides by b-a
- Phrase is called **congruence**
  - Read as "a is congruent to b modulo m"
- Integer m is called the **modulus** 

#### Data Range
- Some langauges define $a \mod m$ in the range of -m to m, but we define as always not negative.
- 

### What is Cryptography?
- Art and science of keeping information secure
- Classical Cryptography = based on characters - human 26 elements
- Modern Cryptography = based on binary - computer - 2 elements

#### Cipher
Crypotgraphic algorithm to encrypt and decrypt data

#### Key
Ysed for encryption and decryption

#### Keyspace
- Range of the kye

#### Cryptanalysis
- Analysis of weakenesses of cipher algorithms
- Attack
- Cryptology = Cryptograph + cryptanalysis


#### Types of Attack
- Ciphertext only
- Known plaintext
  - WW2, german ciphertext started with a data
- Chosen-plaintex
  - Breadking secret code
- Chosen-ciphertext
  - Job to deduce the key
  
#### Confusion
Obscures the relationship between plaintext and cipher text - IE substituing

#### Diffusion
Dissipates reducnecy of plaintext by spreading out over the cipher text. IE transposing plain text.


### Example Ciphers

#### Substitution Cipher
Monoalphabetic: replace each letter with another letter

Polyalphabetic: Made up of several monoalphabetic ciphers

![alt text](imgs/cryptography/image-1.png)

- K consists of all possible permuations.
  - Therefore the keyspace is $26!$ 
- But large key space does not mean secure
  - As can be broken by frequency analysis
  - Substitution ciphers only provide confusion, need both confusing and diffusion.

#### Shift Cipher
![alt text](imgs/cryptography/image.png)

- Not secure, can be broken by **exhaustive search**
- Only 26 possible keys
- One average 26/2 = 13 tried.

EG:
- Caesar Cipher
  - Shift each letter by a fixed amount
  - Key = shift amount
  - Keyspace = 26
  - Weakness: frequency analysis
- ROT13
  - Shift by 13
    - As can shift either direction to get back to original
  - Keyspace = 26
  - Weakness: frequency analysis


#### Vigenere Cipher
- Polyaphabetic cipher - based on combining few caesar ciphers into one.

**Cryptanalysis**:
- Two steps:
  - Find out the key length $m$
  - Find out each letter in teh key.

**Kasiki Test**
- First method, search for identical segments and count how many positions apart.
- IE: 15 positions apart, therefore key length is either 3 or 5.

**Index of Coincidence**
- Second method
- Index of coincidence of a string of characters is the probability that two randomly selected characters are the same.
- String of $n$ with 26 characters, the index of coincidence is:

![alt text](imgs/cryptography/image-2.png)

where occurrence of A = f_0, occurrence of b = f_1, etc.

- Normal Enlish text: 0.065
- Random text: 0.038
- Normal english text shifted by a fixed number: 0.038
- English text encrypted by vigenere cipher: ??

Then feed the text into matrix [n, m] where m is the guessed key length and find the index of coincidence for each column. Find the m that gives the result closest to 0.065

Then break each shift cipher. 

</div>

<div class="equations">

## Stream Cipher
- Encrpts individual characters one at a time.

### One Time Pad
- Simplest cipher with perfect secrecy
- 1917, Gilber Vernam

$$
c_i = k_i \oplus m_i
$$


#### Perfect Secrecy
- A crytosystem has perfect secrecy if $P(m|c) = P(m)$ 
- Probabily of plaintext given ciphertext is equal to the probability of plaintext.
- Therefore, the ciphertext does not give any information about the plaintext.
- Therefore one time pad has perfect secrecy. 
- However, perfect secrecy requires the size of the keylenght be larger than the message length.
- Hence why called one time.
- Thus "perfect" but impractical"

### Synchronous Stream Cipher
- Unable to recover from loss of synchronisation
- Idea: use a short secret key to generate a very long key stream
- Start with $m$ bits (k1, k2, k3 ... km)
- Then generate the key stream using a linear recurrence of degree m.

![alt text](imgs/cryptography/image-3.png)

- Can be produced with **Linear Feedback Shift Register (LFSR)**
  
  ![alt text](imgs/cryptography/image-5.png)

#### Recurrence
- After a period, the same key stream will recurr.
- And using the same key twice, can be broken.
  
![alt text](imgs/cryptography/image-4.png)

#### Weakness
- Example
  - CSS: Content Scrable System
  - Used in DVDs, to prevent piracy
  - 40 bit key
  - But only 16 bits for security
  - So can break
    - Try all 17 bit LFSR to get 20 bytes output
    - Subtract from the first 20 bytes of stream output
    - If consistent with the 25-bit LFSR, then found the key.
  - Security through Obscurity doenst work 

### Self-synchronising Stream Cipher
- Able to recover from loss of synchronisation


## Block Cipher

### Overview

#### Basic structure
![alt text](imgs/cryptography/image-6.png)

#### Iterated Construction
![alt text](imgs/cryptography/image-7.png)
Where R(K_x,. ) is a round function, K is the key, and n is the number of rounds.
- DES 16 rounds, 3DES 48 rounds, AES128 10 rounds

DES = Data Encryption Standard

### Functions

#### Pseudo Random Function (PRF)
- Defined over (K, X, Y)
- $F: K \times X \to Y$
- Such that:
  - Exists an "efficient" algorithm to evaluate F(k,x)

#### Pseudo Random Permutation (PRP)
- Defined over (K, X)
- $E: K \times X \to X$
- Such that:
  - Exists an "efficient" algorithm to evaluate E(k,x)
  - The function E(k,.) is **one to one**
  - Exists an efficient inversion algorithm D(k,.)


A PRP is a PRF where:
- X=Y
- It is invertible

### Fiestel Network
- Need better efficiency
- Can we use the same circuit for both Encrypting and decrypting?
![alt text](imgs/cryptography/image-8.png)

![alt text](imgs/cryptography/image-9.png)

#### Invertible Design
- Can do the inverse operation by swapping L and R
  
![alt text](imgs/cryptography/image-10.png)

On the last round, dont swap the left and right sides, so the decruption can be applied without swapping them.


### DES 16 Round Fiestel Network
![alt text](imgs/cryptography/image-11.png)

![alt text](imgs/cryptography/image-12.png)

- 32 bit input pddeded to 48 bits
- Padded inpit added to the key
- Input divided into 8 groups of 6 bits of input sent to S boxes (look up tables)
  - $S_i: \{0,1\}^6 \to \{0,1\}^4$
  - Take row corresponding to the outer 2 bits and the column corresponding to the inner 4 bits, and find where they intersect.
  - Provides confusion. 
![alt text](imgs/cryptography/image-13.png)

- P box - defines permutation over 32 bits
  - $P: \{0,1\}^{32} \to \{0,1\}^{32}$
  - Provides diffusion
  - ![alt text](imgs/cryptography/image-14.png)


- Choosing S and P boxes
  - Choosing random = results in insecure block cipher
  - No ouput bit should be close to a linear function of the input bits
  - S-Boxes are 4-1 mapping


### More Secure DES
- 56 bit DES is too weak - can be brute forced

#### Double DES
- Encrypt twice, with 2 keys
- Double key = 112 bits
- $c = E(k_2, E(k_1, m))$
![alt text](imgs/cryptography/image-15.png)
- But vulnerable to meet in the middle attack - knowing a few (m, c) pairs

![alt text](imgs/cryptography/image-16.png)


#### Triple DES
- More secure combination
- Few varients:
  - $k_1 \neq k_2 \neq k_3$ - keysize of 168 bits, security 112 bits
  - $k_1 = k_3$ - keysize of 112 bits, security 80 bits
  - $k_1 = k_2 = k_3$ - keysize of 56 bits, security 56 bits