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

##### Variation in Frequency
- Measures changes in frequency of a wave contacting a moving body
- Doppler frequency shift to measure velocity of target


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


## Mechanical Microactuators

Classification:
- Linear displacement
- Angular displacement
- Linear acceleration
- Angular acceleration
- Apply force or torque
- Apply Stress/ Load

### Actuating Principles
- Principles:
  - Electromagnetic
    - Not MEMS - difficult to make efficient and small
  - Electrostatic
    - Two plates opposite charge attact each other
    - Simple
    - Comb drive, Scratch drive
  - Thermal
    - More power, but more force
    - Expansion of bmaterials
    -  
  - Piezoelectric
    - Sensor and actuator
    - Mecahnical amplifciation from small movement
    - Piezopumps
  - Vibration and Noise


- Actuator translates an electrical signal to mechancial movement (output transducer)
- Noramlly only 5% to 35% efficient
- Factors:
  - Fabrication, robustness, resistance to external forces (temperature humidity), range of motion

### Electorstatic Drive
- Very common in MEMS
- Fundemental principle of electrostatic attraction of oppositely charged plates
- Relatively straight forward to fabricate (parallel plate cpacitor)
- Non linear
- Energy stored depends on gap
- ![alt text](imgs/sensors/image-17.png)     


#### Electrostatic Comb Drive
- Common to use comb drive
- Better surface area, therefore more force and more motion
- Multuiple fingers with small thickness compared to width
- Lateral movement with fixed electrode and moving electrode
- Gap doesnt change, it's the surface area that changes

![alt text](imgs/sensors/image-18.png)


#### Elecrostatic Scratch Drive
- Alternative format
- Flexible electrode plate and small bushing
- When voltage applied, plate buckles
- Causes electrode to scratch along insulator cuaisng motion
- Voltage cyclee to produce regular movement
![alt text](imgs/sensors/image-19.png)


### Piezo Eletirc Cantilever
- Used as sensor and actuator
- Small movement requires mechanical amplification
  - Effect is small, requires large voltage
- Can deposit pizeolectric onto cantilevers to create unimorph
- Hecne deflection of the free end is greater than produced film
- ![alt text](imgs/sensors/image-20.png) 

#### Piezoelectric Pumps
- common in micro pumps
- 2 silcion wafers one with etches with inlet and outlet, other etched to form membrane coated with piezoelectric material
- Hence combination forms a pump
![alt text](imgs/sensors/image-21.png)

### Thermal Drive
- Differential thermal expansion
- Consumes more power but produces more force
- Creates stress at interface, hence moevment
- ![alt text](imgs/sensors/image-22.png)

### Mechanical Structures and Key Design parameters
![alt text](imgs/sensors/image-23.png)

### Micromechanical Scaling
- Micron size structures
- Laws of mechancics dont necessarily apply
- Depends on physical principle
- Ideally microstructures should designed so that linear theories of mechanics apply

#### Silicon
- Silicon has excellent properites
- Processed conveiently
- Can combine to make microsensors / actuators
- Precise reliable
  - Youngs modulus similar to steel
  - Brittel
  - CAnnot deform plastically

### Microhmehcanil Structures
- Cantilever beam
- Bridge
- Diaphragm
-  ![alt text](imgs/sensors/image-24.png)
-  
![alt text](imgs/ensors/image-25.png)

![alt text](imgs/sensors/image-26.png)

![alt text](imgs/sensors/image-27.png)


## Inertial MEMS Sensors
- Group of MEMS senosrs include accelerometers (linear) and gyroscopes (angular)
- Used in lots of applications
- Some need different bandwidths, resolutions, ranges
- ![alt text](imgs/sensors/image-28.png)

### Principles of Operation
- Proof mass attached to mechanical suspension system
- Any interial force due to acceleration will deflect proof mass
- Effectibly mass-spring-damper system - second order damped harmonic oscillator
- Can be used to measure acceleration or angular velocity
- ![alt text](imgs/sensors/image-29.png)


### Sensing Principles:
- Capactive
![alt text](imgs/sensors/image-30.png)
- Dispalcement sended by electrosatic (capacitive) sensor
- With fixed bias voltage, a change in charge of the capaciro can be measured
- ![alt text](imgs/sensors/image-31.png)
- ![alt text](imgs/sensors/image-32.png)

