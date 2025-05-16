# Symbol and Stream Codes

Topics:
- Introduction
- Lossless Lossy Compression
- Symbol codes and Entropy encoders
- Fano Codes
- Shannon Codes
- **Huffman codes**
- **Arithmetic coding**
- **Obtaining probabilities**
  - **Laplace Estimator**
  - **Maximum Likelihood Estimator**
- **Sources with Memory**
- **Example of Dictionary Codes: Lempel- ZIV**

## Introduction
- Compression motivated by the need to imrpove:
  - Storage efficiency
  - Transmission bandwidth useage
  - Transmission time
- Compression enables more efficient use of exisitng resources, reducing costs

### Lossless Lossy Compression
- Lossless compression
  - No loss of information
  - Can be decompressed to the original data
  - Examples: Text, numeric data, source code
- Lossy compression
  - Loss of information (can be insiginificant details)
  - Cannot be decompressed to the original data
  - Compression ratio: tradeoff between quality and size
  - Examples: Audio, video, images
  

### Symbol codes
- In compressions codes created with expected lengths close to source entropy
- Means in general, codes are used for compression arent uniform


## Entropy Encoders
- Entropy encoders use simple algorithms to construct suitable Unique Decoding (UD) codes.
- Source Coding Tehroem - word k, prob p_k, it's lenght should be:
- $l_k  = - \lg p_k$
- But implementing directly is poor. 
- So use other algorithms


### Fano Code
- Top down approach
- Steps:
  - Arrange symbols in order of decreasing probability
  - Divide ordered list into two parts with the probabilities of each being as close to equal as possible
  - Assign the binary digit 0 to one side and 1 to the other
  - Recurisvily apply steps 2 and 3 until source is coded.
  - ![alt text](imgs/symbol_and_stream_codes/image.png)
  

### Shannon Code
- After ordering symbols in fano code, the ith code word with probability p_i is given by:
- $ F_i = \sum_{j=1}^{i-1} p_j$
- **(in binary form)**
- Number of positions in expansion limited to:
- $ l_i = \lceil -\lg p_i \rceil$

![alt text](imgs/symbol_and_stream_codes/image-1.png)


### Huffman codes
- Instead built form bottom up
- Steps:
  - Arrange symbols in order of decreasing probability
  - Combine two least proable into new node
  - if there is only one node left, stop Otherwise go to step 1
  - Draw tree and assign binary digits
  - ![alt text](imgs/symbol_and_stream_codes/image-2.png) 
![alt text](imgs/symbol_and_stream_codes/image-3.png)
- Often better than Shannon codes - Optimal to convey sequence of outcomes from fixed source one symbol at a time
- Disadvantage:
  - To deal with changing probabilities, have to adapt the data - causes problem for all codes
  - Fundemental problem arises with $H(x) \leq \bar{l} \leq H(X) + 1$
  - Overehead between 0 and 1 bit per symbol
  - Given entropy often small, thica n be signficuant - therefore **extending source!**

### Huffman Extension
- For sparsse soruce 
- ![alt text](imgs/symbol_and_stream_codes/image-4.png)
- Leads to artihmetic coding (to be feasible)

#### Obtaining probabilities
- Eg Simple biased coin:
  - p, 1-p
  - $ p = \frac{N_0}{N_0 + N_1}$
  - Maximum Likelihood Estimator (MLE) 
- Maximum a Posteriori (MAP)
  - Applies principle to estime p based on abserved data **and prior assumptions** 
  - $p = \frac{N_o + n_0}{N_0 + N_1 + n_0 + n_1}$
  - n_0, n_1 are imagined flips based on waht we know. Ie: for p = 0.6, 6 zeros and 4 ones. 
  - The larger the n, the slower it will converge when we are wrong.
- Laplace Estimator
  - MAP with n = 1
  - Absance of prior knowledge (assume equal probability)?
  - $p = \frac{N_0 + 1}{N_0 + N_1 + 2}$
 - $1-p = \frac{N_1 + 1}{N_0 + N_1 + 2}$  
 - Can be extented to more outcomes:

##### Laplace Estimator for N outcomes
$$
p_i = \frac{N_i + 1}{\sum_{i=1}^q(N_i + 1)} = \frac{N_i + 1}{\sum_{i=1}^N N_i + q}
$$