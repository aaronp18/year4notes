# Sensors

## Temperature Microsensors
- Silicion widely used
- Most temperaure sensosr based on dependence of base-emitter voltage of bipolar transistors
  - (Bipolar tends to have higher sensitivity than MOSFET)
- Thermal sensosrs are also used to indirectly measure non-thermal proepries (velocity of air flow)
- Temperature dependence of silcion is undesirable
  - Therefore temperature dependence intensivly studied, well udnerstood and compensated for
  - Most MEMS device have temp compensation as control
  - ise expensive, need heating /cooling system such as fan or Peliter
- Therefore 2 catagories:
  - Self-generating: Needs no external power source, since it uses the signal as power source (eg thermocouples)
  - Modulating: Needs external power srouce (eg resistors, diodes and transistors)

![alt text](imgs/sensors/image-5.png)

### Classification
![alt text](imgs/sensors/image.png)

### Thermocouple
- Basic principle: Seebeck effect
- 2 conductors joined together at one point
- Temperature difference obtained between joined and non joined parts
- Open circuit voltage measured
  - Very high input impedance 
- ![alt text](imgs/sensors/image-1.png)

**Advantages:**
- Low cost
- Mecahnical stability
- Wide temperature range (-200 to 2000C)
- Reasonable accurace (+- 2.2C)

**Disadvantages**
- Low sensitivity (uV/C)
- Requires known temperature reference
- Requires periodic calibration

### Thermopile
![alt text](imgs/sensors/image-2.png)
- Population of thermal coples togheter
- Used to measure the seebeck effect in silicion
- Narrow p-type stripes made by ion implantation or diffiusion in an n-type epitaxial layer
- Strips connected by evaporated aluminum strips
- ![alt text](imgs/sensors/image-3.png)

**Advantages**:
- Easy to fabricate
- Hgih sensitivity 1mV/K
- Excellent resolution, 1-10uK

**Disadvantages**
- large thermal conductitvy ofsilicon causes probles as it is more difficul to create temperature difference on chip
- Problem can be solved with resistor on chip
- Noisy so set to 50kOhms for lower Johnson noise.



### Thermistor
- Low cost temperature sensitive resistors
- Constructed of solid semiconductor materials that have postive or negative temperature coefficient
- Solid Sate semiconductor device
- Positive Temperature Coefficient (PTC) thermistors
  - increases resistance with increasing temperature
- Negative Temperature Coefficient (NTC) thermistors 
  - decreases resistance with increasing temperature 
  - Tends  to have  large resistance range so easy to measure
- R to T relationship is non-linear
  - Very steep slope
  - Increase sensitivity of the device
  - Resistance change +- 3% /C
  - Limits range of operation
![alt text](imgs/sensors/image-4.png)

**Advantages**
- Low cost
- Very sensitive (10x more than RTDs (PT100 etc) )
- High accuracy (+-0.02C)
- Stable / reliable / repeatable

**Disadvantages**
- Limited operating range (-100 to 150c)
- Very non linear


### RTD (Resistance Temperature Detector)
- Typically platinum wire wrapped around ceramic bobbin. 
- More accurate and more linear over wider range than thermocouple and thermistor


### Silicon n-p Diode as temperature Sensor
- Usually diodes are forward biassed when used as temperatre sensosr
- Between -40 to 125 almost linear behaviour
- Keep bias current low to avoid heating but enough to overcome noise.

![alt text](imgs/sensors/image-6.png)

### Thermotranistor Circuit
- Transistor make more accurate temperature sensors than diodes
- Use of transistor based on Ic-Vbe characteristics
- npn less noisy than FET
- ![alt text](imgs/sensors/image-7.png)
- 

## Mechanical Microsensors

Measurands:
- Angular velocity
- Acceleration
- Force (torque)
- Pressure
- Flow Rate
- + others that we don't cover


### Mechanical Transduction Principles
- Piezo resistive
  - Common, resistence changes with appried pressure or straing
  - Cheap
- Piezoelectric
  - Generate charge from surface when external force
- Capacitive
  - Charge based on capacitance / change of capacitance
  - Low power consumption
  - Simple and easy to fabricate