### Inertial Sensor Interface
- Circuitary to digitse sennsor voltage output
- Amplifier to increase signal - and to get best signal to noise ration (SNR)
- Signal processing tofilter and extract desired information
- Stabilising sensor perforamnce over temerature
![alt text](imgs/sensors/image-33.png)

### Accelerometer
- Measure acceleration
- Multi axis can measure orientatio of gravity directly
- But also can respond to linear acceleration due to motion in x y z
- Acceleration can be generated by motion of sensor or by gravity
- Gravity sensing application used a lot (eg tilt sensing)
- ![alt text](imgs/sensors/image-34.png)

#### Open Loop Vs Closed Loop Accelerometers
- Open loop 
  - Simplest and ease of fabrication
  - Less accurate 
  - Issues with large manufacturing tolerances
  - Larger masses have second order effects, non linear (twisting)
  - Silicion suspension systems are additioanly non linear
  - BUT CHEAP
- Closed Loop
  - More accurate
  - Use output signal + circuitryu to stee actuation mechanism back to point of rest
  - **Force balance devices**
  - Electrical signal proprotional to feedback force
  - Advantages:
    - Deflection of mass reduced - hence less non linearity
    - Sensitivity determined by control system
    - Dyanmcis of control system tailored to application
  - Disadvantages:
    - More complex
    - More expensive
     ![alt text](imgs/sensors/image-35.png)

#### Piezoresistive Accelerometers
- First type - open loop control
- Produced on back of pressure sensors
- Poor temeperature coefficient (dependent on temperature)
- 1-3mV/G 5G to 50G dynamic range, 0.25%/deg C temp coefficient
- Can use integrated circuitary to improve perforamnce
- Uses more power than capacitanve
- Microcmachined out of single crystal silciion
- $\Delta R / R = k_a a_y$ 
- ![alt text](imgs/sensors/image-36.png)

#### Capacitive Accelerometers
- Larger signals
- Good steady state
- Low noise
- But senstive to Electromagnetic fields
- ![alt text](imgs/sensors/image-37.png)

##### Vertical Capactive Accelerometer
- Eeasy to fabricate, just miromachining
- ![alt text](imgs/sensors/image-38.png)


##### Lateral Capacitive Accelerometer
- Cheaper to go with lateral version
- Use surface micromachining
- Comb structure - reduces electrostatic forces, more linear
- Many combs improve signal
- - Sensitivity inline with wafer plane
- Proof of mass much smaller (thinner)
- Onchip electronics for compensation
- Sensing element is poly silicion on top of sacrificial silicion oxide layer.
- ![alt text
- ](imgs/sensors/image-39.png)

#### Piezoelectic MEMS Accelerometers
- Common in macro accelerometers, same principle for micro
- Movement indcues surface charge that can be measured
- High bandwidths
- Poor at low frequencies as charge dissipates
- Usually ZnO or AlN as can be easily deposited
- 1.5mV/G 3Hz - 3kHz
- ![alt text](imgs/sensors/image-40.png)
- Need high impedance to measure

### Gyroscopes
- Measure angular rate
- Gyro has one axis, but can be mounted in 3D 
- ![alt text](imgs/sensors/image-41.png)
- Use the **Coriolis Effect**

#### Coriolis Effect
- Depending on reference, see curved path
- IE: Standing on rotating platform, near center
- If you move to the point near the edge your speed relative to ground is increased
- The rate of increase of your tangential speed caused by your radial velocity is coriolis acceleration
- ![alt text](imgs/sensors/image-42.png)

#### Sensing
![x](imgs/sensors/image-43.png)
- Measure the Coriolis acceleration
- Using bivrating mass. Resonant strucutre
- Then clever maths
![alt text](imgs/sensors/image-44.png)


#### Lateral PolySilicon Gyroscope
- Earyl 1996
- Comb drive actuation to resonate mass
- Then capactive pickup
- ![alt text](imgs/sensors/image-45.png)

#### ring MEMS Gyroscope
- Capacitve pick up place at points at antinode points of flexila mode and nodes of the secondary flexial mode
- Made with DRIE (Deep Reactive Ion Etching)
- Generally more expensive, used in aerospace
- ![alt text](imgs/sensors/image-46.png)


