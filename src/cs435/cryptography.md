# Elementary Cryptography

<equation-table>

| [Classical Cryptography](#classical-cryptography) |                                                                                     |
|---------------------------------------------------|-------------------------------------------------------------------------------------|
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

| [Stream Cipher](#stream-cipher)     |   |
|-------------------------------------|---|
| [Perfect Secrecy](#perfect-secrecy) |   |
| [Recurrence](#recurrence)           |   |
| [Weakness](#weakness)               |   |

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