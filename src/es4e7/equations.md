# ES4E7 Equations
These are the equations that are useful but also those that need to be remembered for the exam.

<equation-table>

| [Equations to Know](#equations-to-know)                                 |                                                          |
|-------------------------------------------------------------------------|----------------------------------------------------------|
| [Decibels](#decibels)                                                   | $R_{dB} = 20 log_{10} (A_1/A_2) = 10 log_{10} (P_1/P_2)$ |
| [Log Properties](#log-properties)                                       | $\lg x = \frac{log_a x}{log_a 2} $                       |
| [General Probability](#general-probability)                             | $0 \leq P(A) \leq 1 $                                    |
| [Probability density function (pdf)](#probability-density-function-pdf) | $P(a \leq X \leq b) = \int_a^b p(x) dx $                 |
| [Expected Value Discrete](#expected-value-discrete)                     | $\mu = E[g(X)] = \sum_{i=1}^{n} g(x_i) P(X = x_i) $      |
| [Expected Value Continuous](#expected-value-continuous)                 | $\mu = E[g(X)] = \int_{-\infty}^{\infty} g(x) p(x) dx $  |
| [Linearity and Scaling](#linearity-and-scaling)                         | $E[ag(X) + f(X)] = aE[g(X)] + E[f(X)] $                  |
| [Varience](#varience)                                                   | $var(x) = E[(X-\mu)^2] = \sigma^2 $                      |
| [Linearity and Scaling](#linearity-and-scaling-1)                       | $var(cx) = [E[(cX-c\mu)^2] = c^2 var(X) $                |
| [Joint Probability](#joint-probability) | $p(x,y) = P(x|y)p(y) = P(y|x)p(x) $ | 
| [Conditional Probability](#conditional-probability) | $p(x|y) = \frac{p(x,y)}{p(y)} $ | 
| [Ttotal Probability](#ttotal-probability) | $p(x) = \sum_{i=1}^{n} p(x|y_i)p(y_i)  = \sum_{i=1}^n = p(x,y_i) $ | 
| [Marginalisation](#marginalisation) | $p(x) = \sum_j p(x|y_j) p(y_j)$ | 
| [Bayes Theorem](#bayes-theorem) | $p(y|x) = \frac{p(x|y)p(y)}{p(x)} $ | 
| [Shannon Information](#shannon-information) | $I(p) = -\lg p = \lg (\frac{1}{p}) $ | 
| [Discrete Entropy](#discrete-entropy) | $H(X) = \sum_{i=1}^{n} p(x_i) I(p(x_i)) = -\sum_{i=1}^{n} p(x_i) \lg p(x_i) $ | 
| [Binary Entropy](#binary-entropy) | $H_b(p) = -p \lg p - (1-p) \lg (1-p) $ | 
| [Continuous Entropy](#continuous-entropy) | $\lim_{\Delta x \to 0} H(X) = -\int_{-\infty}^{\infty} p(x) \lg p(x) dx - \lim_{\Delta x \to 0}  \lg \Delta x $ | 
| [Differential Entropy](#differential-entropy) | $h(X) = -\int_{-\infty}^{\infty} p(x) \lg p(x) dx $ | 
| [Joint Entropy](#joint-entropy) | $H(X,Y) = -\sum_{x,y} P(x,y) \lg P(x,y) $ | 
| [Conditional Entropy](#conditional-entropy) | $H(X|Y) = -\sum_{x,y} P(y) P(x|y) \lg P(x|y) $ | 
| [Mutual Information](#mutual-information) | $I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X) $ | 
| [Chain Rule](#chain-rule) | $H(X_1, X_2, \ldots, X_n) = H(X_1) + H(X_2|X_1) + H(X_3|X_1,X_2) + \ldots + H(X_n|X_1,X_2,\ldots,X_{n-1}) $ | 
| [Mean Length of a Code](#mean-length-of-a-code) | $\bar{l} = \sum_{i=1}^{n} l_i P(x_i) $ | 
| [Compression Ratio](#compression-ratio) | $\rho = \frac{\bar{l}}{\lg q}$ | 
| [Coding Efficiency](#coding-efficiency) | $\eta = \frac{ \min{\bar{l}} }{\bar{l} \lg q} = \frac{H(X)}{\bar{l} \lg q} $ | 
| [Kraft Inequality for Prefix Codes](#kraft-inequality-for-prefix-codes) | $\sum_{i=1}^{n} q^{-l_i} \leq 1 $ | 
| [Source Coding Theorem](#source-coding-theorem) | $\frac{H(X)}{\lg q} \leq \bar{l} \leq \frac{H(X)}{\lg q} + 1 $ | 
| [Binary Source Coding Problem](#binary-source-coding-problem) | $H(X) \leq \bar{l} \leq H(X) + 1 $ | 
| [Channel Capacity](#channel-capacity) | $C = \max_{p(x)} I(X;Y) $ | 
| [Maximum Channel Rate](#maximum-channel-rate) | $R(P_e) = \frac{C}{1 - H_b(P_e)}$ | 
| [Data Processing Inequality](#data-processing-inequality) | $I(U;f(V)) \leq I(U;V) => H(U|V) \leq H(U|f(V)) $ | 
| [Weight, EF and IOWEF](#weight-ef-and-iowef) | $A_{IOWEF}(X,Z) = \sum_{i=1}^{k} \sum_{w=0}^{|c|} a_{i,w} X^i Z^w $ | 

</equation-table>

<div class="equations">

## Equations to Know

#### Decibels
$$
R_{dB} = 20 log_{10} (A_1/A_2) = 10 log_{10} (P_1/P_2)
$$

#### Log Properties
$$
\lg x = \frac{log_a x}{log_a 2} \\

m \log x + \log y - \log z = \log \frac{x^m y}{z} \\

\frac{1}{x} = \frac{d(\ln x)}{dx} \\

e^{\ln x} = x \\

a^{\log_a x} = x \\

\log_a a^x = x
$$


### Probability

#### General Probability
$$
0 \leq P(A) \leq 1 \\
p(x) = dF(x)/dx \\

$$

#### Probability density function (pdf)
$$
P(a \leq X \leq b) = \int_a^b p(x) dx \\
\int_{-\infty}^{\infty} p(x) dx = 1 \\

$$

#### Expected Value Discrete
$$
\mu = E[g(X)] = \sum_{i=1}^{n} g(x_i) P(X = x_i) \\
$$

#### Expected Value Continuous
$$
\mu = E[g(X)] = \int_{-\infty}^{\infty} g(x) p(x) dx \\
$$

#### Linearity and Scaling
$$
E[ag(X) + f(X)] = aE[g(X)] + E[f(X)] \\
E[f(X)g(Y)] = E[f(X)]E[g(Y)] \\

$$

#### Varience
$$
var(x) = E[(X-\mu)^2] = \sigma^2 \\

E[X^2] = \int_{-\infty}^{\infty} x^2 p(x) dx \\
$$

#### Linearity and Scaling
$$
var(cx) = [E[(cX-c\mu)^2] = c^2 var(X) \\
x, y \text{ independent} \\
var(x+y) = var(x) + var(y) \\]
$$

#### Joint Probability
$$
p(x,y) = P(x|y)p(y) = P(y|x)p(x) \\
$$

#### Conditional Probability
$$
p(x|y) = \frac{p(x,y)}{p(y)} \\
$$

#### Ttotal Probability
$$
p(x) = \sum_{i=1}^{n} p(x|y_i)p(y_i)  = \sum_{i=1}^n = p(x,y_i) \\

f(x) = \int_{-\infty}^{\infty} f(x,y) dy \\
$$

#### Marginalisation
$$
p(x) = \sum_j p(x|y_j) p(y_j)\\
f(x) = \int_{y_{min}}^{y_{max}} f(x|y) f(y) dy \\
$$


#### Bayes Theorem
$$
p(y|x) = \frac{p(x|y)p(y)}{p(x)} \\
$$


### Entropy

#### Shannon Information
$$
I(p) = -\lg p = \lg (\frac{1}{p}) \\
$$

#### Discrete Entropy
$$
H(X) = \sum_{i=1}^{n} p(x_i) I(p(x_i)) = -\sum_{i=1}^{n} p(x_i) \lg p(x_i) \\
$$

#### Binary Entropy
$$
H_b(p) = -p \lg p - (1-p) \lg (1-p) \\
$$

#### Continuous Entropy
$$
\lim_{\Delta x \to 0} H(X) = -\int_{-\infty}^{\infty} p(x) \lg p(x) dx - \lim_{\Delta x \to 0}  \lg \Delta x \\ 
$$

#### Differential Entropy
$$
h(X) = -\int_{-\infty}^{\infty} p(x) \lg p(x) dx \\
$$


#### Joint Entropy
$$
H(X,Y) = -\sum_{x,y} P(x,y) \lg P(x,y) \\
= H(X) + H(Y|X)  = H(Y) + H(X|Y) \\
$$

#### Conditional Entropy
$$
H(X|Y) = -\sum_{x,y} P(y) P(x|y) \lg P(x|y) \\
$$

#### Mutual Information
$$
I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X) \\
$$

#### Chain Rule
$$
H(X_1, X_2, \ldots, X_n) = H(X_1) + H(X_2|X_1) + H(X_3|X_1,X_2) + \ldots + H(X_n|X_1,X_2,\ldots,X_{n-1}) \\
$$


### Coding

#### Mean Length of a Code
$$
\bar{l} = \sum_{i=1}^{n} l_i P(x_i) \\
$$

#### Compression Ratio
$$
\rho = \frac{\bar{l}}{\lg q}
$$

#### Coding Efficiency
$$
\eta = \frac{ \min{\bar{l}} }{\bar{l} \lg q} = \frac{H(X)}{\bar{l} \lg q} \\
$$


#### Kraft Inequality for Prefix Codes
$$
\sum_{i=1}^{n} q^{-l_i} \leq 1 \\
$$

#### Source Coding Theorem
$$
\frac{H(X)}{\lg q} \leq \bar{l} \leq \frac{H(X)}{\lg q} + 1 \\
$$

#### Binary Source Coding Problem
$$
H(X) \leq \bar{l} \leq H(X) + 1 \\
$$


### Other

#### Channel Capacity
$$
C = \max_{p(x)} I(X;Y) \\
$$

#### Maximum Channel Rate
$$
R(P_e) = \frac{C}{1 - H_b(P_e)}
$$


#### Data Processing Inequality
$$
I(U;f(V)) \leq I(U;V) => H(U|V) \leq H(U|f(V)) \\
$$


#### Weight, EF and IOWEF
$$
A_{IOWEF}(X,Z) = \sum_{i=1}^{k} \sum_{w=0}^{|c|} a_{i,w} X^i Z^w \\ 
$$


## Equations that Will be given
We still need to reconginise and understand these equations, but they will be given in the exam so we don't need to memorise them.


- Probability
  - Binomial distribution
  - Poisson distribution
  - Gaussian distribution
- Entropy
  - POME
  - ERFC approximation
  - Jensen's inequality
  - Relative Entropy / Kullback-leiber divergence/ Gibbs inequality
- Coding
  - Laplace Estimator
  - Markov Process
  - Bhattacharya parameter
  - BER bound / MLD bound for BER
  - DCT
  - SNR expressions
- Channel Capacity
  - Channel Capcity for various simple channels
  - Fano's Inequality   

</div>