### Commerical MEMS Sensors
- ADXL202 - 2 axis
- Surface mircomachined
- Static and dyancic accelerations
- Capacitive sensing
- ![alt text](imgs/sensors/image-47.png)


## Pressure Sensors
- MEMS tech ideal for making low cost microsized pressure sensors
- Pressure measurement from displacement or strain
- ![alt text](imgs/sensors/image-48.png)
- Applications:
  - Automatoive air pressure sensor
  - Typre pressure sensor
  - Blood pressure
- Mostly fabricated from forming mebranes in silicion
- Common method;
  - Wet etching (KOH)
  - Also can use surface micromachining (can have a higher precision)
- Define membrane dimensions by using etch stops (electrochemcial, timed, boron)
- 3 Types:
  - Absolute (relatuive to vacuum)
  - Gauge (relative to atmospheric pressure)
  - Differential (relative to two inputs) (easiest)
- When bulk micromachining:
  - Accruate dimensional toelrence are essential for good manufacturing process
  - use of dopants may lead to considerable residual stresses that can cause buckling of a structure
  - Fatigue endruance will depend on the surface roughness and hence the quaility of the ethcing process.
- When Surface micromachining:
  - Mechanical properties of polysilion are predominatly detemrined by grainsize
  - Smallest physial dimension of the structure should be larger than the grainsize (so linear elasticity applies)
  

  ### Piezoresistive Pressure Sensors
  
  #### Simplest
  - Simplest
  - Thin silicion membrane
  - Resistors placed on points of maximum strain
  - Used to measure deflection
  - Piezo-resistors diffused in top
  - Single Cyrstal Silicon
    - Excellent material
    - No creep (no plasticicity)
    - No hysteresis 
  - Been in use for years
  - ![alt text](imgs/sensors/image-49.png)

#### Boss Design
- Employs rigid center, ehnce resitors can be laid out in pairs with no inrinsic stress issue (thicker)
- Arrangement improves linearily characteristics of diaphram in both directions - so suitable for differential pressure
- ![alt text](imgs/sensors/image-50.png)

#### Surface Micromachined
- Cheaper and smaller
- Diaphram formed from SiNx or polysilicon
- But requires sacrificial layer
- Used for Blood pressure measurement
- can use a dummy pressure senosr for temperature compensation

![alt text](imgs/sensors/image-51.png)


#### Cantilever Beams
- Atteched to underside of the diaphragm
- Piezoresistive strain guage on cantilever
- Mechancial "amplifier"
- Second beam used for temperature compensation
- ![alt text](imgs/sensors/image-52.png)

### Capacitive Pressure Sensors
- Use parallel plates
- Can be more compact
- Highly non linear
- Early: Pyrex (cryasl glass) as lid
- Newer: Sacirfical layers
- ![alt text](imgs/sensors/image-53.png)

![alt text](imgs/sensors/image-54.png)

**Comparison:**
![alt text](imgs/sensors/image-55.png)


### Resonant MEMS Pressure Sensor
- Use a resonant mechanical structure to sense deflection in pressure sensitive diaphram
- Has many challenges:
  -  Fabrication of resonator on top of presure sening structure (complex)
  -  Silicion resonantors - incoroorating vibration excitiement circuitary and detection mechanism
  -  Vaccum encapsulation of resoantor to remove gas damping effects
-  
#### Lateral Resonant Pressure Sensor
- Mounted centrally on silicion diaphragm
- Electostatic excitiation
- Capacitive detection
- ![alt text](imgs/sensors/image-56.png)

### Warwick Design Presure Sensor
![alt text](imgs/sensors/image-57.png)
![alt text](imgs/sensors/image-58.png)
![alt text](imgs/sensors/image-59.png)
![alt text](imgs/sensors/image-60.png)
![alt text](imgs/sensors/image-61.png)
![alt text](imgs/sensors/image-62.png)


### Pressure Sensor Fabrication Steps
![alt text](imgs/sensors/image-63.png)



## Force Sensors
- Importat quantity in many applications
- EG: Weight machines, load cells, aerospace engines
- Large range
- Require environmental robustnes from vibration / overloads
- Mecahnical interfacing (physical contact) is diffucult for touch/tactile/contacting measurements
- Mostly fabricated from forming mebranes in silicion
- Common method;
  - Wet etching (KOH)
  - Also can use surface micromachining (can have a higher precision)
