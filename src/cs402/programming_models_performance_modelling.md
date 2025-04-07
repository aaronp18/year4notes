# Programming Models & Performance Modelling

## Performance, Protability, Productivity
- Comparing different paralllisim methods is diifficult
  - How does it affect compile time
  - How does it affect runtime
  - How does it trnaslate between different hardware software model
  - What is the overhead / cost to utilisng a prallesiation model
  - How easy is it to develop in
  - How easy is it to incorporate into already exisisin code

### Performance Portability
> A measurement of an aplications performance efficiency for a a given problem that can be executed correctly on all platforms in a given set.
- Application effiicency = achieved time / fastest time
- Archiecture efficiency = Achieved GLOPS / Theoretical peak GLOPS
    - Or memoery bandwidth efficiency

$$
P(a,e,H) = \frac{|H|}{\sum_{i\in H} \frac{1}{e_i(a,p)}} 
$$

- If $i$ is supported $\forall i \in H$ otherwise $P(a,e,H) = 0$
- $H$ is a set of platforms
- $a$ is the application
- $p$ is the parameters for a
- $e$ is the performance efficiency measure
