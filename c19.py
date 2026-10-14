# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH19=mkch(19,"Control, sensing and signal conversion",
 "Closed-loop control, the sensors that report the real world, and the conversion between analogue and digital",
 "A circuit that simply switches a load on is open-loop: it acts without checking the result. "
 "A control loop measures the result and adjusts. This chapter develops the sensing, comparison "
 "and correction chain that appears in every thermostat, motor drive and process controller.",
 ["Draw a closed control loop and name the function of each block.",
  "Distinguish open-loop from closed-loop control and state when each is appropriate.",
  "Describe on-off control with hysteresis and compute the switching band.",
  "Explain proportional control and the meaning of offset.",
  "Select a sensor for temperature, light or position and describe its characteristic.",
  "Compute the resolution and quantisation step of an analogue-to-digital converter.",
  "Scale a sensor signal to match a converter input range."],
 ("c19_loop","A closed control loop. The measured value is compared with the set point and the "
  "difference drives the correcting element until the error is reduced.",46),
 [dict(h2="Open loop and closed loop",
   paras=["In open-loop control the output is set and no account is taken of the result. A lamp "
    "on a timer is open-loop: the timer does not know whether the room is bright. Open-loop "
    "control is simple, cheap and adequate whenever the relationship between input and output "
    "is predictable and disturbances are small.",
    "Closed-loop control measures the controlled quantity, compares it with the desired value, "
    "and uses the difference to drive the correcting element. The measured value is called the "
    "process variable, the desired value is the set point, and their difference is the error. "
    "Closed-loop control tolerates disturbances and component drift because it responds to the "
    "result rather than to the command."],
   bullets=["Set point: the value the system should reach, supplied by the operator or a schedule.",
    "Process variable: the measured value of the controlled quantity.",
    "Error: set point minus process variable, the signal that drives correction.",
    "Controller: the block that converts error into a correcting output.",
    "Correcting element: the valve, heater, contactor or drive that acts on the process.",
    "Feedback path: the sensor and conditioning circuit that reports the result."],
   bh="The blocks of a control loop",
   eq=["error = set point - process variable",
       "e = SP - PV"]),
  dict(h2="On-off control and the need for hysteresis",
   paras=["The simplest controller switches the correcting element fully on when the error is "
    "positive and fully off when it is negative. A heater controlled this way would switch at "
    "exactly the set point, and because the measurement always carries a little noise the output "
    "would chatter rapidly between states, wearing the contacts and the load.",
    "The cure is hysteresis: two thresholds instead of one. The output turns on below a lower "
    "threshold and off above an upper threshold, and between them it holds its last state. The "
    "separation is the switching band, or differential. A wide band gives slow, infrequent "
    "switching and a large swing in the controlled quantity; a narrow band holds the quantity "
    "closer to the set point but switches more often."],
   fig=("c19_onoff","On-off control with hysteresis. The two thresholds prevent chatter by "
    "requiring the measured value to travel the width of the band before the output changes.",46),
   eq=["upper threshold = SP + band/2",
       "lower threshold = SP - band/2",
       "differential = upper - lower"]),
  dict(h2="Proportional control and offset",
   paras=["Proportional control makes the correcting output a multiple of the error rather than "
    "a simple on or off. Small errors produce small corrections, so the system settles smoothly "
    "instead of overshooting. The multiplier is the proportional gain.",
    "A purely proportional controller has a characteristic limitation. Because the output is "
    "proportional to the error, a non-zero output requires a non-zero error. A heater that must "
    "run at thirty per cent to hold temperature against heat loss therefore settles at a "
    "temperature slightly below the set point. That steady difference is the offset, or droop. "
    "Raising the gain reduces the offset but moves the loop towards instability, which is why "
    "practical controllers add integral action to remove the offset entirely."],
   eq=["output = K_p " + TIMES + " e",
       "offset " + AP + " required output / K_p"],
   table=(["Control action","What it responds to","What it fixes","What it costs"],
    [["On-off with hysteresis","Error sign only","Simplicity, no tuning","Continuous cycling about the set point"],
     ["Proportional","Present error","Smooth approach, no chatter","Leaves a steady offset"],
     ["Proportional plus integral","Present and accumulated error","Removes the offset","Slower response, risk of overshoot"],
     ["Proportional, integral, derivative","Error, its history and its rate","Fast settling with no offset","Three parameters to tune, noise sensitivity"]],
    None)),
  dict(h2="Sensors: turning a physical quantity into a voltage",
   paras=["A control loop can only regulate what it can measure. Every sensor is a transducer "
    "with a characteristic relating the physical quantity to an electrical one, and that "
    "characteristic is rarely a straight line over the whole range.",
    "A thermistor is a resistor whose resistance falls sharply with temperature. It is cheap and "
    "sensitive but markedly non-linear, so it is used either over a narrow span or with "
    "linearisation. A resistance thermometer uses the nearly linear rise of platinum resistance "
    "and is used where accuracy matters. A thermocouple produces a small voltage from the "
    "junction of two dissimilar metals and suits high temperatures, but it needs cold-junction "
    "compensation. A light-dependent resistor falls in resistance with illumination. A "
    "potentiometer reports shaft or slider position directly as a voltage ratio.",
    "Most of these are resistive, and a resistance is not a voltage. The usual conditioning "
    "circuit is therefore a divider or a bridge, which converts the resistance change into a "
    "voltage change that the controller can read."],
   fig=("c19_conv","Sensor conditioning. The resistive sensor forms one arm of a divider, and "
    "the resulting voltage is scaled to match the converter input range.",46),
   table=(["Sensor","Quantity","Characteristic","Typical use"],
    [["Thermistor","Temperature","Strongly non-linear, resistance falls as temperature rises","Appliance and board-level temperature limits"],
     ["Resistance thermometer","Temperature","Nearly linear rise with temperature","Process measurement where accuracy matters"],
     ["Thermocouple","Temperature","Small voltage, needs cold-junction compensation","Furnace and exhaust temperatures"],
     ["Light-dependent resistor","Illumination","Resistance falls with light, slow response","Lighting control and dusk switching"],
     ["Potentiometer","Position","Linear ratio of output to supply","Valve and actuator position feedback"],
     ["Current transformer","Alternating current","Secondary current proportional to primary","Load monitoring without breaking the circuit"]],
    None)),
  dict(h2="Analogue to digital conversion",
   paras=["A digital controller works on numbers, so the conditioned sensor voltage must be "
    "converted. An analogue-to-digital converter divides its input range into a number of equal "
    "steps set by its resolution in bits, and reports which step the input falls in. An n-bit "
    "converter has two to the power n steps.",
    "The size of one step is the quantisation step, and it sets the finest change the system can "
    "detect. No amount of averaging recovers detail smaller than one step, so the sensor signal "
    "should be scaled to use as much of the converter range as possible. A sensor that swings "
    "only over a tenth of the input range wastes more than three bits of resolution.",
    "Conversion in the other direction uses a digital-to-analogue converter, which reconstructs "
    "a voltage from a number. The same resolution argument applies to its output steps."],
   eq=["steps = 2" + "\u207f",
       "step size = V_range / 2" + "\u207f",
       "resolution (10 bit, 5 V) = 5 / 1024 = 4.88 mV"],
   panel=("Scaling before conversion",
    ["Measure the full swing of the sensor output across the range you actually need.",
     "Choose a divider or amplifier that maps that swing onto nearly the whole converter input range.",
     "Leave a small margin at both ends so that tolerance and drift do not clip the signal.",
     "Check that the source resistance seen by the converter is low enough for its sampling circuit."])),
 ],
 [ex("Switching band of an on-off controller",
   "A thermostat has a set point of 20 " + DEG + "C and a differential of 1.5 " + DEG + "C.",
   "The two switching thresholds and the resulting swing in room temperature.",
   [("Half the differential","1.5/2 = 0.75 " + DEG + "C"),
    ("Upper threshold","20 + 0.75 = 20.75 " + DEG + "C"),
    ("Lower threshold","20 - 0.75 = 19.25 " + DEG + "C"),
    ("Swing between switching points","20.75 - 19.25 = 1.5 " + DEG + "C"),
    ("Effect of narrowing the band","Closer control, more frequent switching")],
   "The room temperature cycles over the width of the differential, not about a single value. "
   "Choosing the band is a direct trade between control accuracy and switching frequency."),
  ex("Offset in a proportional controller",
   "A proportional heater controller has a gain of 8 per cent output for each degree of error, "
   "and the heater must run at 24 per cent to hold the set point against heat loss.",
   "The steady-state offset below the set point.",
   [("Relationship","output = K_p " + TIMES + " e"),
    ("Rearranged for error","e = output / K_p"),
    ("Substituting","e = 24 / 8 = 3 " + DEG + "C"),
    ("Settled temperature","3 " + DEG + "C below the set point"),
    ("Effect of doubling the gain","Offset halves to 1.5 " + DEG + "C, stability margin falls")],
   "The offset is real and predictable, not a fault. It is the price of proportional-only "
   "control, and it is why integral action exists."),
  ex("Resolution of an analogue-to-digital converter",
   "A 10-bit converter has a 0 to 5 V input range. A temperature sensor delivers 10 mV per "
   + DEG + "C over a 0 to 100 " + DEG + "C span.",
   "The voltage step, the temperature step, and the fraction of range used.",
   [("Number of steps","2\u00b9\u2070 = 1024"),
    ("Voltage per step","5 / 1024 = 4.88 mV"),
    ("Temperature per step","4.88 mV / 10 mV per " + DEG + "C = 0.49 " + DEG + "C"),
    ("Sensor output at 100 " + DEG + "C","100 " + TIMES + " 10 mV = 1.0 V"),
    ("Fraction of the 5 V range used","1.0 / 5.0 = 20 per cent")],
   "The converter can resolve about half a degree, but only a fifth of its range is in use. "
   "Amplifying the sensor output by five would improve the temperature resolution to about "
   "0.1 " + DEG + "C without changing the converter."),
 ],
 lab("building and tuning an on-off temperature controller",
  "Build a thermistor-sensed on-off controller, measure its switching thresholds, observe the "
  "effect of changing the differential, and record the resulting temperature cycling.",
  ["Regulated direct-voltage supply, 12 V.",
   "Thermistor, nominal 10 k" + OH + " at 25 " + DEG + "C, with its stated characteristic.",
   "Resistors to form the divider and the feedback path, 0.25 W.",
   "Comparator or operational amplifier, single supply type.",
   "Relay or transistor output stage with a small lamp as the simulated heater.",
   "Digital multimeter and a reference thermometer."],
  ["Record the thermistor resistance at room temperature and compare it with its stated value.",
   "Build the divider with the thermistor and compute the expected output voltage.",
   "Set up the comparator with a fixed reference to establish the set point.",
   "Confirm the output switches as you warm the thermistor gently between your fingers.",
   "Add a feedback resistor from output to the reference input to create hysteresis.",
   "Measure the divider voltage at the instant the output turns on, and again when it turns off.",
   "Compute the differential from those two voltages and convert it to a temperature span.",
   "Change the feedback resistor to widen the band, then repeat the two threshold measurements.",
   "Record the lamp on-time and off-time in each case and compare the switching frequency.",
   "Return the circuit to the narrower band and confirm the thresholds repeat on a second run."],
  ("c19_onoff","The on-off control test circuit. The feedback resistor sets the width of the "
   "switching band, which you measure directly as two divider voltages.",46),
  ["Feedback resistor","V at turn-on","V at turn-off","Differential (V)","On-time (s)"],
  [["none","","","",""],["1 M" + OH,"","","",""],["470 k" + OH,"","","",""],
   ["220 k" + OH,"","","",""],["100 k" + OH,"","","",""],["47 k" + OH,"","","",""]],
  ["Which feedback resistor produced the widest switching band, and why?",
   "How did the switching frequency change as the band narrowed?",
   "What happened to the output with no feedback resistor fitted, and why?",
   "Convert one measured differential into a temperature span using the thermistor characteristic.",
   "If this controlled a real heater, what band would you choose and what would you trade away?",
   "Why does a narrow band not give arbitrarily good control in a system with slow response?"],
  ["Keep the supply voltage low; there is no reason to prove this principle at mains voltage.",
   "Warm the thermistor with your fingers or warm air, never with a flame.",
   "Fit a flyback diode across any relay coil before applying power.",
   "Check the output stage current rating against the lamp before connecting it."]),
 [["Output chatters rapidly at the set point","No hysteresis, or band narrower than the measurement noise","Observe the comparator input on a scope while it switches","Add or increase the feedback resistor to widen the band"],
  ["Controlled quantity settles below the set point","Proportional offset, not a fault","Compare the steady error with required output divided by gain","Accept it, raise the gain slightly, or add integral action"],
  ["Loop oscillates with a growing swing","Gain too high for the system's delay","Reduce the gain and observe whether the swing decays","Lower the gain, then add integral action to recover accuracy"],
  ["Reading jumps by several converter steps","Sensor signal too small for the converter range","Measure the sensor swing and compare it with the full input range","Amplify or rescale the sensor signal before conversion"],
  ["Temperature reading drifts over hours","Self-heating in the sensor, or reference drift","Reduce the sensor current and watch whether the drift falls","Lower the divider current, use a stable reference"],
  ["Output never switches","Set point outside the sensor's achievable range","Compare the divider voltage with the reference voltage directly","Rescale the divider so the set point falls inside the swing"],
  ["Correct response but very slow","Sensor thermally isolated from what it should measure","Compare sensor response time with the process response time","Improve thermal contact and reduce the sensor's own mass"]],
 ("c19_conv","The sensing and conversion chain. Each stage must match the range of the next, "
  "or resolution is lost before the controller ever sees the signal.",46),
 ["State the set point, the measured quantity and the correcting element before drawing a loop.",
  "Record a sensor's actual characteristic rather than trusting the nominal figure.",
  "Scale a sensor signal to fill the converter range; resolution thrown away cannot be recovered.",
  "Set the hysteresis band deliberately from the acceptable swing, not by trial and error.",
  "Check that the sensor measures the quantity you care about, at the place that matters.",
  "Change one tuning parameter at a time and record the result before changing another."],
 ["Define open-loop and closed-loop control, and give a practical example of each.",
  "Name the five blocks of a closed control loop and state the function of each.",
  "A thermostat has a set point of 60 " + DEG + "C and a differential of 4 " + DEG + "C. Find both thresholds.",
  "Explain why an on-off controller with no hysteresis is unsatisfactory in practice.",
  "A proportional controller has a gain of 5 per cent per degree and needs 40 per cent output. Find the offset.",
  "Explain in your own words why proportional-only control leaves a steady offset.",
  "An 8-bit converter has a 0 to 10 V range. Find the step size.",
  "A sensor swings over 0 to 2 V into a 0 to 5 V, 12-bit converter. How many bits are effectively wasted?",
  "Compare a thermistor and a resistance thermometer for a process requiring accuracy over 0 to 200 " + DEG + "C.",
  "Why does a thermocouple need cold-junction compensation?",
  "Sketch a divider that converts a resistive sensor into a voltage, and state what sets the sensitivity.",
  "A loop oscillates with increasing amplitude. State two possible causes and the test for each.",
  "Explain why narrowing the hysteresis band does not improve control of a slow process indefinitely.",
  "Describe one case where open-loop control is the correct engineering choice."],
 [["3","63 " + DEG + "C and 57 " + DEG + "C","Half the differential is 2 " + DEG + "C, applied either side of the set point."],
  ["5","8 " + DEG + "C","Error equals required output divided by gain, 40 divided by 5."],
  ["7","39.1 mV","Ten volts divided by 256 steps."],
  ["8","Between two and three bits","Only two fifths of the range is used, so the top bits never change."],
  ["10","The measured voltage depends on both junctions","The reference junction temperature must be known to recover the hot junction temperature."]],
 ["Open-loop control acts without checking the result; closed-loop control measures the result and corrects.",
  "A control loop comprises a set point, a sensor reporting the process variable, a comparison producing error, a controller, and a correcting element.",
  "On-off control requires hysteresis to prevent chatter; the differential sets the swing in the controlled quantity.",
  "Proportional control is smooth but leaves a steady offset, because a non-zero output needs a non-zero error.",
  "Integral action removes the offset at the cost of response speed and overshoot margin.",
  "Every sensor has a characteristic that is usually non-linear, and conditioning converts it into a usable voltage.",
  "Converter resolution sets the finest detectable change; scaling the signal to fill the input range preserves it.",
  "Resolution lost to poor scaling cannot be recovered by filtering or averaging."],
 [["Control error","e = SP - PV","The driving signal for every closed-loop controller"],
  ["Proportional output","output = K_p " + TIMES + " e","Proportional control, within the output limits"],
  ["Proportional offset","e " + AP + " output / K_p","Steady state of a proportional-only loop"],
  ["Switching thresholds","SP " + "\u00b1" + " band/2","On-off control with a symmetrical differential"],
  ["Converter steps","2" + "\u207f","Any converter of n bits resolution"],
  ["Quantisation step","V_range / 2" + "\u207f","Uniform converters across their stated range"],
  ["Divider output","V_out = V_in R\u2082/(R\u2081+R\u2082)","Resistive sensor conditioning, light loading"]],
 [["Set point","The value the controlled quantity should reach"],
  ["Process variable","The measured value of the controlled quantity"],
  ["Error","Set point minus process variable"],
  ["Hysteresis","Deliberate separation of the on and off thresholds"],
  ["Differential","The width of the switching band in an on-off controller"],
  ["Offset","The steady error left by proportional-only control"],
  ["Transducer","A device converting one physical quantity into another"],
  ["Quantisation step","The voltage change corresponding to one converter count"],
  ["Resolution","The number of distinguishable steps in a converter output"]],
 "The remaining chapter draws the whole book together. It takes the measurement habits, the "
 "circuit models, the machines, the electronics and the safety discipline, and sets them inside "
 "a single ordered method for diagnosing a fault and reviewing a design.")
