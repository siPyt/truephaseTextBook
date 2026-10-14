# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH14=mkch(14,"Operational amplifiers",
 "Very high gain tamed by feedback",
 "A single transistor's gain varies between samples and with temperature, which makes precise "
 "analogue work difficult. An operational amplifier has so much gain that feedback can be used "
 "to make the circuit's behaviour depend on external resistors instead of on the device, which "
 "is why almost all analogue signal conditioning is built this way.",
 ["Identify the operational amplifier symbol and its inverting and non-inverting inputs.",
  "State the ideal assumptions and the virtual-earth principle.",
  "Compute the gain of inverting and non-inverting amplifier circuits.",
  "Analyse summing, difference and buffer configurations.",
  "Explain comparator operation and the purpose of hysteresis.",
  "Recognise the practical limits: supply rails, offset, bandwidth and slew rate."],
 ("c14_inv","An inverting amplifier. The feedback resistor and the input resistor set the gain, "
  "and the inverting input is held at the reference potential by feedback.",46),
 [dict(h2="The device and the ideal assumptions",
   paras=["An operational amplifier is a differential amplifier with two inputs and one output. "
    "It amplifies the difference between the inputs by an enormous factor, typically a hundred "
    "thousand or more at low frequency. That raw gain is almost never used directly; it is traded "
    "away through feedback in exchange for predictability.",
    "Analysis is made simple by two assumptions that real devices approach closely. First, the "
    "input terminals draw negligible current. Second, when negative feedback is present, the "
    "amplifier drives its output to whatever value makes the two input voltages equal. Together "
    "these let every standard configuration be analysed with Ohm's law alone."],
   eq=["V_out = A(V\u207a \u2212 V\u207b)      with A very large",
       "Ideal assumption 1:  input currents \u2248 0",
       "Ideal assumption 2:  with feedback, V\u207a \u2248 V\u207b"],
   panel=("Why feedback is worth the loss of gain",
     ["Open-loop gain varies widely between devices and with temperature.",
      "Closed-loop gain depends on a ratio of two resistors, which is stable and known.",
      "Feedback also widens bandwidth and lowers output impedance.",
      "The design question becomes which resistors to fit, not which device to select."])),
  dict(h2="The inverting amplifier and virtual earth",
   paras=["In the inverting configuration the signal enters through a resistor to the inverting "
    "input, and the feedback resistor returns from the output to the same point. The "
    "non-inverting input is tied to the reference, so feedback holds the inverting input at the "
    "reference potential too. That point is called a virtual earth: it sits at reference "
    "potential without being connected to it.",
    "The consequence is that the input current is set entirely by the input resistor, and because "
    "no current enters the amplifier, all of it continues through the feedback resistor. The gain "
    "is therefore the ratio of the two resistors, with a sign inversion, and the input impedance "
    "of the stage equals the input resistor."],
   eq=["Gain = \u2212R_f / R_in",
       "Input impedance = R_in",
       "At the virtual earth:  I_in = V_in / R_in = I_f"],
   after=["The inversion is a genuine phase reversal, not a sign convention. A positive input "
    "produces a negative output, which matters whenever the stage feeds something polarity "
    "sensitive."]),
  dict(h2="The non-inverting amplifier and the buffer",
   paras=["Taking the signal directly to the non-inverting input and returning feedback through a "
    "divider to the inverting input gives a non-inverting amplifier. Its gain is one plus the "
    "ratio of the feedback resistor to the grounded resistor, so the minimum gain of this "
    "configuration is unity and it cannot attenuate.",
    "Setting the feedback resistor to zero and omitting the grounded resistor gives the voltage "
    "follower, or buffer, with a gain of exactly one. It is used not for gain but for impedance "
    "transformation: it presents a very high impedance to the source and a very low impedance to "
    "the load, so a weak high-impedance signal can drive a substantial load without being "
    "loaded down."],
   eq=["Gain = 1 + R_f / R_g",
       "Buffer:  gain = 1, very high input impedance",
       "Input impedance \u2248 that of the amplifier input itself"],
   fig=("c14_noninv","A non-inverting amplifier. The signal drives the high-impedance input "
     "directly and the divider sets the gain.",46),
   table=(["Configuration","Gain","Input impedance","Phase","Typical use"],
     [["Inverting","\u2212R_f/R_in","R_in","Inverted","Gain, summing, virtual-earth circuits"],
      ["Non-inverting","1 + R_f/R_g","Very high","Preserved","Amplifying a weak source"],
      ["Buffer","1","Very high","Preserved","Impedance transformation"],
      ["Summing","\u2212R_f per input resistor","Each input resistor","Inverted","Mixing signals"],
      ["Difference","Set by matched pairs","Moderate","Differential","Rejecting common-mode noise"]],
     None)),
  dict(h2="Summing and difference amplifiers",
   paras=["Because the virtual earth holds its potential regardless of what is connected to it, "
    "several input resistors can feed the same point without interacting. Each contributes a "
    "current proportional to its own input voltage, the currents add, and the output reflects "
    "their sum. Giving each input a different resistor applies a different weight to it.",
    "A difference amplifier uses both inputs with matched resistor pairs and responds only to the "
    "difference between its two inputs, rejecting any voltage common to both. This is the "
    "standard approach to recovering a small signal from a sensor at the end of a long cable, "
    "where interference appears almost equally on both conductors."],
   eq=["Summing:  V_out = \u2212R_f (V\u2081/R\u2081 + V\u2082/R\u2082 + V\u2083/R\u2083)",
       "Difference:  V_out = (R_f/R_in)(V\u2082 \u2212 V\u2081)   with matched pairs",
       "Common-mode rejection depends on resistor matching"],
   panel=("Common-mode rejection depends on matched components",
     ["Interference on a twisted pair appears almost equally on both conductors.",
      "A difference amplifier subtracts it out, leaving the wanted signal.",
      "Rejection is limited by how closely the two resistor pairs match.",
      "Use close-tolerance resistors, or an instrumentation amplifier, for demanding work."])),
  dict(h2="The comparator and hysteresis",
   paras=["Without feedback, the enormous open-loop gain drives the output to one supply rail or "
    "the other according to which input is higher. This is comparator operation, and it converts "
    "an analogue input into a two-state output, which is how an analogue measurement becomes a "
    "control decision.",
    "A plain comparator chatters when the input hovers near the threshold, because noise repeatedly "
    "crosses it. Adding positive feedback moves the threshold slightly whenever the output "
    "changes, so the input must travel further to switch back. That deliberate gap is hysteresis, "
    "and it is why a thermostat has a dead band rather than buzzing at setpoint."],
   eq=["V_out \u2192 positive rail when V\u207a > V\u207b",
       "V_out \u2192 negative rail when V\u207a < V\u207b",
       "Hysteresis gap set by the positive feedback ratio"],
   fig=("c14_cond","A signal conditioning stage. The sensor output is amplified and compared "
     "against a reference to produce a two-state control output.",46)),
  dict(h2="Practical limits",
   paras=["Real devices depart from the ideal in ways that matter. The output cannot reach beyond "
    "the supply rails, and many types stop short of them, so a circuit designed for a gain that "
    "would demand more output than the supply allows will simply clip. Input offset voltage means "
    "the output is not exactly zero for a zero input, which matters in precision direct-voltage "
    "measurement.",
    "Gain also falls with frequency, so a device with a gain-bandwidth product of one megahertz "
    "gives a gain of a hundred only up to ten kilohertz. Slew rate limits how fast the output can "
    "change regardless of gain, which distorts large fast signals. Each of these is a data-sheet "
    "figure to be checked against the application rather than a defect."],
   bh="Checking a design against real limits",
   bullets=["Confirm the required output swing fits within the supply rails.",
     "Divide the gain-bandwidth product by the gain to find the usable bandwidth.",
     "Check slew rate against the fastest large output change required.",
     "Allow for input offset in precision direct-voltage work.",
     "Provide a path for input bias current at both inputs.",
     "Decouple the supply pins close to the device."]),
 ],
 [ex("Inverting amplifier gain and output",
   "An inverting amplifier has an input resistor of 10 k\u03a9 and a feedback resistor of 220 k\u03a9, "
   "with an input of 45 mV.",
   "The gain, the output voltage, and the stage input impedance.",
   [("Gain","\u2212220/10 = \u221222"),
    ("Output voltage","\u221222 \u00d7 0.045 = \u22120.99 V"),
    ("Input impedance","Equal to the input resistor, 10 k\u03a9"),
    ("Current at the virtual earth","0.045/10 000 = 4.5 \u00b5A")],
   "The output is just under one volt and inverted. Note that the input impedance is only 10 k\u03a9, "
   "so this configuration loads the source; a non-inverting stage would not."),
  ex("Non-inverting amplifier for a sensor",
   "A sensor produces 0 to 120 mV and must drive a 0 to 5 V input. The feedback resistor is to be "
   "a convenient value.",
   "The required gain and a suitable resistor pair.",
   [("Required gain","5/0.120 = 41.7"),
    ("Non-inverting relation","Gain = 1 + R_f/R_g, so R_f/R_g = 40.7"),
    ("Choose R_g","1 k\u03a9"),
    ("Required R_f","40.7 k\u03a9, so use 39 k\u03a9 with a trimmer, or 40.2 k\u03a9 close tolerance"),
    ("Resulting gain with 39 k\u03a9","1 + 39 = 40, giving 4.8 V full scale")],
   "The non-inverting configuration suits a sensor because its input impedance is very high and "
   "it does not load the source. The slight gain shortfall is normally trimmed rather than "
   "accepted."),
  ex("Summing amplifier with unequal weights",
   "A summing amplifier has a 100 k\u03a9 feedback resistor and three inputs through 10 k\u03a9, 20 k\u03a9 "
   "and 50 k\u03a9. The inputs are 0.4 V, 0.8 V and 1.0 V.",
   "The output voltage.",
   [("Contribution from the first input","\u2212(100/10) \u00d7 0.4 = \u22124.0 V"),
    ("Contribution from the second","\u2212(100/20) \u00d7 0.8 = \u22124.0 V"),
    ("Contribution from the third","\u2212(100/50) \u00d7 1.0 = \u22122.0 V"),
    ("Total output","\u22124.0 \u2212 4.0 \u2212 2.0 = \u221210.0 V"),
    ("Supply check","Requires rails beyond \u221210 V")],
   "Each input is weighted by its own resistor and the three contributions simply add. The output "
   "demand of ten volts must be checked against the available supply, or the stage will clip."),
  ex("Bandwidth available at a chosen gain",
   "A device has a gain-bandwidth product of 1.5 MHz and is used at a closed-loop gain of 50.",
   "The usable bandwidth, and the gain available at 100 kHz.",
   [("Bandwidth at a gain of 50","1.5\u00d710\u2076/50 = 30 kHz"),
    ("Gain available at 100 kHz","1.5\u00d710\u2076/100\u00d710\u00b3 = 15"),
    ("Implication","A gain of 50 cannot be achieved at 100 kHz with this device")],
   "Gain and bandwidth trade directly against each other. A design needing both must use a faster "
   "device or distribute the gain across two cascaded stages."),
  ex("Comparator with hysteresis",
   "A comparator operates from 0 to 10 V rails with a reference of 5 V, and positive feedback set "
   "to one fiftieth of the output.",
   "The two thresholds and the hysteresis band.",
   [("Feedback contribution","10/50 = 0.2 V"),
    ("Upper threshold, output low","5 + 0.1 = 5.1 V approximately"),
    ("Lower threshold, output high","5 \u2212 0.1 = 4.9 V approximately"),
    ("Hysteresis band","0.2 V"),
    ("Effect","Input noise below 0.2 V peak to peak cannot cause chatter")],
   "A 0.2 V band is enough to reject typical sensor noise while keeping the control threshold "
   "close to the intended 5 V. Too little hysteresis gives chatter; too much gives a sloppy "
   "control point.")],
 lab("inverting and non-inverting gain, saturation, bandwidth and hysteresis",
  "Verify the predicted gain of inverting and non-inverting configurations, observe clipping "
  "against the supply rails, measure the gain-bandwidth trade-off, then demonstrate comparator "
  "chatter and cure it with hysteresis.",
  ["General-purpose operational amplifier, dual in-line package, with its data sheet.",
   "Split supply, plus and minus 12 V, or a single 12 V supply with a mid-rail reference.",
   "Resistors: 1 k\u03a9, 10 k\u03a9, 22 k\u03a9, 100 k\u03a9, 220 k\u03a9, 1 M\u03a9, close tolerance where "
   "available.",
   "Signal generator with sine and square outputs and a calibrated amplitude.",
   "Two-channel oscilloscope and two multimeters.",
   "Potentiometer, 10 k\u03a9, to provide a slowly varying input.",
   "Decoupling capacitors, 100 nF, for the supply pins."],
  ["Fit the decoupling capacitors across the supply pins before any measurement.",
   "Build the inverting amplifier with a 10 k\u03a9 input resistor and a 100 k\u03a9 feedback resistor.",
   "Apply a 1 kHz sine input of 100 mV peak and measure the output amplitude. Compute the measured "
   "gain and compare with the prediction.",
   "Confirm the phase relationship between input and output on the two oscilloscope channels.",
   "Measure the voltage at the inverting input with respect to the reference and confirm it is "
   "near zero. Record the value.",
   "Increase the input amplitude in steps until the output stops growing. Record the amplitude at "
   "which clipping begins and the clipped output level.",
   "Compare the clipped level with the supply rail voltage.",
   "Change the feedback resistor to 220 k\u03a9 and repeat the gain measurement.",
   "Rebuild as a non-inverting amplifier with 1 k\u03a9 and 22 k\u03a9, measure the gain and confirm "
   "the phase is preserved.",
   "Reconfigure as a buffer and confirm unity gain.",
   "Return to a gain of 100 and sweep the input frequency upward, recording the frequency at "
   "which the output has fallen to 0.707 of its low-frequency value.",
   "Compute the gain-bandwidth product from that result and compare with the data sheet.",
   "Build a comparator with a mid-rail reference and drive the input from the potentiometer.",
   "Turn the potentiometer slowly through the threshold and observe the output on the oscilloscope. "
   "Record whether chatter occurs.",
   "Add a 1 M\u03a9 positive feedback resistor from output to the non-inverting input and repeat. "
   "Measure the two thresholds and compute the hysteresis band."],
  ("c14_inv","The inverting configuration under test. The virtual-earth node is monitored "
   "directly to confirm it remains near reference potential.",46),
  ["Configuration","Predicted gain","Measured gain","Phase","Observation"],
  [["Inverting, 10 k / 100 k","","","",""],["Inverting, 10 k / 220 k","","","",""],
   ["Non-inverting, 1 k / 22 k","","","",""],["Buffer","","","",""],
   ["Clipping onset","","","",""],["Bandwidth at gain of 100","","","",""],
   ["Comparator, no hysteresis","","","",""],["Comparator with hysteresis","","","",""]],
  ["How closely did your measured gains match the resistor ratios, and what accounts for the "
   "difference?",
   "What voltage did you measure at the inverting input during normal operation? Explain why it "
   "stays there without being connected to the reference.",
   "At what output level did clipping begin, and how did that compare with the supply rails? What "
   "does that imply for a design needing a large output swing?",
   "From your bandwidth measurement at a gain of 100, compute the gain-bandwidth product. What "
   "bandwidth would the same device give at a gain of 10?",
   "Why does the non-inverting configuration not load the signal source, while the inverting one "
   "does?",
   "Describe what the comparator output did as the input crossed the threshold without hysteresis, "
   "and explain the cause.",
   "Compute the hysteresis band from your two measured thresholds and compare it with the "
   "prediction from the feedback ratio.",
   "In what application would you deliberately choose a wider hysteresis band, and what is the "
   "penalty?"],
  ["Observe supply polarity carefully; a reversed supply destroys the device immediately.",
   "Keep the input signal within the supply rails at all times.",
   "Fit the supply decoupling capacitors before applying power, or the stage may oscillate.",
   "Do not short the output to either supply rail; many devices tolerate it only briefly.",
   "Return the signal generator amplitude to minimum before changing any connection.",
   "Check that the computed output swing fits the supply before increasing gain."]),
 [["Output sits hard at one supply rail","No negative feedback path, or an input outside the "
   "permitted range","Check the feedback resistor is fitted and measure both input voltages",
   "Restore the feedback path and bring the inputs within range"],
  ["Output waveform is flat topped","Required output swing exceeds the supply rails",
   "Compare the predicted output amplitude with the rail voltages","Reduce the gain or raise the "
   "supply voltage"],
  ["Gain falls off well below the expected frequency","Gain-bandwidth product exceeded at the "
   "chosen gain","Divide the data-sheet product by the closed-loop gain","Use a faster device or "
   "split the gain across two stages"],
  ["Large fast signals are distorted while small ones are clean","Slew-rate limiting","Compare "
   "the required rate of output change with the data-sheet slew rate","Select a device with a "
   "higher slew rate or reduce the signal amplitude"],
  ["Stage oscillates with no signal applied","Inadequate supply decoupling or stray feedback "
   "through the layout","Observe the output with the input grounded","Fit decoupling capacitors "
   "at the supply pins and shorten feedback wiring"],
  ["Comparator output chatters near the threshold","No hysteresis, so input noise crosses the "
   "threshold repeatedly","Observe the input and output together on an oscilloscope","Add a "
   "positive feedback resistor to establish a hysteresis band"],
  ["Precision direct-voltage reading has a constant error","Input offset voltage amplified by the "
   "stage gain","Short the input and measure the residual output","Use an offset trim, or select "
   "a low-offset device"],
  ["Difference stage passes interference as well as signal","Resistor pairs not matched closely "
   "enough","Measure the output with both inputs tied together and driven","Fit close-tolerance "
   "matched resistors or an instrumentation amplifier"]],
 ("c14_cond","Signal conditioning under test. The amplified sensor signal and the comparator "
  "output are observed together to confirm the switching thresholds.",46),
 ["Fit supply decoupling capacitors at the device pins as a matter of routine, not as a cure "
  "after oscillation appears.",
  "Check the required output swing against the supply rails before selecting a gain.",
  "Divide the gain-bandwidth product by the intended gain early in the design, not after testing.",
  "Add deliberate hysteresis to every comparator that drives a contactor or a relay.",
  "Use close-tolerance matched resistors wherever common-mode rejection matters."],
 ["State which input of an operational amplifier produces a phase-inverted output.",
  "State the two ideal assumptions used to analyse feedback amplifier circuits.",
  "Find the gain of an inverting amplifier with a 4.7 k\u03a9 input and a 47 k\u03a9 feedback resistor.",
  "Find the output voltage of the stage above for a 60 mV input.",
  "Find the gain of a non-inverting amplifier with 2.2 k\u03a9 and 68 k\u03a9.",
  "State the gain of a voltage follower and its purpose.",
  "Explain what a virtual earth is and why it occurs.",
  "A summing amplifier has a 68 k\u03a9 feedback resistor and inputs through 10 k\u03a9 and 22 k\u03a9 at "
  "0.3 V and 0.5 V. Find the output.",
  "State the minimum gain achievable with the non-inverting configuration and explain why.",
  "A device has a gain-bandwidth product of 4 MHz. Find the bandwidth at a gain of 80.",
  "Explain why an amplifier output clips, and what determines the clipping level.",
  "State the purpose of hysteresis in a comparator and one consequence of omitting it.",
  "Explain why a difference amplifier rejects interference picked up on a long sensor cable.",
  "State which configuration you would choose to amplify a high-impedance sensor, and why.",
  "Explain why input offset voltage matters more in direct-voltage measurement than in audio work."],
 [["1","The inverting input","Signal applied there appears inverted at the output"],
  ["2","Inputs draw no current; feedback equalises the input voltages","These two permit analysis "
   "with Ohm's law alone"],
  ["3","\u221210","Gain = \u2212R_f/R_in"],
  ["4","\u22120.6 V","Output = gain \u00d7 input"],
  ["5","31.9","Gain = 1 + R_f/R_g"],
  ["6","Unity; impedance transformation","It presents high impedance to the source and low "
   "impedance to the load"],
  ["7","A node held at reference potential by feedback","Feedback drives the output until the "
   "inverting input matches the non-inverting input"],
  ["8","\u22123.59 V","\u2212(68/10)(0.3) \u2212 (68/22)(0.5)"],
  ["9","Unity","The relation 1 + R_f/R_g cannot fall below one, so it cannot attenuate"],
  ["10","50 kHz","Bandwidth = product divided by gain"],
  ["11","The demanded output exceeds the rails","The supply voltage, less the device's rail "
   "shortfall, sets the limit"],
  ["12","To prevent chatter near the threshold","Without it, input noise repeatedly crosses the "
   "threshold and the output oscillates"],
  ["13","Interference appears equally on both conductors","The stage responds only to the "
   "difference, so the common part is subtracted out"],
  ["14","Non-inverting or buffer","Its very high input impedance does not load the source"],
  ["15","Offset is indistinguishable from a small direct signal","Audio coupling removes the "
   "steady component, but a direct measurement carries the offset as an error"]],
 ["An operational amplifier has very high open-loop gain, which feedback trades for predictable "
  "closed-loop behaviour set by external resistors.",
  "The two ideal assumptions, negligible input current and equal input voltages under feedback, "
  "allow analysis with Ohm's law.",
  "Inverting gain is the resistor ratio with inversion, and the input impedance equals the input "
  "resistor.",
  "Non-inverting gain is one plus the resistor ratio, cannot fall below unity, and presents a "
  "very high input impedance.",
  "The virtual earth lets several weighted inputs be summed without interaction.",
  "A difference amplifier rejects common-mode interference to the extent that its resistor pairs "
  "match.",
  "Without feedback the device acts as a comparator, and hysteresis is needed to prevent chatter.",
  "Supply rails, offset, gain-bandwidth product and slew rate are the practical limits to check."],
 [["Differential gain","V_out = A(V\u207a \u2212 V\u207b)","Open loop"],
  ["Inverting gain","Gain = \u2212R_f/R_in","Inverting configuration"],
  ["Non-inverting gain","Gain = 1 + R_f/R_g","Non-inverting configuration"],
  ["Summing output","V_out = \u2212R_f \u03a3(V\u2099/R\u2099)","Virtual-earth summing node"],
  ["Difference output","V_out = (R_f/R_in)(V\u2082 \u2212 V\u2081)","Matched resistor pairs"],
  ["Usable bandwidth","BW = GBP / gain","Closed-loop operation"],
  ["Input impedance, inverting","Z_in = R_in","Inverting configuration"]],
 [["Open-loop gain","The device's own gain before feedback is applied"],
  ["Closed-loop gain","The gain of the complete circuit, set by external components"],
  ["Virtual earth","A node held at reference potential by feedback rather than by connection"],
  ["Buffer","A unity-gain stage used to transform impedance"],
  ["Common-mode rejection","The ability to ignore a voltage present equally on both inputs"],
  ["Hysteresis","A deliberate gap between a comparator's rising and falling thresholds"],
  ["Slew rate","The maximum rate at which the output voltage can change"],
  ["Gain-bandwidth product","The constant relating achievable gain to available bandwidth"]],
 "A comparator turns an analogue quantity into a two-state output. Once signals are reduced to "
 "two states, they can be combined by logic rules rather than by Ohm's law, which is the subject "
 "of the next chapter.",
)
