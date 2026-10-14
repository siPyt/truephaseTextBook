# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH7=mkch(7,"Impedance, phase and power factor",
 "Reactance, the impedance triangle, and why apparent power exceeds real power",
 "Add a capacitor or an inductor to an alternating circuit and the current no longer peaks with "
 "the voltage. The opposition is then impedance rather than resistance, and the product of "
 "voltage and current is no longer the power delivered. Power factor is the bookkeeping that "
 "reconciles them.",
 ["Compute inductive and capacitive reactance at a stated frequency.",
  "Combine resistance and reactance into an impedance magnitude and phase angle.",
  "Distinguish real, reactive and apparent power and state the unit of each.",
  "Compute power factor and explain its effect on conductor and supply loading.",
  "Select a correction capacitor to raise the power factor of an inductive load."],
 ("c7_rl_series","A resistive-inductive series circuit. The current is common to both elements, "
  "but the voltages across them are not in phase with each other.",46),
 [dict(h2="Reactance: frequency-dependent opposition",
   paras=["An inductor's opposition rises with frequency, because a faster rate of change "
    "produces a larger induced voltage. A capacitor's opposition falls with frequency, because a "
    "faster change moves more charge per second. Both are measured in ohms and called reactance, "
    "but neither dissipates energy: reactance stores and returns it each cycle.",
    "Because reactance depends on frequency, the same component behaves differently on a 50 Hz "
    "supply, a 60 Hz supply and the harmonic frequencies that electronic loads inject. A "
    "capacitor sized for correction at the fundamental presents a much lower reactance to the "
    "fifth harmonic, which is why correction equipment is sometimes detuned."],
   eq=["X_L = 2\u03c0 f L          X_C = 1 / (2\u03c0 f C)",
       "Both in ohms; neither dissipates power"],
   table=(["Element","Reactance","As frequency rises","Current relative to voltage"],
     [["Resistance","R, constant","Unchanged","In phase"],
      ["Inductance","X_L = 2\u03c0fL","Increases","Lags by 90 "+DEG],
      ["Capacitance","X_C = 1/(2\u03c0fC)","Decreases","Leads by 90 "+DEG]],None)),
  dict(h2="Impedance as a magnitude and an angle",
   paras=["Resistance and reactance do not add arithmetically because they act 90 degrees apart. "
    "They combine as the sides of a right triangle whose hypotenuse is the impedance magnitude "
    "and whose angle is the phase difference between voltage and current. This is the impedance "
    "triangle, and it is the single most useful picture in alternating current work.",
    "The same triangle, scaled by the current, gives the voltage triangle, and scaled by the "
    "current squared, gives the power triangle. Learning one shape therefore gives you three "
    "sets of relationships at no extra cost."],
   eq=["Z = \u221a(R\u00b2 + X\u00b2)",
       "\u03c6 = arctan(X / R)",
       "I = V / Z"],
   fig=("c7_rc_series","A resistive-capacitive series circuit. The capacitor voltage lags the "
     "resistor voltage by 90 degrees, so the two add vectorially, not arithmetically.",46)),
  dict(h2="Real, reactive and apparent power",
   paras=["Real power, in watts, is the energy actually converted to heat, light or mechanical "
    "work. Reactive power, in reactive volt-amperes, is energy borrowed and returned each cycle "
    "by reactive elements; it does no useful work but it does occupy conductor capacity. Apparent "
    "power, in volt-amperes, is the simple product of voltage and current and is what the supply "
    "must actually deliver.",
    "The three form a right triangle in the same proportions as the impedance triangle. Power "
    "factor is the ratio of real to apparent power, equal to the cosine of the phase angle for a "
    "sinusoidal supply. A load at 0.7 power factor draws about 43 per cent more current than a "
    "unity-power-factor load doing the same work."],
   eq=["P = V I cos\u03c6   (watts, W)",
       "Q = V I sin\u03c6   (reactive volt-amperes, var)",
       "S = V I         (volt-amperes, VA)",
       "S = \u221a(P\u00b2 + Q\u00b2)      pf = P / S = cos\u03c6"],
   panel=("Why a poor power factor costs money even though it does no work",
     ["Conductors and transformers are sized by current, which is set by apparent power.",
      "At 0.7 power factor, delivering 7 kW needs 10 kVA of supply capacity.",
      "The extra current produces real I\u00b2R losses in the distribution system."])),
  dict(h2="Correcting the power factor",
   paras=["An inductive load draws lagging reactive power. A capacitor draws leading reactive "
    "power, so a correctly sized capacitor connected in parallel supplies the reactive component "
    "locally and the supply current falls. The real power is unchanged, because correction does "
    "not reduce the work being done.",
    "Correction is sized from the reactive power to be cancelled, not from the kilowatts. "
    "Overcorrection should be avoided: it produces a leading power factor, can raise the voltage "
    "at light load and can resonate with system inductance at harmonic frequencies."],
   numbered=["Determine the real power P and the existing power factor, giving \u03c6\u2081.",
     "Compute the existing reactive power Q\u2081 = P tan\u03c6\u2081.",
     "Choose the target power factor, giving \u03c6\u2082, and compute Q\u2082 = P tan\u03c6\u2082.",
     "The capacitor must supply Q_c = Q\u2081 \u2212 Q\u2082.",
     "Convert to capacitance using C = Q_c / (2\u03c0 f V\u00b2).",
     "Verify the resulting current and confirm the correction is not excessive at light load."],
   fig=("c7_pf","Parallel capacitive correction of an inductive load. The capacitor supplies the "
     "reactive current locally, so the supply conductor carries less.",46)),
  dict(h2="Series resistance-inductance-capacitance behaviour",
   paras=["When all three elements appear in series the two reactances oppose each other, so the "
    "net reactance is their difference. Below a particular frequency the capacitive reactance "
    "dominates and the circuit appears capacitive; above it the inductive reactance dominates. At "
    "the frequency where they are equal the reactances cancel entirely.",
    "At that frequency the impedance reduces to the resistance alone, the current reaches its "
    "maximum and the voltage and current are in phase. This is series resonance, and it is "
    "developed fully in the next chapter."],
   eq=["X_net = X_L \u2212 X_C",
       "Z = \u221a(R\u00b2 + (X_L \u2212 X_C)\u00b2)"]),
 ],
 [ex("Impedance of a series resistive-inductive circuit",
   "A coil of 0.15 H and 40 "+OH+" winding resistance is supplied at 230 V, 50 Hz.",
   "The reactance, impedance, current, phase angle and power factor.",
   [("Inductive reactance","X_L = 2\u03c0 \u00d7 50 \u00d7 0.15 = 47.1 "+OH),
    ("Impedance magnitude","Z = \u221a(40\u00b2 + 47.1\u00b2) = 61.8 "+OH),
    ("Current","I = 230/61.8 = 3.72 A"),
    ("Phase angle","\u03c6 = arctan(47.1/40) = 49.7 "+DEG+" lagging"),
    ("Power factor","cos 49.7"+DEG+" = 0.647 lagging"),
    ("Real power","P = 230 \u00d7 3.72 \u00d7 0.647 = 553 W")],
   "Check through the resistance: P = I\u00b2R = 3.72\u00b2 \u00d7 40 = 553 W. The two agree, "
   "which confirms that only the resistance dissipates power."),
  ex("Apparent, real and reactive power",
   "A motor draws 12 A at 400 V single phase with a power factor of 0.82 lagging.",
   "The apparent, real and reactive power.",
   [("Apparent power","S = V I = 400 \u00d7 12 = 4800 VA"),
    ("Real power","P = S cos\u03c6 = 4800 \u00d7 0.82 = 3936 W"),
    ("Phase angle","\u03c6 = arccos 0.82 = 34.9 "+DEG),
    ("Reactive power","Q = S sin\u03c6 = 4800 \u00d7 0.572 = 2746 var"),
    ("Verify the triangle","\u221a(3936\u00b2 + 2746\u00b2) = 4799 VA \u2713")],
   "The supply must carry 4800 VA to deliver 3936 W of useful power. The 2746 var is borrowed and "
   "returned each cycle but still occupies conductor capacity."),
  ex("Sizing a correction capacitor",
   "The motor above is to be corrected from 0.82 to 0.95 lagging at 400 V, 50 Hz.",
   "The required reactive compensation, the capacitance and the new supply current.",
   [("Existing reactive power","Q\u2081 = 2746 var, as calculated"),
    ("Target angle","\u03c6\u2082 = arccos 0.95 = 18.2 "+DEG),
    ("Target reactive power","Q\u2082 = 3936 \u00d7 tan 18.2"+DEG+" = 1294 var"),
    ("Capacitor reactive power","Q_c = 2746 \u2212 1294 = 1452 var"),
    ("Capacitance","C = 1452 / (2\u03c0 \u00d7 50 \u00d7 400\u00b2) = 28.9 \u00b5F"),
    ("New current","S\u2082 = 3936/0.95 = 4143 VA, so I = 4143/400 = 10.36 A")],
   "The current falls from 12 A to 10.36 A, a 13.7 % reduction, while the real power stays at "
   "3936 W. The conductor and the supply transformer both see less loading.")],
 lab("impedance and power factor of a resistive-inductive load",
  "Measure the voltage, current and power of an inductive load, compute its power factor from the "
  "measurements, then demonstrate that a parallel capacitor reduces the supply current without "
  "changing the real power.",
  ["Low-voltage AC supply, 24 V, from an isolating transformer, fused at 2 A.",
   "Inductor or transformer winding of roughly 0.1 H with measurable resistance.",
   "Resistor, 22 "+OH+" 10 W.",
   "Capacitors, 10 \u00b5F, 22 \u00b5F and 47 \u00b5F, AC rated for at least 100 V.",
   "True rms multimeter, clamp meter or series ammeter, and a wattmeter if available."],
  ["Measure the inductor's DC resistance and record it; this is the resistive part of the coil.",
   "Connect the coil in series with the 22 "+OH+" resistor across the 24 V AC supply.",
   "Measure the supply voltage, the circuit current and the voltage across each element.",
   "Note that the two element voltages do not add to the supply voltage arithmetically; record "
   "all three.",
   "Compute the impedance from V over I, then the phase angle from the measured resistance.",
   "Compute the real power as I\u00b2 times the total resistance, and the apparent power as V "
   "times I.",
   "Connect the 10 \u00b5F capacitor in parallel with the whole load and re-measure the supply "
   "current.",
   "Repeat with 22 \u00b5F and 47 \u00b5F, recording the supply current each time.",
   "Identify which capacitor gave the lowest supply current and whether any value overcorrected."],
  ("c7_pf","The test arrangement. The capacitor is connected across the supply terminals of the "
   "load, and the ammeter reads the total supply current.",46),
  ["Capacitor","Supply V","Supply I (A)","S = VI (VA)","Computed pf"],
  [["none","24.0","","",""],["10 \u00b5F","24.0","","",""],["22 \u00b5F","24.0","","",""],
   ["47 \u00b5F","24.0","","",""],["repeat none","24.0","","",""],["best value","24.0","","",""]],
  ["Did the two element voltages add to the supply voltage arithmetically? Explain using the "
   "voltage triangle.",
   "Which capacitor produced the minimum supply current? Compare it with the value you would "
   "calculate for unity power factor.",
   "Did the real power change as capacitors were added? Explain why it should not.",
   "At the largest capacitor, was the current rising again? If so, explain overcorrection.",
   "Compute the percentage current reduction achieved at your best value and state what that "
   "would mean for conductor sizing."],
  ["Use an isolating transformer and keep the supply at 24 V; do not perform this activity on "
   "mains voltage.",
   "Capacitors must be AC rated. DC-rated or electrolytic capacitors must not be used across an "
   "AC supply.",
   "Discharge capacitors before handling and verify zero volts.",
   "Check the resistor and inductor power ratings against the measured current before energising."]),
 [["Element voltages do not add to the supply voltage","Normal: they are 90 "+DEG+" apart and add "
   "vectorially","Compute \u221a(V_R\u00b2 + V_X\u00b2) and compare with the supply","No fault; "
   "record the measurement and use the triangle"],
  ["Supply current higher than the real power suggests","Poor power factor from an inductive load",
   "Measure watts and volt-amperes separately","Apply parallel capacitive correction sized to the "
   "reactive power"],
  ["Current rises after adding more correction capacitance","Overcorrection, now a leading power "
   "factor","Compare supply current across several capacitor values","Reduce the capacitance to "
   "the minimum-current value"],
  ["Correction capacitor runs hot or fails early","Harmonic current flowing into a low capacitive "
   "reactance","Measure the capacitor current and look at its waveform","Fit a detuning reactor "
   "or a harmonic-rated capacitor assembly"],
  ["Measured power factor differs from the nameplate figure","Load not at rated output; power "
   "factor varies with loading","Measure at several load points","Use the power factor at the "
   "actual operating load for correction sizing"],
  ["Voltage rises at light load after correction was installed","Fixed capacitors remain "
   "connected when the inductive load falls away","Log voltage against load over a cycle of "
   "operation","Use switched or automatically staged correction"]],
 ("c7_rl_series","Separating resistance from reactance by measurement. The DC resistance and the "
  "AC impedance together give the reactance and the phase angle.",46),
 ["Measure watts and volt-amperes separately; a current reading alone cannot reveal power factor.",
  "Record the load point with any power factor figure, because power factor varies with loading.",
  "Size correction from the reactive power to be cancelled, never from the kilowatts.",
  "Expect reactive element voltages to exceed what arithmetic suggests; the triangle, not addition, "
  "governs."],
 ["Find the reactance of a 0.2 H inductor at 50 Hz and at 60 Hz.",
  "Find the reactance of a 10 \u00b5F capacitor at 50 Hz.",
  "A circuit has 30 "+OH+" resistance and 40 "+OH+" inductive reactance. Find the impedance and "
  "the phase angle.",
  "The circuit above is supplied at 120 V. Find the current, the real power and the apparent power.",
  "A load draws 8 A at 230 V with a power factor of 0.75. Find the real, reactive and apparent power.",
  "Explain why reactive power occupies conductor capacity despite doing no work.",
  "A series circuit has 25 "+OH+" resistance, 60 "+OH+" inductive and 20 "+OH+" capacitive "
  "reactance. Find the impedance.",
  "A 5 kW load at 0.8 power factor is to be corrected to 0.95 at 400 V, 50 Hz. Find the required "
  "capacitance.",
  "State what happens to the supply current if correction capacitance is doubled beyond the "
  "unity-power-factor value.",
  "Explain why a capacitor sized for 50 Hz correction presents a much lower reactance to the "
  "fifth harmonic, and why that matters."],
 [["1","62.8 "+OH+" at 50 Hz; 75.4 "+OH+" at 60 Hz","X_L = 2\u03c0fL"],
  ["2","318 "+OH,"X_C = 1/(2\u03c0fC)"],
  ["3","50 "+OH+"; 53.1 "+DEG+" lagging","Z = \u221a(30\u00b2+40\u00b2); \u03c6 = arctan(40/30)"],
  ["4","2.4 A; 173 W; 288 VA","I = V/Z; P = I\u00b2R; S = V I"],
  ["5","1380 W; 1217 var; 1840 VA","S = V I, then P = S cos\u03c6 and Q = S sin\u03c6"],
  ["6","Current is set by apparent power","Conductors and transformers are rated by current, not "
   "by watts"],
  ["7","47.2 "+OH,"Net reactance 40 "+OH+", so Z = \u221a(25\u00b2+40\u00b2)"],
  ["8","About 42 \u00b5F","Q_c = 5000(tan36.9"+DEG+" \u2212 tan18.2"+DEG+") = 2106 var, then "
   "C = Q_c/(2\u03c0fV\u00b2)"],
  ["9","It rises again, now leading","The circuit becomes capacitive and the reactive current "
   "returns, opposite in sign"],
  ["10","X_C falls by a factor of five","Harmonic currents concentrate in the capacitor, "
   "overheating it and risking resonance"]],
 ["Reactance is frequency-dependent opposition that stores and returns energy rather than "
  "dissipating it.",
  "Resistance and reactance combine as a right triangle, giving an impedance magnitude and a "
  "phase angle.",
  "Real power is in watts, reactive power in var and apparent power in volt-amperes, and they "
  "form the same triangle.",
  "Power factor is the ratio of real to apparent power, and a poor value raises current without "
  "raising useful output.",
  "Parallel capacitors correct a lagging power factor by supplying the reactive component locally.",
  "Correction must be sized from the reactive power and must not be excessive, or the circuit "
  "becomes leading."],
 [["Inductive reactance","X_L = 2\u03c0fL","Sinusoidal supply at frequency f"],
  ["Capacitive reactance","X_C = 1/(2\u03c0fC)","Sinusoidal supply at frequency f"],
  ["Impedance","Z = \u221a(R\u00b2+X\u00b2)","Series combination"],
  ["Phase angle","\u03c6 = arctan(X/R)","Series combination"],
  ["Real power","P = V I cos\u03c6","Sinusoidal quantities"],
  ["Reactive power","Q = V I sin\u03c6","Sinusoidal quantities"],
  ["Apparent power","S = V I","Always the product of rms values"],
  ["Correction","C = Q_c/(2\u03c0fV\u00b2)","Parallel capacitor at the load voltage"]],
 [["Reactance","Frequency-dependent opposition that stores rather than dissipates energy"],
  ["Impedance","The total opposition to alternating current, with magnitude and phase"],
  ["Power factor","The ratio of real to apparent power, cos\u03c6 for sinusoidal supplies"],
  ["Reactive power","Energy exchanged each cycle with reactive elements, measured in var"],
  ["Overcorrection","Adding more capacitance than needed, producing a leading power factor"]],
 "Impedance varies with frequency, so there is generally a frequency at which a circuit's "
 "behaviour changes character. The next chapter examines resonance, where inductive and "
 "capacitive reactances cancel, and the filters built from that effect.",
)