- Define membrane dimensions by using etch stops (electrochemcial, timed, boron)
- When bulk micromachining:
  - Accruate dimensional toelrence are essential for good manufacturing process (needs calibration)
  - use of dopants may lead to considerable residual stresses that can cause buckling of a structure
  - Fatigue endruance will depend on the surface roughness and hence the quaility of the ethcing process.
- When Surface micromachining:
  - Mechanical properties of polycrystaline silion are predominatly detemrined by grainsize
  - Smallest physial dimension of the structure should be larger than the grainsize (so linear elasticity applies)

![alt text](imgs/sensors/image-64.png)


- Force is normalle converted into a change in leng (spring movement) or strain
- Hookes Law: $F = k\Delta x$
- Methods of measuring:
  - Piezoresistive
  - Capacttive
  - Resonant and Surface Acoustic Wave (SAW)
  - Less common: 
    -  Piezoelectirc strain guage
       -  Need to deposit piezoelectric material (which siliion is not)
       -  ZnO, AlN possible
       -  Small singal so need high impedance amplifier
       -  PZT has higher coefficient but not easy to despoit
    -  Metal strain guages - Not ideal for MEMS
       -  Low guage factor (1.7) - small output voltage range
       -  Small output voltage (as small change in resistance)
       -  Small operating range
       -  High power consumption as needs currents
       -  Temperature coefficient high compared with straing
       -  Therefore piezo-resistive ideal.  
-  

### Capacitive Force Sensors
- Differential force sensor
  - Variable cap sensor
  - Two electrodes with small cap
  - Ass force is applied, one increases in capacitance, the other decreases
  - Therefore differential reading gives higher sensitivity and linearity
  - ![alt text](imgs/sensors/image-65.png)
- Load Cell
  - Array of capacitive sensing elements formed from pillars
  - Design fabricated from two silicion wafers
  - Bottom electrode array forms capacitodes with a common top electrode
  - Force moves pillars closer together
  - Quite robust
  - ![alt text](imgs/sensors/image-66.png)

### Resonator
- Highly attractive
  - Easy frequency measurement
  - Extremely sensitive - high Q factor
  - Wide dynamic range
  - Easy intergration in CMOS
- Surface microcmaching sensors based on tuning fork
- Based on DETF (double ended tuning fork)
- One side fixed, other have applied force
![alt text](imgs/sensors/image-67.png)


### Cantilever Force Sensors - Silicon Based
- Load deflection sensing by piezeoresitive straing sensing of cantilever beam
- Advabtages over metal:
  - High guage factor (+-130 compared to 2 for metal)
- Disadvantages:
  - High temperature dependence 
  - Overcome by using pairs of strain guages
- ![alt text](imgs/sensors/image-68.png)

### Force Microscope
- Need to scan microscopic surfaces
- Called AFM (Atomic Force Microscope) or SFM (Scanning Force Microscope)
- Vibrating or statid head
- Use piezoresistive, piezoelectric or capactive sensors
- ![alt text](imgs/sensors/image-69.png)

#### Atomic Force Microscope
- Measures the force between atoms of probe and ataoms of sample
- Works on conductors and insulators! (therfore no current)
![alt text](imgs/sensors/image-70.png)
![alt text](imgs/sensors/image-73.png)

#### Probart - Probe Array technology
![alt text](imgs/sensors/image-71.png)
![alt text](imgs/sensors/image-72.png)


## Flow Microsensors
- Many applications:
![alt text](imgs/sensors/image-74.png)
- Many types:
  - Thermoresistive
  - Thermoelectric
  - Thermoelectronic
  - Resonant
- With many configurations:
  - Hotfilm (Anenometer, heat loss)
  - Calorimetric (thermo transfer)
  - Time of flight (pulse)
  
### Thermal Flow Sensor
- Majoruty of flow sensors
- Electrical resistivty changes with temperature
- Rely on abiliyt of fluid flow to cause heat transfer
- Therefore is trandsuced into a varying electrical signal through the sensor response to flow change
- Senosr should be thermally isolated so only heat transfer is from the flow
- Other heat transfer pathways should be minimised (substrate, electircal leads etg - result in thermal losses, degrade snesor performance)
- Thermal flow sensor response depenednt upon constant fluid temperature. temperature compensation must be implemented if fluid temperature drifts


