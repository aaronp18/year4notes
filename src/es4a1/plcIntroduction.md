# PLCs Introduction

## Archiecture

#### What is a PLC?
- Programmable Logic Controller
- Industry computer to control / automate systems in real time
- Inventred by automotovie indsutry to replace dedicated relays

![alt text](imgs/plcIntroduction/image.png)

#### Designing PLC program steps
1) Undserstand the process
2) Define the variables to use (Addresses and Tags)
3) Design / build the ladder diagram
4) Run and verify the LD


### Memory Addressing (Tags)
- Global memory:
    - Inputs (I)
    - Outputs (Q)
    - Memory (M)
- Bits
  - Reference byte then bit
  - Example:
    - I1.6 = Input memomry, byte 1, bit 6

Different formats of displaying depending on manufacture
![alt text](imgs/plcIntroduction/image-1.png)

### Programming languages
- Ladder logic / diagram (LD) - Most commonly used
- Structured Text (ST) - More like C
- Function Block Diagram (FBD) - Graphical
- Sequential Function Chart (SFC) - flowchart like
- Instruction List (IL) - Assembly like

### Ladder Logic

![alt text](imgs/plcIntroduction/image-2.png)

![alt text](imgs/plcIntroduction/image-3.png)


### Scan Cycle
- PLCs run in a loop
- Read inputs
- Execute program
- Housekeeping diagnostics
- Write outputs
- Repeat

### Logic Functions

#### AND
- Both inputs must be true

![alt text](imgs/plcIntroduction/image-4.png)

#### OR
- Either input must be true


![alt text](imgs/plcIntroduction/image-5.png)

#### NAND
- Not AND
- Either output must be false

![alt text](imgs/plcIntroduction/image-6.png)

#### NOR
- Not OR
- Both outputs must be false

![alt text](imgs/plcIntroduction/image-7.png)

#### XOR
- Either input must be true, but not both
- Exclusive OR

![alt text](imgs/plcIntroduction/image-8.png)



#### Ladder Logic Advice
- Input instructions on the left
- Output instructions on the right
- Logic execute from left to right, top to bottom
- Outpiuts are written to memory first (and copied to actual outputs at teh end of the logic scan)
- Avoid duplicating outputs.
  - Output address should be referenced only once, otherwise the last output overwrites earlier settings
  - Avoid using negative coils as outputs
