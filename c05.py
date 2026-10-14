# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH5=mkch(5,"Inductors and RL circuits",
 "Stored magnetic energy, induced voltage, and why switching inductive loads is violent",
 "An inductor opposes change in current. That opposition stores energy in a magnetic field and, "
 "when a switch interrupts the current, releases it as a voltage spike many times the supply. "
 "Understanding this explains contact erosion, relay suppression diodes and most switching damage.",
 ["State what inductance measures and compute induced voltage from a rate of current change.",
  "Compute stored magnetic energy and the time constant of an RL circuit.",
  "Explain why interrupting inductive current produces a large reverse voltage.",
  "Select and connect a suppression diode across a DC coil correctly.",
  "Recognise inductive behaviour in chokes, coils, contactors and motor windings."],
 ("c5_rl","An RL circuit. The inductor opposes the change in current, so the current rises "
  "exponentially rather than instantly.",46),
 [dict(h2="Inductance and induced voltage",
   paras=["Inductance, symbol <i>L</i>, measured in henries, relates the voltage induced across "
    "a coil to the rate of change of current through it. A one-henry inductor develops one volt "
    "when the current changes at one ampere per second. The induced voltage opposes the change "
    "that produced it, which is Lenz's law and the reason inductors are said to resist change.",
    "The practical consequence is immediate: the faster you try to change the current, the larger "
    "the voltage that appears. A switch opening a coil circuit attempts to bring the current to "
    "zero in microseconds, so the induced voltage can reach hundreds or thousands of volts even "
    "from a 24 V supply."],
   eq=["v = L (di/dt)",
       "W = \u00bd L I\u00b2"],
   panel=("Why relay contacts erode",
     ["Opening a coil circuit forces a very large di/dt, so v = L di/dt becomes large.",
      "The resulting voltage strikes an arc across the opening contacts.",
      "The arc carries the stored energy \u00bdLI\u00b2 into the contact metal, eroding it."])),
  dict(h2="Combining inductors, and the RL time constant",
   paras=["Inductors in series add and in parallel combine reciprocally, following the same "
    "pattern as resistors. The arithmetic is only valid when the coils share no magnetic "
    "coupling; coupled coils must be treated as a transformer instead.",
    "In an RL circuit the time constant is the inductance divided by the resistance. The current "
    "rises toward its final value with the same exponential shape as capacitor voltage, reaching "
    "63.2 per cent in one time constant and effectively settling after five. Note that raising "
    "the resistance shortens an RL transient, the opposite of the RC case."],
   eq=["Series:  L_eq = \u03a3 L      Parallel: 1/L_eq = \u03a3 1/L",
       TAU+" = L / R",
       "i(t) = (V/R)(1 \u2212 e^(\u2212t/"+TAU+"))"],
   fig=("c5_choke","A choke in a supply line. It passes direct current but opposes rapid changes, "
     "which is the basis of inductive filtering.",44)),
  dict(h2="Limiting behaviour at the two instants",
   paras=["At the first instant after switching, an inductor carrying no current behaves as an "
    "open circuit, because any sudden current would demand an infinite voltage. At steady state, "
    "with current no longer changing, it behaves as a plain resistance equal to its winding "
    "resistance. These are the mirror image of the capacitor's limits.",
    "Knowing both limits lets you solve any RL problem by inspection: find the initial condition, "
    "find the final condition, and join them with the exponential governed by L over R."],
   table=(["Element","At the first instant","At steady state","Energy stored in"],
     [["Capacitor, uncharged","Short circuit","Open circuit","Electric field"],
      ["Capacitor, charged","Source at its stored voltage","Open circuit","Electric field"],
      ["Inductor, no current","Open circuit","Winding resistance only","Magnetic field"],
      ["Inductor, carrying current","Source holding that current","Winding resistance only","Magnetic field"]],None)),
  dict(h2="Suppressing the switching transient",
   paras=["A diode connected across a DC coil, reverse biased in normal operation, provides a "
    "path for the inductor current the instant the switch opens. The current circulates through "
    "the diode and decays harmlessly, clamping the coil voltage to roughly one diode drop above "
    "the supply. This is the flyback or freewheel diode, and fitting it correctly is one of the "
    "highest-value habits in control wiring.",
    "Polarity is critical. Connected the wrong way the diode short circuits the supply through "
    "the coil and will fail immediately, usually taking the driving transistor with it. On AC "
    "coils a diode cannot be used; a resistor-capacitor snubber or a varistor is fitted instead."],
   fig=("c5_flyback","A flyback diode across a DC coil. The diode is reverse biased while the "
     "coil is energised and conducts only during the switching transient.",46),
   bh="Suppression choices by supply type",
   bullets=["DC coil: a diode across the coil, cathode to the positive side.",
     "AC coil: a resistor-capacitor snubber across the contacts or the coil.",
     "Either: a varistor across the coil, clamping both polarities at a chosen voltage.",
     "Semiconductor drivers: many include an internal clamp, but check before relying on it."]),
  dict(h2="Where inductance appears in practice",
   paras=["Deliberate inductance appears in chokes, filter reactors, ballasts, relay and "
    "contactor coils, solenoids and transformer windings. Incidental inductance appears in every "
    "conductor loop, which is why high-current cable runs are kept close together and why "
    "long leads cause ringing on fast switching edges.",
    "Motor windings are strongly inductive, which is why a motor draws a large starting current "
    "that lags the voltage, and why opening a motor circuit under load stresses the switching "
    "device far more than opening a resistive one of the same rating."],
   panel=("Reading a component as its model",
     ["A coil is an inductance in series with its own winding resistance, so an ohmmeter reads "
      "the resistance only.",
      "An open coil reads infinite resistance; a shorted turn reads lower than the nameplate value.",
      "Winding resistance alone cannot confirm inductance, but it does find most coil faults."])),
 ],
 [ex("Induced voltage from a switching event",
   "A 0.4 H coil carries 2 A. A switch reduces the current to zero in 1 ms.",
   "The average induced voltage and the energy that must be absorbed.",
   [("Rate of current change","di/dt = 2 / 0.001 = 2000 A/s"),
    ("Induced voltage","v = L di/dt = 0.4 \u00d7 2000 = 800 V"),
    ("Stored energy","W = \u00bd L I\u00b2 = 0.5 \u00d7 0.4 \u00d7 4 = 0.8 J")],
   "800 V from a low-voltage supply is why an unsuppressed coil destroys contacts and "
   "semiconductors. A flyback diode diverts the 0.8 J into the coil's own resistance instead."),
  ex("RL time constant and current rise",
   "A 250 mH coil of 50 "+OH+" winding resistance is connected to 24 V.",
   "The time constant, the final current, and the current after 5 ms.",
   [("Time constant","\u03c4 = L/R = 0.25/50 = 5 ms"),
    ("Final current","I = V/R = 24/50 = 0.48 A"),
    ("Current at one time constant","i = 0.48 \u00d7 0.632 = 0.303 A"),
    ("Time to settle","5\u03c4 = 25 ms")],
   "Note that raising the resistance would shorten the transient and lower the final current, "
   "the opposite of the RC relationship where resistance lengthens the transient."),
  ex("Sizing a flyback diode",
   "A 24 V contactor coil draws 150 mA and has an inductance of 1.2 H.",
   "The diode's required reverse voltage and forward current, and the decay time constant.",
   [("Reverse voltage seen in normal operation","24 V, so choose at least 100 V rating"),
    ("Forward current at the instant of switching","Equal to the coil current, 150 mA"),
    ("Coil resistance","R = 24/0.15 = 160 "+OH),
    ("Decay time constant","\u03c4 = 1.2/160 = 7.5 ms"),
    ("Energy dissipated per operation","W = \u00bd \u00d7 1.2 \u00d7 0.15\u00b2 = 13.5 mJ")],
   "A 1 A 100 V diode is ample. The decay takes about 37 ms to complete, which slightly delays "
   "contactor drop-out, a known and usually acceptable side effect of freewheel suppression.")],
 lab("current rise in an inductive circuit and the effect of a flyback diode",
  "Observe that current in an inductive branch rises gradually rather than instantly, measure the "
  "time constant, and demonstrate that a correctly connected diode removes the switching spike.",
  ["DC supply, 24 V, current limited to 0.5 A.",
   "Inductor or relay coil of known inductance, roughly 0.1\u20131 H, with its resistance measured.",
   "Series resistor, 100 "+OH+" 1 W, used as a current-sensing shunt.",
   "Oscilloscope, or a multimeter with a peak-hold function.",
   "Diode, 1N4007 or similar, and a toggle switch."],
  ["Measure and record the coil resistance and the series resistor value.",
   "Compute the expected time constant from L over the total circuit resistance.",
   "Wire the coil in series with the 100 "+OH+" resistor and the switch across the supply.",
   "Connect the oscilloscope across the 100 "+OH+" resistor, so the trace shows current directly.",
   "Close the switch and capture the rising current. Measure the time to 63 % of final.",
   "Move the oscilloscope across the switch contacts and capture the voltage when the switch opens.",
   "Record the peak voltage observed. This is the unsuppressed transient.",
   "Fit the diode across the coil, cathode to the positive side, and repeat the opening capture.",
   "Reverse the diode briefly only as a thought exercise on paper; do not actually energise it reversed."],
  ("c5_flyback","The test circuit. The sensing resistor converts current to a voltage the "
   "instrument can display, and the diode is fitted across the coil only.",46),
  ["Condition","Peak switch voltage (V)","Time to 63 % (ms)","Predicted \u03c4 (ms)","Comment"],
  [["No diode, closing","\u2014","","",""],["No diode, opening","","\u2014","",""],
   ["Diode fitted, opening","","\u2014","",""],["Diode fitted, closing","\u2014","","",""],
   ["Repeat, no diode","","","",""],["Repeat, diode","","","",""]],
  ["By what factor did the diode reduce the peak switching voltage?",
   "Did fitting the diode change the current rise on closing? Explain why or why not.",
   "Compute the coil inductance implied by your measured time constant and compare it with the "
   "marked value.",
   "Explain, using v = L di/dt, why the opening transient is far larger than the closing one.",
   "What would happen electrically if the diode were connected the other way round, and which "
   "component would fail first?"],
  ["Keep the supply at 24 V with the current limit at 0.5 A.",
   "The unsuppressed opening transient can exceed several hundred volts at the switch; do not "
   "touch the contacts while switching.",
   "Observe diode polarity. A reversed diode becomes a short circuit across the supply.",
   "The coil stores energy; allow it to decay before disconnecting."]),
 [["Relay contacts pitted and welding after short service","Unsuppressed inductive switching "
   "transient and arcing","Observe the switch voltage on an oscilloscope while opening","Fit a "
   "flyback diode on DC, or a snubber or varistor on AC"],
  ["Driving transistor fails repeatedly on a coil output","Missing or reversed suppression diode",
   "Check the diode's presence and polarity against the drawing","Fit the diode with its cathode "
   "to the positive supply"],
  ["Coil reads open on an ohmmeter","Broken winding or an open internal joint","Measure resistance "
   "at the coil terminals de-energised","Replace the coil or the whole device"],
  ["Coil resistance well below the nameplate value","Shorted turns from insulation failure",
   "Compare with a known good coil of the same part number","Replace; do not attempt repair"],
  ["Contactor drops out sluggishly after a diode was added","Freewheel current sustains the coil "
   "flux briefly","Measure the decay time against the mechanical requirement","Accept it, or use "
   "a varistor instead for faster clamping"],
  ["Electronic equipment misbehaves when a nearby coil switches","Radiated or conducted switching "
   "transient","Correlate the fault with the switching event","Suppress at the source and separate "
   "the wiring routes"]],
 ("c5_rl","Measuring an inductive transient. A sensing resistor converts the branch current into "
  "a voltage the instrument can record.",46),
 ["Fit suppression at the coil, not at the panel; the transient must be clamped where it is generated.",
  "Check diode polarity twice before energising a coil output; a reversed diode is an immediate "
  "short circuit.",
  "Measure coil resistance when a device misbehaves; it finds open and shorted windings quickly.",
  "Expect inductive loads to stress switchgear far more than resistive loads of the same current "
  "rating."],
 ["A 0.8 H coil's current changes at 50 A/s. Find the induced voltage.",
  "Find the energy stored in a 0.5 H inductor carrying 3 A.",
  "Find the time constant of a 400 mH coil with 80 "+OH+" total circuit resistance.",
  "A 12 V supply feeds a 100 mH coil of 24 "+OH+". Find the final current and the time constant.",
  "Find the equivalent of 100 mH and 150 mH in series, and in parallel.",
  "A coil carrying 1.5 A has its current interrupted in 0.5 ms. With L = 0.3 H, find the induced "
  "voltage.",
  "State the correct polarity for a flyback diode across a DC coil and explain why.",
  "Explain why a diode cannot be used to suppress an AC-operated coil.",
  "An RL circuit reaches 95 % of final current in 60 ms. Find its time constant.",
  "A motor winding measures 3.2 "+OH+" cold. State two separate faults that would make it read "
  "much lower, and how you would distinguish them."],
 [["1","40 V","v = L di/dt"],
  ["2","2.25 J","W = \u00bdLI\u00b2"],
  ["3","5 ms","\u03c4 = L/R"],
  ["4","0.5 A; 4.17 ms","I = V/R, then \u03c4 = L/R"],
  ["5","250 mH series; 60 mH parallel","Series adds; parallel is reciprocal"],
  ["6","900 V","di/dt = 3000 A/s, then v = L di/dt"],
  ["7","Cathode to the positive side, reverse biased when energised","It then conducts only when "
   "the coil voltage reverses at switch-off"],
  ["8","The diode would conduct on alternate half cycles","It would short the supply for half of "
   "every cycle, so a snubber or varistor is used instead"],
  ["9","20 ms","95 % corresponds to three time constants"],
  ["10","Shorted turns, or a measurement across the wrong terminals","Compare against a known "
   "good machine and verify the terminal identification first"]],
 ["Inductance relates induced voltage to the rate of change of current, so fast changes produce "
  "large voltages.",
  "Stored magnetic energy is \u00bdLI\u00b2 and must go somewhere when the circuit is interrupted.",
  "The RL time constant is L over R, so increasing resistance shortens the transient.",
  "An inductor is momentarily an open circuit and eventually just its winding resistance, the "
  "mirror of a capacitor.",
  "A correctly polarised flyback diode clamps DC coil transients; AC coils need a snubber or varistor.",
  "Inductive loads stress contacts and semiconductors far more than resistive loads of equal current."],
 [["Induced voltage","v = L di/dt","Any inductance with changing current"],
  ["Stored energy","W = \u00bdLI\u00b2","Inductor carrying a steady current"],
  ["Time constant",TAU+" = L/R","Single inductance with series resistance"],
  ["Current rise","i = (V/R)(1 \u2212 e^(\u2212t/"+TAU+"))","From zero initial current"],
  ["Series inductance","L_eq = \u03a3 L","Uncoupled coils"],
  ["Parallel inductance","1/L_eq = \u03a3 1/L","Uncoupled coils"]],
 [["Inductance","The property relating induced voltage to the rate of change of current"],
  ["Lenz's law","The induced voltage opposes the change in current that produced it"],
  ["Flyback diode","A diode across a DC coil that carries the current during switch-off"],
  ["Snubber","A resistor-capacitor network that absorbs a switching transient"],
  ["Varistor","A voltage-dependent resistor that clamps transients of either polarity"]],
 "Capacitors and inductors both respond to change rather than to steady values. The next chapter "
 "introduces alternating current, where the voltage changes continuously, and develops the "
 "language of frequency, phase and root-mean-square values.",
)
