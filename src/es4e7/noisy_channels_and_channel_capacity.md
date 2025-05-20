# Noisy Channels and Channel Capacity

## Noisy Channels
- Noise applied during discrete channel between the transmitter and receiver
- We assume:
  - **Stationary** Properties do not vary with time 
  - **Memoryless** properties do not vary with previsou symbols
  - **Synchronised** (we know which y maps to which x)
  
  ![alt text](imgs/noisy_channels_and_channel_capacity/image-7.png)

### Matrix Representation
- The channel can be represented as a matrix

![alt text](imgs/noisy_channels_and_channel_capacity/image-8.png)
- Calculate $p(y_j)$, $p(x_i|y_j)$ and Probability of error $P_e$

<!-- $$
% P_{YX} = \begin{bmatrix}
$$ -->
- Use Bayes theorem to calculate the probability of the output given the input
$$
p(y_i) = \sum_{j=1}^{M} p(x_i) p(y_j|x_i)
$$
$$
p(x_i|y_j) = \frac{p(y_j|x_i)p(x_i)}{p(y_j)}
$$
- Correctly received symbols:
  - $ p(y_0|x_0)$, $p(y_1|x_1)$ 
- Incorrectly received symbols:
  - $p(y_0|x_1)$, $p(y_1|x_0)$
  - 

### Binary Symmetric Channel
- Equal probabilities
- ![alt text](imgs/noisy_channels_and_channel_capacity/image-9.png)
- Gives the following ransition matrix
- ![alt text](imgs/noisy_channels_and_channel_capacity/image-10.png)
- Poor BSC
  - When the probabilies are poorly distributed
  - Choice of input distribtuion is cruicla
  - Cannot change the nature of the source but we can use an encode to modify the input probabilies
  - Need mathmatical tools to calculate the channels capabilitiy to convey infomration


### Pre Processing
- ![alt text](imgs/noisy_channels_and_channel_capacity/image-11.png)
- Preproecssor has the same noisy channel with the same binary input and nosie source
- Preporcessing stage has the input charactersitic Z -> Z_out prior to making it's estimate $\hat{X}$
- eg:
- ![alt text](imgs/noisy_channels_and_channel_capacity/image-12.png)
- ![alt text](imgs/noisy_channels_and_channel_capacity/image-13.png)

## Mutal Information
- Omniciscient outsider has more information that an observer at either end
- But outsider does not have more information that the sum of both ends
- Difference is the mutual information
$$
I(X;Y) = H(X) + H(Y) - H(X,Y) \\
I(X;Y) = \sum_{x,y} p(x,y) \lg \frac{p(x,y)}{p(x)p(y)} \\
I(X;Y) \geq 0
$$

- But if X and Y are independent, then ofcourse no information shared, $I(X;Y) = 0$

### Chain Rule
- $I(X;Y;Z) = I(X;Y) + I(X;Z|Y)$
or
$I(X;Y,Z) = I(X;Y) + I(X;Z|Y)$


### For BSC
- $I(X;Y) = H(X) - H(X|Y)$
- Symetric
- Therefore binary entropy function
$$
H(X) = -p \lg p - (1-p) \lg (1-p)
$$

Slide 35