#### Anemometer (Heat loss)
![alt text](imgs/sensors/image-75.png)
- Hot wire / hot film serves as a heater and sensing element
- Resistance value dependent on temperature
- Hot wire:
  -  Resistive wire within fluid flow
-  Hot film:
  -  Thin film resistive senor, element placed adjecent to the flow
-  ![alt text](imgs/sensors/image-78.png)
- Linear resistance relatioship to temperature
- ![alt text](imgs/sensors/image-79.png)
- ![alt text](imgs/sensors/image-80.png)
- ![alt text](imgs/sensors/image-81.png)

#### Calorimetric Flow Sensor
![alt text](imgs/sensors/image-76.png)
- require two elements
- One heating elementm, two temperature sensors
- Upstream sensor cooled by fluid, downstream heated from heating element
- Amount of heat measured is proportional to flow rate
- Calibration performed for each fluid due to different thermal properties
- Operated as a wheatsone bridge and uses CMOS tech
- Significantly more sensitive than aneometer
- Thereoy:
  - Simple equations
  - ![alt text](imgs/sensors/image-82.png)
  - ![alt text](imgs/sensors/image-83.png)
- Directional thermal flow sensors
  - Can measure flow velcoity and direction with few heaters and few sensors
  - ![alt text](imgs/sensors/image-84.png)  

#### Time of Flight Flow Sensor
![alt text](imgs/sensors/image-77.png)
- Transit time of a thermal pulse is tracked to extract flow rate
- At least one heater and one downstream thermal sensor
- Short thermal pusle transferred from heater to fluid.
- Ideally heater is thermally isolated from substrate to elimate interference from thermal conduction effects
- ![alt text](imgs/sensors/image-85.png)
- Theory:
  - Downstream thermal flow sensor detects thermal pulse
  - Least senstive tio changes in ambient temperature as maxima are measured
  - Can be bidirectioanl
  - ![alt text](imgs/sensors/image-86.png) 

#### Transconduction Principles
- Thermoresistive - **resisteive** elements
- thermoelectric - Thermal changes from **thermopiles**
- Thermoelectronic sensing - **Diode** and **transistor** elements
- Frequency analogue sensors - based on changes in **resonant** frequency within mechanical structures due to temperature change induced stress
  

##### Thermoresistive Microthermal flow sensors
- Nickel resistors used due to their high TCR (temperature coefficient of resistance)
- Cr Ni resistors over a suspended silcion nitride membrane - creates an array of flow sensors for micro gas chromatography systems
- ![alt text](imgs/sensors/image-87.png)

#### Thermoelectirc Calorimetric Flow Sensors
![alt text](imgs/sensors/image-88.png)


#### SOI MEMS Flow Sensors
- Silicon on insulator (SOI) technology
- Fastest bandwidth
- Based on hotwire with thermodiodes or thermo couples
- Low cost -small structures
- By Spinout company from 2016 - Flusso LTD (serveral patents)
- SOI CMOS, Tungsten metalisation, stress compensated membrane,e DRIE membrane
![alt text](imgs/sensors/image-89.png)
![alt text](imgs/sensors/image-90.png)



### Pressure Difference Flow Sensors
- Measurement of differential pressure in flowing fluiod
- Measure presusre drop along channel (fluidic reisistnace)
- Mass flow based on fludidic owhms law
- Use capacitive pickup (unspirisingly)
- Although piezoresistive / piezoelectric also used
![alt text](imgs/sensors/image-91.png)
- ![alt text](imgs/sensors/image-92.png)
- Capacitive:
  - Fabricated using bulk silicion micromaching and boron etch stops
  - Different pressure measured by capacitve pressure sensor

### resontnat Bridge Flow Microsensor
- Based on frequnecy shift of reosnant microbrdige
- Fabricated by front side anisotropic etch of grobve
- Thinfilm phosphorous doped polysicilion reisitions mebedded with bridge
- thermal excitiation and piezorresitive sensing of vibrations
- High sensitivity - fast repsonse - good stability
- ![alt text](imgs/sensors/image-93.png)
- ![alt text](imgs/sensors/image-94.png)


### Commerical Flow sensors
- Driven by car industry
- Originally hot wire aneometer -but poor range, fragile, cannot reverse flow
- Changed to microversion with Pt heater on nitride membrane (150nm thick)
- fast due to low thermal mass, can withsand pressures of over 1 bar
- Uses air bypass from main air intake to reduce pressure
- 1996 start
- ![alt text](imgs/sensors/image-95.png)


