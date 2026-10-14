# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH4=mkch(4,"Capacitors and RC circuits",
 "Stored charge, stored energy, and circuits whose behaviour unfolds over time",
 "A capacitor is the first element whose current depends not on the voltage across it but on how "
 "fast that voltage is changing. That single difference introduces time into circuit analysis "
 "and underlies timing, filtering, smoothing and every transient you will meet.",
 ["State what capacitance measures and compute stored charge and energy.",
  "Combine capacitors in series and parallel, noting that the rules invert the resistor rules.",
  "Compute the time constant of an RC circuit and sketch charge and discharge curves.",
  "Predict the voltage or current at a stated number of time constants.",
  "Discharge and test a capacitor safely before handling it."],
 ("c4_rc","An RC charging circuit. The resistor limits the rate at which charge accumulates, so "
  "the capacitor voltage rises exponentially toward the supply.",46),
 [dict(h2="Capacitance, charge and stored energy",
   paras=["Capacitance, symbol <i>C</i>, is the charge stored per volt applied, measured in "
    "farads. One farad is one coulomb per volt, an enormous quantity, so practical values run "
    "from picofarads to millifarads. A capacitor stores energy in the electric field between its "
    "plates, and that energy is proportional to the square of the voltage.",
    "Because the energy depends on voltage squared, a capacitor charged to twice the voltage "
    "holds four times the energy. This is why a large capacitor in a drive or power supply "
    "remains a genuine hazard after the supply is removed, and why discharge is a required step "
    "rather than a precaution."],
   eq=["C = Q / V          Q = C V",
       "W = \u00bd C V\u00b2"],
   panel=("Capacitor discharge is a safety step, not an optional one",
     ["A 1000 \u00b5F capacitor at 400 V stores 80 J, enough to cause serious injury.",
      "Discharge through a resistor sized for the energy, never by shorting with a screwdriver.",
      "Verify zero volts with a meter after discharging, then verify the meter on a known source."])),
  dict(h2="Combining capacitors",
   paras=["Capacitors in parallel add, because the plate areas effectively add. Capacitors in "
    "series combine reciprocally, because the same charge must pass through each and the voltages "
    "add. The rules are therefore exactly the inverse of the resistor rules, which is worth "
    "stating explicitly because it is a common examination trap.",
    "A practical consequence is that series capacitors divide the applied voltage in inverse "
    "proportion to their capacitance, so the smallest capacitor sees the largest voltage. "
    "Equalising resistors are fitted across series electrolytics for exactly this reason."],
   eq=["Parallel:  C_eq = C\u2081 + C\u2082 + ... + C_n",
       "Series:    1/C_eq = 1/C\u2081 + 1/C\u2082 + ... + 1/C_n"],
   fig=("c4_cseries","Series and parallel capacitor groups. In series the same charge passes "
     "through each, so the smallest capacitance takes the largest share of the voltage.",46)),
  dict(h2="The time constant",
   paras=["When a capacitor charges through a resistance the product of the two has units of "
    "time and is called the time constant, written "+TAU+". It is the time to reach about 63.2 "
    "per cent of the final change, and the curve is effectively complete after five time "
    "constants, by which point 99.3 per cent of the change has occurred.",
    "The same time constant governs charging and discharging. On discharge the voltage falls to "
    "36.8 per cent of its initial value in one time constant. Memorising the five-step table "
    "below lets you read any RC transient without a calculator."],
   eq=[TAU+" = R C",
       "Charging:    v(t) = V(1 \u2212 e^(\u2212t/"+TAU+"))",
       "Discharging: v(t) = V\u2080 e^(\u2212t/"+TAU+")"],
   table=(["Elapsed time","Charged to","Remaining on discharge","Practical reading"],
     [["1 "+TAU,"63.2 %","36.8 %","Clearly rising, far from final"],
      ["2 "+TAU,"86.5 %","13.5 %","Most of the change has happened"],
      ["3 "+TAU,"95.0 %","5.0 %","Within 5 % of final"],
      ["4 "+TAU,"98.2 %","1.8 %","Indistinguishable on most meters"],
      ["5 "+TAU,"99.3 %","0.7 %","Treated as complete"]],None)),
  dict(h2="Current during a transient",
   paras=["At the instant of switching, an uncharged capacitor behaves as a short circuit: the "
    "full supply appears across the resistor and the current is at its maximum. As the capacitor "
    "charges the resistor voltage falls and so does the current, decaying with the same time "
    "constant. Once fully charged the capacitor passes no steady current at all, behaving as an "
    "open circuit to DC.",
    "These two limiting behaviours, short circuit at the first instant and open circuit at steady "
    "state, let you find the initial and final conditions of any RC circuit without solving a "
    "differential equation. The exponential simply connects the two."],
   eq=["i(0) = V / R          i(t) = (V/R) e^(\u2212t/"+TAU+")",
       "Steady state: i = 0, v_C = V"],
   fig=("c4_timing","Voltage and current during charging. The current starts at its maximum and "
     "decays as the capacitor voltage rises.",46),
   panel=("Two limits that solve most problems by inspection",
     ["At t = 0 an uncharged capacitor is a short circuit, so all the supply is across the resistance.",
      "At steady state a capacitor is an open circuit, so no current flows in its branch.",
      "Find both limits first, then join them with the exponential."])),
  dict(h2="Practical capacitors and their imperfections",
   paras=["A real capacitor is not purely capacitive. It has series resistance, which causes "
    "heating under ripple current, leakage resistance, which slowly discharges it, and series "
    "inductance, which limits its high-frequency usefulness. Electrolytic types are polarised "
    "and will fail, sometimes violently, if reverse connected.",
    "Capacitors also age. An electrolytic that has lost electrolyte shows reduced capacitance and "
    "raised series resistance, which in a power supply appears as excessive output ripple long "
    "before the part fails outright. Measuring series resistance is therefore more diagnostic "
    "than measuring capacitance alone."],
   table=(["Type","Typical range","Polarised","Common application"],
     [["Ceramic","1 pF \u2013 1 \u00b5F","No","Decoupling, high frequency"],
      ["Film","1 nF \u2013 10 \u00b5F","No","Timing, audio, motor run"],
      ["Aluminium electrolytic","1 \u00b5F \u2013 10 mF","Yes","Smoothing, bulk storage"],
      ["Tantalum","0.1 \u00b5F \u2013 100 \u00b5F","Yes","Compact decoupling"],
      ["Motor start","20 \u00b5F \u2013 400 \u00b5F","No","Single-phase motor starting"]],None)),
 ],
 [ex("Charge and energy stored",
   "A 470 \u00b5F capacitor is charged to 25 V.",
   "The stored charge and the stored energy.",
   [("Charge from capacitance and voltage","Q = C V = 470\u00d710\u207b\u2076 \u00d7 25 = 0.01175 C"),
    ("Energy from the square law","W = \u00bd C V\u00b2 = 0.5 \u00d7 470\u00d710\u207b\u2076 \u00d7 625"),
    ("Evaluate","W = 0.147 J")],
   "Doubling the voltage to 50 V would give 0.587 J, four times the energy, confirming the square "
   "law. At 400 V the same capacitor would hold 37.6 J, firmly in hazardous territory."),
  ex("Time constant and charging time",
   "A 100 \u00b5F capacitor charges through 10 k"+OH+" from a 12 V supply.",
   "The time constant, the voltage after 1 s, and the time to reach 95 % of final.",
   [("Time constant","\u03c4 = R C = 10 000 \u00d7 100\u00d710\u207b\u2076 = 1.0 s"),
    ("Voltage after one time constant","v = 12(1 \u2212 e\u207b\u00b9) = 12 \u00d7 0.632 = 7.58 V"),
    ("Time to 95 %","three time constants = 3.0 s"),
    ("Initial current","i(0) = 12/10 000 = 1.2 mA")],
   "Using the cancelling pair \u00b5F \u00d7 k\u03a9 = ms: 100 \u00d7 10 = 1000 ms = 1 s, which "
   "confirms the time constant without powers of ten."),
  ex("Series capacitors sharing voltage",
   "A 10 \u00b5F and a 22 \u00b5F capacitor are connected in series across 200 V.",
   "The equivalent capacitance and the voltage across each.",
   [("Series combination","1/C = 1/10 + 1/22 = 0.1455 per \u00b5F"),
    ("Equivalent","C_eq = 6.875 \u00b5F"),
    ("Charge is common","Q = C_eq V = 6.875\u00d710\u207b\u2076 \u00d7 200 = 1.375 mC"),
    ("Voltage on each","V\u2081\u2080 = 1.375 m/10 \u00b5 = 137.5 V ; V\u2082\u2082 = 1.375 m/22 \u00b5 = 62.5 V")],
   "137.5 + 62.5 = 200 V, satisfying KVL. The smaller capacitor carries the larger voltage, so "
   "its voltage rating governs the design."),
  ex("Discharge to a safe level",
   "A 1000 \u00b5F capacitor at 320 V is discharged through a 2.2 k"+OH+" bleed resistor.",
   "The time constant, the time to fall below 50 V, and the peak power in the resistor.",
   [("Time constant","\u03c4 = 2200 \u00d7 1000\u00d710\u207b\u2076 = 2.2 s"),
    ("Required ratio","50/320 = 0.156, and ln(1/0.156) = 1.86"),
    ("Time to 50 V","t = 1.86 \u00d7 2.2 = 4.1 s"),
    ("Peak resistor power","P = V\u00b2/R = 320\u00b2/2200 = 46.5 W momentarily")],
   "The resistor must tolerate a brief 46.5 W pulse even though the average is low. Verify zero "
   "with a meter after discharging; never assume the bleed resistor is intact.")],
 lab("charging and discharging a capacitor through a known resistance",
  "Measure a charge and a discharge curve, extract the time constant from the data, and compare "
  "it with the product of the measured resistance and capacitance.",
  ["DC supply, 12 V regulated.",
   "Capacitor, 1000 \u00b5F electrolytic, voltage rating at least 25 V.",
   "Resistors, 10 k"+OH+" and 22 k"+OH+", 0.5 W.",
   "Multimeter with at least 1 M"+OH+" input resistance, and a stopwatch.",
   "SPDT switch, or a flying lead used carefully, and a 1 k"+OH+" bleed resistor."],
  ["Measure and record the resistor and capacitor values. Compute the expected time constant "
   "before building anything.",
   "Observe polarity: the electrolytic's negative terminal goes to the reference node.",
   "Wire the capacitor in series with the 10 k"+OH+" resistor, with the switch selecting either "
   "the supply or a short to the reference through the resistor.",
   "Connect the voltmeter directly across the capacitor and leave it there for the whole run.",
   "With the capacitor discharged, switch to the supply and start the stopwatch together.",
   "Record the capacitor voltage every 2 s for 60 s.",
   "Switch to the discharge position and record every 2 s for a further 60 s.",
   "Repeat the charge run with the 22 k"+OH+" resistor and compare the two time constants.",
   "Discharge fully through the bleed resistor and verify zero volts before dismantling."],
  ("c4_rc","The charge and discharge arrangement. The voltmeter stays across the capacitor "
   "throughout, and its input resistance appears in parallel with the capacitor.",46),
  ["Time (s)","Charge v (V)","Predicted v (V)","Discharge v (V)","Predicted v (V)"],
  [["0","","0.00","","12.00"],["5","","","",""],["10","","7.58","",""],
   ["20","","","",""],["30","","11.40","",""],["60","","11.97","",""]],
  ["From your charge data, read the time to reach 7.58 V. How does it compare with the computed "
   "time constant?",
   "From your discharge data, read the time to fall to 4.42 V. Does it match the same time constant?",
   "Your voltmeter's input resistance is in parallel with the capacitor during discharge. "
   "Estimate the error it introduces.",
   "Compare the two time constants from the 10 k"+OH+" and 22 k"+OH+" runs. Is the ratio what "
   "you expected?",
   "Electrolytic capacitors are often 20 % tolerance. Compute the capacitance implied by your "
   "measured time constant and compare it with the marked value."],
  ["The electrolytic is polarised. Reverse connection can cause it to vent or burst.",
   "Keep the supply at 12 V; this activity does not require or permit higher voltages.",
   "Discharge through the bleed resistor and confirm zero volts before touching the terminals.",
   "Do not short the capacitor with a tool; the current is high enough to weld and to spray metal."]),
 [["Capacitor voltage rises far more slowly than predicted","Capacitance higher than marked, or "
   "resistance higher than measured","Measure both components and recompute the time constant",
   "Use measured values; replace the component if it is out of tolerance"],
  ["Capacitor will not hold charge after the supply is removed","Internal leakage, or the "
   "voltmeter is loading it","Disconnect the meter and retest after a delay","Replace a leaky "
   "capacitor; use a higher impedance meter"],
  ["Power supply output ripple has risen over time","Smoothing electrolytic has lost capacitance "
   "and gained series resistance","Measure ripple on the rail and the capacitor's series "
   "resistance","Replace the electrolytic with an equal or better ripple rating"],
  ["Electrolytic is swollen or has vented","Reverse polarity, overvoltage or excessive ripple "
   "heating","Inspect, then confirm the applied polarity and voltage","Replace and correct the "
   "cause before re-energising"],
  ["Series electrolytics fail one at a time","Unequal voltage sharing, so one exceeded its rating",
   "Measure the voltage across each while energised","Fit equalising resistors across each capacitor"],
  ["Motor will not start, run capacitor suspected","Open or low-capacitance run capacitor",
   "Discharge, then measure capacitance out of circuit","Replace with the same microfarad and "
   "voltage rating"]],
 ("c4_timing","Reading a transient on an instrument. The time constant is found from the 63 % "
  "point on charge or the 37 % point on discharge.",46),
 ["Treat every large capacitor as charged until you have discharged it and verified zero.",
  "Record the resistance and capacitance you actually measured, not the printed values.",
  "When a transient looks wrong, check the meter's input resistance before suspecting the circuit.",
  "On a power supply, measure ripple rather than capacitance; it fails first and is easier to see."],
 ["A 220 \u00b5F capacitor is charged to 40 V. Find the stored charge and energy.",
  "Find the equivalent of 10 \u00b5F and 15 \u00b5F in parallel, and in series.",
  "Find the time constant of 47 k"+OH+" with 10 \u00b5F.",
  "A 22 \u00b5F capacitor charges through 100 k"+OH+" from 15 V. Find the voltage after 2.2 s.",
  "How long does a transient take to be 99 % complete, in time constants?",
  "A capacitor discharges from 100 V to 36.8 V in 0.5 s. Find the time constant.",
  "Two capacitors, 4.7 \u00b5F and 1 \u00b5F, are in series across 150 V. Find the voltage across each.",
  "Find the initial current when an uncharged 100 \u00b5F capacitor is connected through 470 "+OH+" to 24 V.",
  "Explain why a capacitor passes no steady DC current but does pass alternating current.",
  "A 2200 \u00b5F capacitor at 400 V must reach under 60 V within 5 s. Find the largest bleed resistor."],
 [["1","8.8 mC; 0.176 J","Q = CV, then W = \u00bdCV\u00b2"],
  ["2","25 \u00b5F parallel; 6 \u00b5F series","Parallel adds; series is reciprocal"],
  ["3","0.47 s","\u03c4 = RC, using 47 \u00d7 10 = 470 ms"],
  ["4","9.48 V","\u03c4 = 2.2 s, so t = 1\u03c4 and v = 15 \u00d7 0.632"],
  ["5","About 4.6 time constants","ln(100) \u2248 4.6"],
  ["6","0.5 s","Falling to 36.8 % defines one time constant"],
  ["7","26.3 V and 123.7 V","Inverse to capacitance; the 1 \u00b5F takes the larger share"],
  ["8","51.1 mA","i(0) = V/R, the capacitor is momentarily a short circuit"],
  ["9","DC gives no rate of change once charged","Current requires dv/dt, which alternating "
   "voltage supplies continuously"],
  ["10","About 1.2 k"+OH,"Needs \u03c4 \u2264 2.6 s, so R \u2264 2.6/2200 \u00b5F"]],
 ["Capacitance is charge stored per volt; stored energy follows the square of the voltage, so "
  "high-voltage capacitors are hazardous long after isolation.",
  "Capacitors add in parallel and combine reciprocally in series, the inverse of the resistor rules.",
  "Series capacitors divide voltage inversely to capacitance, so the smallest sees the most volts.",
  "The time constant RC sets the pace of every RC transient: 63 % in one, 99 % in five.",
  "An uncharged capacitor is momentarily a short circuit; a fully charged one is an open circuit "
  "to DC.",
  "Real capacitors have series resistance and leakage, and in power supplies these degrade before "
  "the part fails outright."],
 [["Capacitance","C = Q/V","Defines capacitance from charge and voltage"],
  ["Stored energy","W = \u00bdCV\u00b2","Any capacitor at a steady voltage"],
  ["Parallel capacitance","C_eq = \u03a3 C","Shared end nodes"],
  ["Series capacitance","1/C_eq = \u03a3 1/C","Common charge path"],
  ["Time constant",TAU+" = RC","Single resistance charging a single capacitance"],
  ["Charging voltage","v = V(1 \u2212 e^(\u2212t/"+TAU+"))","From an uncharged start"],
  ["Discharging voltage","v = V\u2080 e^(\u2212t/"+TAU+")","From an initial charge"]],
 [["Time constant","The product RC, the time to complete 63.2 % of a change"],
  ["Transient","The time-varying response between two steady states"],
  ["Steady state","The condition reached once all rates of change have ceased"],
  ["Series resistance","The unwanted internal resistance that heats a capacitor under ripple"],
  ["Bleed resistor","A resistor fitted to discharge a capacitor safely after isolation"]],
 "The capacitor opposes change in voltage. The next chapter introduces the inductor, which "
 "opposes change in current, and shows why switching an inductive circuit produces voltages far "
 "higher than the supply.",
)