- Optical
  - Modulating properties of optical wave
  - Multiple properties to alter and measure
- Resonantors / Moving mass
  - Vibrate at fixed freuqency

#### Piezoreisistivty
- Measures change in resistance to applied pressure or strain
- Metal foil
- Sensitivity defined by gauge factor (GF)
- Ristance changed / applied strain, $\epsilon$
  - $GF = \frac{\Delta R / R}{\Delta L / L} = \frac{\Delta R / R}{\epsilon}$ 
![alt text](imgs/sensors/image-9.png)
- ![alt text](imgs/sensors/image-8.png)    
- Fairly cheap

#### Piezoelectric
- Materials generate electric charge when mechanical stress is applied
- Occur due to charge assymetry in the crystal lattice
- Hence have anisotropic properties
- can be used for oscillators / resonators
- At *Curie Temperature* (usually very high), loses its properties
- Voltage produced from rectangular block of Area A, thicknes t, Charge Q, capactiance C and relative permittivity $\epsilon_r$
- $V = \frac{Q}{C} = \frac{dFt}{\epsilon_o \epsilon_r A}$
- High input impedance required (as large currents cannot be drawn)
- ![alt text](imgs/sensors/image-10.png)
- ![alt text](imgs/sensors/image-11.png)
- Could use to cause movement, but nto very common as need high voltages and only give micron displacements


#### Capacitive
- Physical structure very simple and easy to fabricate in MEMS
- Gives presice means of measuring movement
- Charge based device, therefore low power consumption
- ![alt text](imgs/sensors/image-12.png)
- Variable cap - Vertical motion
- Variable area - Horizontal motion
- Variable dieletric constant - dieletric material moves

$$
C = \frac{\epsilon_o \epsilon_r A}{d}F
$$
- Can be non linear
- As A, d, $\epsilon$ are temperature dependent, need to be careful
- Therefore use differential capacitance senosr (temperature affects both capacitors, therefore cancels out)
- ![alt text](imgs/sensors/image-13.png)

#### Optical
- rely on modulating the properties of an optical wave
- Typical microsensors interact with the measurand and usually do not have integrated optical components
- Can alter:
  -  Intensity
  -  Phase
  -  Wavelenght
  -  Spatial Position
  -  Frequency
-  
##### Variation in Light Intensity
- Simply measure change in light signal by optical sensor (eg photodiode)
- Optical soruce usually LEd
- Temperautre and humidity can affect the output
- ![alt text](imgs/sensors/image-14.png)
  
##### Variation in Spatial Position
- used for triangulation
- ![alt text](imgs/sensors/image-15.png)

##### Variation in Freuqneyc
- Measures changes in freuqency of a wave contacting a moving body
- Dopper frequency shift to measure velocity of target


#### Resonance
- Vibrate at fixed frequency ($f = \frac{1}{2\pi} \sqrt{\frac{k}{m}}$)
- Extremely stable
- Measurand typically modifies:
  - Stiffness, Mass and Shape of resonator (hene frequency)
- Resonance peaks at sepcific frequency - magnetigute will be limited by damping effects
- Quality factor Q - defines sensitivity
  - $ Q = 2\pi \frac{E_m}{E_C} $ where Em is energy stored, EC is energy lost per cylce
- possible microsensor resonantor structures based on multiple beasms
  - Double ended tuning fork (DETF)
  - Triple beam tuning fork (TBTF) 
- ![alt text](imgs/sensors/image-16.png)

#### Q-Factor
- high Q factor - shows structure isolated from surroudnings
- Q factor controlled by many parameters
- EG:
  - Energy lost to surrounding fluiod = $1/Q_a$
  - Energy coupled through resonator supports = $1/Q_s$
  - Energy lost to internal damping = $1/Q_i$
  - $1/Q = 1/Q_a + 1/Q_s + 1/Q_i$
- $Q_a$ usually largest
- Below 100 Pa, moelcules behave independently exchanging momentum with the resonator
- Above 100 Pa behaves as a fluid, hence viscous drag dominates
- 