- HSG-IMIT flow sensor with polysilicon heating element and temperature snsing elements
- Coated with Sio2 and SiNx for protection
- Connected bty nano tubes for flow measurement in larger pipes
- Air con systmes
- 2015 miliosn sold
- ![alt text](imgs/sensors/image-96.png)
- ![alt text](imgs/sensors/image-97.png)

## Chemical Microsensors
- environmental / Air quality
- Very large market:
  - Health care, air quality, global warwming, food saftey, safety
- many sources of VOCs:
  - ![alt text](imgs/sensors/image-98.png)
- Vocs lead to Poor Indoor Air Quality (IAQ)
- Can lead to range of chronic adverse health effects
- Issue with gas sensors:
  - Non linearity - Response not proportional to concentration
  - Slow Response - Slow to reach steady state (few seconds)
  - Small Working range - Restricted working range
  - Low sensitivity - Only respond to large input signals
  - SBaseline drift - Output varies with time
  - Ssensitivity Drift - Output varies with time (eg with temperature)
  - Offset drifts - Offset changes with time (ageing of sensor)
  - Interference - Sensitive to external conditions (eg humidity)

### Gas Sensor Principles
- Reaction
- Resisitve
- Mass Sensitivity
- calorimetic
- Optical
- FET
- ![alt text](imgs/sensors/image-99.png)

Classification:
![alt text](imgs/sensors/image-100.png)


### Classic Electrochemical Sensors
- Very common for toxic and other gases
- Low poer
- Weak temperature dependence
- Large
- Expensive £20 each
- Liquid electrolyte can evaporate
- Eletrodes can poison
- Cannot be minaturised
- ![alt text](imgs/sensors/image-101.png)

### Optical Gase Sensors
- Co2 and CH4
- Uses IR source and detectorer
- Good selectivity
- Physical sensor
- Large
- Power hungry
- Expensive
- ![alt text](imgs/sensors/image-102.png)

### Plasmonically-enchanced CMOS NDIR gas sensor
![alt text](imgs/sensors/image-103.png)


### Resistive Gas Sensors
![alt text](imgs/sensors/image-104.png)
- Polymer composite: cyrano Inc
- Conducting polymer: Marconi PLC, osmetech PLC
- Metal Oxide (T=400C): Figaro, FiS, Applied Sensor

Metal Oxide Nano Materials:
![alt text](imgs/sensors/image-105.png)


### MEMS based Gas/Odour Sensor
- Much better power efificiency
- Very small
- ![alt text](imgs/sensors/image-106.png)
- ![alt text](imgs/sensors/image-108.png)

### SOI CMOS Microhotplate
- ![alt text](imgs/sensors/image-107.png)

### Smart Gas Sensors
- CMOS tech for air quality monitioring
- Indoor Air Quality (IAQ)
- Toxic gas detetor for Carbon Monoxide (CO)
- alchol Breathalyser to provide ethanol levels on breath for Blood acolhol content (BAC)

#### First In Phone Humidity
- Sensiron Chips for temp and relative humidity
- SHT21
- Capacitvie type
- +-2% RH +- 0.3C
- Low power and digital I2C
- Used in Samsung Galaxy S4
- ![alt text](imgs/sensors/image-109.png)

### Breath Anaylsis
- Conecntration of VOCs in breth, can provide non-invasive health monitoring
- Acetone - Metabolism + Diabetes
- Isoprene - Chlolesterol
- Ammonia - Liver function
- Expensive and acurate sensors used in hospitals
- Indirect Calorimetry
  - Considered best for Energy expenditure (EE) assessment in clinical car
  - Wheere volumes of oxygen consumed and carbon dioxide produced are measured
  
#### Breath Alchol
- CCS801 - responds to Ethanol
- 4 seconds required for breath anaylsis
- Wide accuracy
- Gives an indicator, not certified sensor
- ![alt text](imgs/sensors/image-110.png)


#### CO - Toxic Gas Detection
- CO is odourless and colourless
- CCS801 responds to CO
- Indicator not certified
- so "Safe / Warning / Alert"


