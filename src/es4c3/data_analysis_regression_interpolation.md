# Data Analysis, Regression & Interpolation

## Equations

<equation-table>

| [Interpolation](#interpolation)                                                                              |                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [Linear Interpolation Formula](#linear-interpolation-formula)                                                | $y = y_0 + \frac{y_1 - y_0}{x_1 - x_0} (x - x_0)$                                                                       |
| [Taylor's Expansion Formula](#taylors-expansion-formula)                                                     | $f(x) = f(x_0) + (x-x_0)f'(x_0) + \frac{(x-x_0)}{2!}f''(x_0) + \ldots + \frac{(x-x_0)^n}{n!}f^{(n)} (x_0) + R_n =$      |
| [Newton's Divided-Difference Interpolating Polynomial](#newtons-divided-difference-interpolating-polynomial) | $f_n(x) = g[x_0] + g[x_1, x_0](x - x_0) + \ldots + g[x_n, x_{n-1}, \ldots, x_0](x - x_0)(x - x_1) \ldots (x - x_{n-1})$ |
| [Lagrange's Interpolation Polynomial](#lagranges-interpolation-polynomial)                                   | $f_n(x) = \sum_{i=0}^{n} L_i(x)f(x_i) = \sum_{i=0}^{n} L_i(x)y_i$                                                       |
| [Cubic Spline](#cubic-spline)                                                                                | Cubic polynomial approximates the data between two conseceutive data points                                             |

</equation-table>

<div class="equations">

## Interpolation

- Determining new data points within range of known data points
- Assumption: data is exact or error is small
- Task: find continuous function that fits data

### Linear Interpolation

- Straight line between two points
- Error can be large depending on given know values
- Use similar triangles to compute

#### Linear Interpolation Formula

$$
y = y_0 + \frac{y_1 - y_0}{x_1 - x_0} (x - x_0)

$$

![Linear interpolation image](imgs/data_analysis_regression_interpolation/image.png)

### Taylor's Expansion

Expanded around point $x_0$

#### Taylor's Expansion Formula

$$
f(x) = f(x_0) + (x-x_0)f'(x_0) + \frac{(x-x_0)}{2!}f''(x_0) + \ldots + \frac{(x-x_0)^n}{n!}f^{(n)} (x_0) + R_n =

$$

$$
f(x) = \sum_{k=0}^{n} \frac{(x-x_0)^k}{k!}f^{(k)} (x_0) + R_n

$$

Where $R_n$, Lagrange remainder

$$
R_n = \frac{(x-x_0)^{n+1}}{(n+1)!}f^{(n+1)}(x^*)  \quad x^* \in (x_0, x)

$$

Leads to polynomial:

$$
f(x) = p_0 + p_1x + p_2x^2 + \ldots + p_nx^n + R_n = \sum_{k=0}^{n} p_k x^k + R_n

$$

- $n+1$ data points **uniquely** n-th order polynomail
- Polynmoal describes data **exaclty** if in given data range, the function $f(x)$ can be represeted by nth order polynomial with $R_n = 0$
- $R_n$ is the error of the polynomial approximation

### Polynomial Interpolation

- $n+1$ data points
- Polynomial of degree $n$
- **unique** nth order polynomial can be calculated using *Newtons divided-difference interpolating polynomial*
- Can become highly inaccurate if using high-order polynomials. Overfitting
- Both:

  - Data points dont have to be equally spaced
  - Abscissa values dont need to be in ascending order
- Newtons Advantages

  - Expression of corefficients is recursive
  - Higher order differences are computed by taking differences of lower order differences
- Disadvantages

  - Small errors in data / low accuracy lead to error accumulation + propagation

#### Newton's Divided-Difference Interpolating Polynomial

$$
f_n(x) = g[x_0] + g[x_1, x_0](x - x_0) + \ldots + g[x_n, x_{n-1}, \ldots, x_0](x - x_0)(x - x_1) \ldots (x - x_{n-1})

$$

Where function gs are *finite divided differences*

#### Lagrange's Interpolation Polynomial

$$
f_n(x) = \sum_{i=0}^{n} L_i(x)f(x_i) = \sum_{i=0}^{n} L_i(x)y_i

$$

where

$$
L_i(x) = \prod_{j=0, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}

$$

Consdiered as **weighted average** of n values we are connectign by nth order polynomial

![alt text](imgs/data_analysis_regression_interpolation/image-1.png)

Example: See L2, slide 24

### Spline (piece-wise) interpolation

- Remedy for highly inacrruate high-order polynomials
- Use **low order piecewise** polynomials to connect data points
- Not unique (different end conditions)

#### Cubic Spline

Cubic polynomial approximates the data between two conseceutive data points

$$
f_i(x) = a_ix^3+b_ix^2+c_ix+d_i \quad x_{i-1} \leq x \leq x_i

$$

There are 4n unknowns, 4n equations so setup conditions

1. Each spline goes through 2 consecutive data points, first and last pass through end points
2. First derivative at the interior knots must be equal
3. Second derivative at the interior knots must be equal
4. Two (arbritary) end conditions

Alternative technique only requires n-1 linear alegebraic equations


- **Natural End Conditions** - Natural spline requires zero second derivative at the end points
- **Clamped End Conditions** - Clamped spline requires first derivative at the end points to be equal to a given value
- **Not-a-knot End Conditions** - To force continuity of the third derivates at the second and next ot last knots

![alt text](imgs/data_analysis_regression_interpolation/image-2.png)

**Resampling:**
- Often data sampled on irregular grid
- Therefore need redifining of regular grid
- Can use spline interpolation
- Matlab ODE solving, returns on non-uniform grid, so need to resample
- Use matlab `interp1` function

</>