### AQ sensors on Robots
- Aim for highbandwith sensors, with fast response time in harsh environments
- To generate map in real time
- Incorporated temperature modulation technique which uses MOX sensors dynamic repsonse to decrease the response time and remove drift
- ![alt text](imgs/sensors/image-111.png)
- ![alt text](imgs/sensors/image-112.png)
- ![alt text](imgs/sensors/image-113.png)


### Market
- Estimated to be more than 15 billion
- Low cost CMOS sensors
- Algortigms implemented to compensate for stability and interference
- BME688 combo chip does everything with added AI
![alt text](imgs/sensors/image-114.png) 



## BoSensors & BioMEMS
- Microsystems / MEMS are at the size of large virus, bacterial cell and redblood cell
- Biological sensors (biosensors) contain biological modeluces
- Generally detect non-vollatite molecures and so work in the liquid phase (sense of taste - gustation)
- Can detect volatile molecules (smell - olfaction)
- BioMEMS is a growing field
  - Biosensors, bio reactors, biopumps, biovalves, bioneedles, microfluidics, micromechanics, bio chemsitry, optics, signal processing
  -  

### Biological Molecules
- Small molecules:
  - Hydrocarbonates (sucrose)
  - Lipids (cholesterol)
  - Vitamins (A)
  - Hormones (adrenaline)
  - Disaccharides (sucrose, lactose, maltose)
  - Neurotransmitters (dopamine, serotonin)
- Biological Monomers
  - Amino acides (alanine)
  - Nucleotides (adenosine, guanosine, thymir, cytosize (AGTC))
  - Monosaccharides (half of sucrose)
- Polymers / Macromolecules
  - Peptides, polypeptides (chain of amino acids)
  - Proteins (enzymes, antibodies)
  - Nucleic acids (DNA, RNA)
  - Polysaccharides (starch, cellulose)
  - Lignin (Plant Cells)


### BioSensing Principles


#### Enzyme Based Reactions
![alt text](imgs/sensors/image-115.png)
**Diabetes:**
  - Common in elderly people
  - Use blood glucose sensor
  - Biomolecule glucose oxidase
  - Billions sold, disposable strips
  - Abbott et al.
- Electrochemcial
  - Eznymatic redox reaction
  - Plastic strips with polymers and enzyme
  - 2 electrode cell
  - Millions sold
  - ![alt text](imgs/sensors/image-117.png)
- Now theres wearable epidermal glucose sensors
  - Non invasive
  - ![alt text](imgs/sensors/image-118.png) 

**Pulse Oximeter**
- Measures blood oxygen saturation
- Based on IR absorption
- Finger clip on
- Smart watch 
- Large market
- ![alt text](imgs/sensors/image-119.png)


#### Antibody-antigen reaction
![alt text](imgs/sensors/image-116.png)
- Inject antigen into host (chicken, mouse etc) to obtain antibodies
- Large molecule 150kDa
- Label antibody (eg anti-goat) with fluorescent dye
- Used for biochemcial assays
- ELISA (Enzyme Linked Immunosorbent Assay)
  - Load up titer plate with wells for different antigens
  - Look for fluoresent
  - Simple method
- Fluorescent tequinuq - UV
 - Different levels for difference colours etc


- DNA Biosensors
  - ssDNA and cDNA
  - Compare and check for polymorphism
  - Denaturing temperature changes and can be measured
  - ssDNA also on SAW resonantors
  - SSDNA also on optical fibres
  - ![alt text](imgs/sensors/image-120.png)
- DNA BioSensors with qPCR
  - Polymerase chain reaction - large quantities of DNA/RNA and identifiy
-  


#### Cell Based Sensors
- Cytometers for:
  - Red blood cells
  - Platelets
  - White blood cells
  - Bacteria
- Optical
- Capacitive
- Piezoelectirc resonators
- Cantielver beams
  
Sizing Cells:
- Electric field displacement
- EG on urine sample
- Red cells, white cells, bacteria
- ![alt text](imgs/sensors/image-121.png)


Isolation of Leukocytes from human blood
- Lysis of red blood
- Electrodynamic manipulation using AC fieldz
- ![alt text](imgs/sensors/image-122.png)

Cells on Cantielver Beams
- Biological coatings on micro cantilever beams
- Measure frequency shift
- Requires large molelcues
- ![alt text](imgs/sensors/image-123.png)

