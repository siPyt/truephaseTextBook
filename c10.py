# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH10=mkch(10,"Transformers",
 "Changing voltage without moving parts, and what that costs",
 "Transformers make the whole distribution system possible. Generating at one voltage, "
 "transmitting at a much higher one and using at a safe one is only practical because a "
 "transformer converts between them efficiently and with no moving parts.",
 ["Derive and apply the turns, voltage and current ratios.",
  "Explain why a transformer cannot operate on direct current.",
  "Distinguish step-up, step-down, isolating and auto-transformer connections.",
  "Compute transformer rating in volt-amperes and relate it to load current.",
  "Account for no-load and load losses and compute efficiency and regulation.",
  "Interpret a nameplate, select tap positions and explain inrush current."],
 ("c10_xfmr","A two-winding transformer on a shared iron core. Alternating flux produced by the "
  "primary links the secondary, inducing a voltage set by the turns ratio.",46),
 [dict(h2="How a transformer works",
   paras=["Two windings share a magnetic core. Alternating voltage applied to the primary drives "
    "an alternating flux around that core, and because the same flux links the secondary, a "
    "voltage is induced there. No electrical connection between the windings is needed; the "
    "coupling is entirely magnetic.",
    "Because the induced voltage depends on the rate of change of flux, a transformer needs "
    "alternating supply. Applied to direct current it produces a brief output at switch-on and "
    "then nothing, while the primary draws a current limited only by its own winding resistance. "
    "This is why connecting a transformer to a direct supply destroys it."],
   eq=["e = \u2212N d\u03a6/dt      so steady flux induces nothing",
       "V\u209a / V\u209b = N\u209a / N\u209b = a      (turns ratio)"],
   panel=("A transformer is an alternating-current device only",
     ["Output voltage depends on flux changing, not on flux existing.",
      "On direct current the primary becomes a low-resistance coil across the supply.",
      "The winding overheats within seconds and the transformer is lost.",
      "Confirm the supply type before energising any transformer."])),
  dict(h2="Voltage, current and impedance ratios",
   paras=["The voltage ratio follows the turns ratio directly. The current ratio is the inverse, "
    "because an ideal transformer neither creates nor absorbs power: whatever volt-amperes enter "
    "the primary leave the secondary. A step-down transformer therefore raises current in the "
    "same proportion as it lowers voltage.",
    "This inversion has an important safety consequence. The secondary of a step-down "
    "transformer can deliver very large currents from a modest primary supply, so secondary "
    "conductors and protection must be sized for the stepped-up current, not for the primary "
    "current."],
   eq=["V\u209a / V\u209b = N\u209a / N\u209b",
       "I\u209b / I\u209a = N\u209a / N\u209b      so V\u209a I\u209a = V\u209b I\u209b (ideal)",
       "Z\u209a / Z\u209b = (N\u209a / N\u209b)\u00b2 = a\u00b2"],
   after=["The impedance ratio is the square of the turns ratio, which is why a transformer can "
    "match a load to a source and why a secondary short circuit appears to the primary as a "
    "fault reduced by the square of the ratio."]),
  dict(h2="Rating in volt-amperes",
   paras=["A transformer is rated in volt-amperes rather than watts because its limits are set "
    "by current in the windings and by flux in the core, neither of which depends on the load's "
    "power factor. A winding heated by 20 A is equally heated whether that current is in phase "
    "with the voltage or not.",
    "Load current is therefore found from the apparent power and the secondary voltage. Where "
    "the load power factor is poor, the transformer must be sized on apparent power even though "
    "the useful power delivered is lower."],
   eq=["S = V I      (single phase, in volt-amperes)",
       "I\u209b = S / V\u209b",
       "S = \u221a3 V_L I_L      (three phase)"],
   fig=("c10_taps","Tap connections on the primary winding. Selecting a different tap changes "
     "the effective turns ratio to compensate for a high or low incoming supply.",46)),
  dict(h2="Losses, efficiency and regulation",
   paras=["Real transformers lose power in two distinct ways. Core loss, comprising hysteresis "
    "and eddy-current loss, depends on voltage and frequency and is therefore almost constant "
    "whenever the unit is energised. Copper loss arises from winding resistance and varies with "
    "the square of the load current.",
    "Efficiency is highest at the load where these two losses are equal, which for distribution "
    "transformers is usually designed to fall somewhere between half and three-quarters of full "
    "load. Regulation is a separate measure: the fall in secondary voltage from no load to full "
    "load, expressed as a percentage of the no-load value."],
   eq=["\u03b7 = output / (output + P_core + P_cu)",
       "P_cu at any load = P_cu(full) \u00d7 (I / I_full)\u00b2",
       "Regulation % = (V_noload \u2212 V_load) / V_noload \u00d7 100"],
   table=(["Quantity","Determined by","Varies with load?","Measured by"],
     [["Core loss","Applied voltage and frequency","No","Open-circuit test"],
      ["Copper loss","Winding resistance and current","Yes, as current squared",
       "Short-circuit test"],
      ["Efficiency","Ratio of output to input","Yes, peaks where losses are equal",
       "Computed from both tests"],
      ["Regulation","Winding impedance and load power factor","Yes","Loaded voltage measurement"]],
     None)),
  dict(h2="Isolation, autotransformers and inrush",
   paras=["A two-winding transformer provides galvanic isolation: there is no conductive path "
    "between primary and secondary, so a fault on one side does not reference the other to earth. "
    "This is the property exploited by isolating transformers used for sensitive equipment and "
    "for certain tool supplies.",
    "An autotransformer uses a single tapped winding instead, which makes it smaller and cheaper "
    "for small ratio changes but provides no isolation whatever. The primary and secondary share "
    "conductors, so an earth fault or an open point in the common section can place full input "
    "voltage on the output.",
    "All transformers draw a heavy inrush current at energisation, because the core may be left "
    "magnetised from the previous switch-off and can be driven briefly into deep saturation. "
    "Inrush may reach ten or more times rated current for a few cycles, which is why transformer "
    "protection must tolerate it without tripping."],
   bh="Choosing and energising transformers",
   bullets=["Specify a two-winding type wherever isolation is required; an autotransformer "
     "cannot provide it.",
     "Size secondary conductors for the stepped-up secondary current.",
     "Select protection that rides through inrush but still clears a genuine fault.",
     "Record the tap position at commissioning, so later voltage complaints can be checked.",
     "De-energise unused transformers, because core loss continues regardless of load."],
   fig=("c10_iso","An isolating transformer. With no conductive path between the windings, the "
     "secondary has no fixed relationship to the primary reference.",46)),
 ],
 [ex("Turns ratio, secondary voltage and currents",
   "A transformer has 960 primary turns and 80 secondary turns, supplied at 240 V, delivering "
   "15 A to its load.",
   "The turns ratio, secondary voltage, primary current and the apparent power.",
   [("Turns ratio","a = 960/80 = 12 : 1, step down"),
    ("Secondary voltage","V\u209b = 240/12 = 20 V"),
    ("Apparent power","S = 20 \u00d7 15 = 300 VA"),
    ("Primary current","I\u209a = 15/12 = 1.25 A"),
    ("Confirm the power balance","240 \u00d7 1.25 = 300 VA \u2713")],
   "Voltage fell by twelve times and current rose by twelve times, leaving the apparent power "
   "unchanged. A 1.25 A primary circuit is feeding a 15 A secondary, which is why the secondary "
   "cable must be sized on 15 A."),
  ex("Efficiency at full and half load",
   "A 5 kVA transformer has a core loss of 60 W and a full-load copper loss of 110 W. The load "
   "power factor is 0.9.",
   "The efficiency at full load and at half load.",
   [("Full-load output power","P = 5000 \u00d7 0.9 = 4500 W"),
    ("Full-load total loss","60 + 110 = 170 W"),
    ("Full-load efficiency","\u03b7 = 4500/(4500 + 170) = 0.964, that is 96.4 %"),
    ("Half-load output","P = 2250 W"),
    ("Half-load copper loss","110 \u00d7 0.5\u00b2 = 27.5 W"),
    ("Half-load efficiency","\u03b7 = 2250/(2250 + 60 + 27.5) = 0.963, that is 96.3 %")],
   "Efficiency barely changes between half and full load because copper loss falls as the square "
   "of current while core loss stays fixed. The peak lies where the two losses are equal, near "
   "73 % of full load here."),
  ex("Voltage regulation",
   "A transformer measures 230 V at its secondary with no load and 219 V at full load.",
   "The regulation, and whether it is acceptable for a lighting circuit.",
   [("Voltage drop","230 \u2212 219 = 11 V"),
    ("Regulation","11/230 \u00d7 100 = 4.8 %"),
    ("Typical expectation","Distribution transformers commonly give 2 to 5 %"),
    ("Assessment","Acceptable, but near the upper end")],
   "A 4.8 % regulation leaves little margin once cable drop is added downstream. If terminal "
   "voltage at the far end of the final circuit matters, this transformer should be tapped up or "
   "a lower-impedance unit chosen."),
  ex("Secondary fault current reflected to the primary",
   "A 12 : 1 step-down transformer suffers a secondary short circuit drawing 480 A.",
   "The resulting primary current, and why the primary protection may not see it as alarming.",
   [("Current ratio","I\u209a = I\u209b / a"),
    ("Substitute","I\u209a = 480/12 = 40 A"),
    ("Impedance seen at the primary","Z\u209a = a\u00b2 Z\u209b = 144 \u00d7 Z\u209b"),
    ("Consequence","A severe secondary fault appears as a modest primary overload")],
   "The transformer transforms faults as well as load. A 480 A secondary fault looks like 40 A at "
   "the primary, which may sit within the primary device's tolerance long enough to burn the "
   "secondary winding, so secondary-side protection is required.")],
 lab("transformer ratio, loss separation and regulation",
  "Verify the turns and current ratios by measurement, separate core loss from copper loss using "
  "open-circuit and short-circuit tests, then load the transformer progressively and determine "
  "its regulation and efficiency curve.",
  ["Two-winding transformer, 240 V to 24 V, 150 VA or similar, on a bench mount.",
   "Variable alternating supply with an isolating transformer ahead of it.",
   "Two true rms multimeters and a power meter or wattmeter.",
   "Resistive load bank, switchable in steps, rated for the secondary current.",
   "Clamp meter suitable for small alternating currents.",
   "Insulation resistance tester."],
  ["With the transformer de-energised and disconnected, measure and record the resistance of each "
   "winding and the insulation resistance between them.",
   "Identify primary and secondary from the nameplate and compute the expected turns ratio.",
   "Open-circuit test: apply rated voltage to the primary with the secondary open. Record primary "
   "voltage, current and power. This power is essentially the core loss.",
   "Record the secondary open-circuit voltage and compute the measured voltage ratio.",
   "Short-circuit test: with the secondary shorted through an ammeter, raise the primary voltage "
   "from zero only until rated secondary current flows. Record primary voltage, current and power. "
   "This power is essentially the full-load copper loss.",
   "Return the supply to zero before changing any connection.",
   "Reconnect the load bank and apply rated primary voltage.",
   "Record secondary voltage and current at no load and at four increasing load steps up to rated "
   "current.",
   "Measure primary current at each step and compare the measured current ratio with the turns "
   "ratio.",
   "Compute efficiency at each step from the two loss figures, and compute regulation from your "
   "no-load and full-load secondary voltages."],
  ("c10_xfmr","The test arrangement. The same transformer serves the open-circuit, short-circuit "
   "and loading tests with only the secondary connection changed.",46),
  ["Load step","V\u209b (V)","I\u209b (A)","I\u209a (A)","Efficiency and comment"],
  [["No load","","","",""],["25 % load","","","",""],["50 % load","","","",""],
   ["75 % load","","","",""],["100 % load","","","",""],
   ["Short-circuit test","","","",""]],
  ["How closely did your measured voltage ratio match the nameplate turns ratio, and what "
   "accounts for the difference?",
   "Why is the open-circuit power essentially all core loss, and the short-circuit power "
   "essentially all copper loss?",
   "At which load step was your computed efficiency highest? Compare that load with the point "
   "where your two losses are equal.",
   "Compute the regulation. What would that drop do to a load at the end of a long secondary cable?",
   "Why must the short-circuit test be started from zero volts and raised only to rated current?",
   "Your measured current ratio probably departs from the turns ratio slightly more than the "
   "voltage ratio does. Suggest why."],
  ["Always supply the bench through an isolating transformer and a residual current device.",
   "During the short-circuit test, raise the voltage from zero slowly. Applying rated voltage to "
   "a shorted secondary will destroy the transformer and is dangerous.",
   "Secondary current in a step-down transformer is much higher than primary current. Size the "
   "load leads and the ammeter accordingly.",
   "Return the variable supply to zero and prove dead before altering any connection.",
   "Windings and the load bank become hot. Allow them to cool before handling.",
   "Do not apply any direct-current supply to the transformer."]),
 [["Transformer hums loudly and runs hot with no load","Supply voltage high or tap set too low, "
   "pushing the core toward saturation","Measure the incoming voltage and check the selected tap",
   "Move to the correct tap or correct the supply voltage"],
  ["Secondary voltage low only when loaded","Excessive regulation, undersized transformer or "
   "undersized secondary cable","Measure secondary voltage at no load and at full load, then at "
   "the load terminals","Tap up, fit a larger transformer, or increase cable size"],
  ["Primary protection trips at every energisation","Inrush current exceeding the device's "
   "instantaneous setting","Compare the device characteristic with the expected inrush",
   "Fit a device with a suitable inrush-tolerant characteristic"],
  ["Transformer destroyed shortly after installation","Connected to a direct-current supply, or "
   "primary and secondary reversed","Check the supply type and compare terminal markings with "
   "the nameplate","Replace the unit and correct the supply or the connection"],
  ["Shock risk present on an output believed to be isolated","Autotransformer fitted where an "
   "isolating transformer was specified","Test for continuity between input and output terminals "
   "with the unit de-energised","Replace with a genuine two-winding isolating transformer"],
  ["Insulation resistance between windings has fallen","Moisture ingress or winding insulation "
   "degradation","Insulation resistance test between windings and to earth, de-energised",
   "Dry out and retest, or withdraw the transformer from service"]],
 ("c10_iso","Verifying isolation. With the unit de-energised, a continuity test between primary "
  "and secondary distinguishes a true isolating transformer from an autotransformer.",44),
 ["Record the tap position and the no-load secondary voltage at commissioning, so later voltage "
  "complaints have a baseline.",
  "Size secondary conductors and protection on the secondary current, never on the primary current.",
  "Test for continuity between windings before relying on any transformer for isolation.",
  "De-energise transformers serving no load, because core loss continues the whole time they "
  "are energised.",
  "Treat a change in transformer noise as a real symptom and investigate the supply voltage."],
 ["A transformer has 1200 primary and 100 secondary turns on 230 V. Find the secondary voltage.",
  "The transformer above delivers 8 A. Find the primary current.",
  "Find the apparent power of a transformer delivering 24 V at 12 A.",
  "A 3 kVA transformer has a 48 V secondary. Find the rated secondary current.",
  "State why transformers are rated in volt-amperes rather than watts.",
  "Explain why a transformer cannot work on a direct-current supply.",
  "A transformer has 40 W core loss and 90 W full-load copper loss. Find the copper loss at half load.",
  "For the transformer above delivering 2 kW at full load, find the full-load efficiency.",
  "A secondary measures 48 V unloaded and 45.5 V at full load. Find the regulation.",
  "State the single most important difference between an autotransformer and a two-winding "
  "transformer.",
  "Explain why inrush current can reach many times rated current at energisation.",
  "A 20 : 1 step-down transformer has a secondary fault of 600 A. Find the primary current and "
  "state the protection implication."],
 [["1","19.2 V","V\u209b = V\u209a N\u209b/N\u209a"],
  ["2","0.667 A","I\u209a = I\u209b N\u209b/N\u209a"],
  ["3","288 VA","S = V I"],
  ["4","62.5 A","I = S/V"],
  ["5","Limits are set by current and flux, not power factor","A winding is heated by its "
   "current whatever the phase angle"],
  ["6","Induced voltage needs changing flux","Steady current gives constant flux, so nothing is "
   "induced and the primary acts as a low-resistance coil"],
  ["7","22.5 W","P_cu scales with current squared, so 90 \u00d7 0.25"],
  ["8","93.9 %","\u03b7 = 2000/(2000 + 40 + 90)"],
  ["9","5.2 %","(48 \u2212 45.5)/48 \u00d7 100"],
  ["10","The autotransformer gives no galvanic isolation","Its windings share conductors, so "
   "input and output are conductively connected"],
  ["11","Residual core magnetism plus switching instant","The core can be driven into deep "
   "saturation for a few cycles, briefly collapsing the limiting impedance"],
  ["12","30 A; secondary protection is required","A severe secondary fault looks like a modest "
   "primary overload, so the primary device may not clear it in time"]],
 ["A transformer couples two windings magnetically, so it changes voltage with no electrical "
  "connection and no moving parts, but only on alternating supply.",
  "Voltage follows the turns ratio, current follows its inverse, and impedance follows the square "
  "of the ratio.",
  "Rating is in volt-amperes because winding current and core flux, not load power factor, set "
  "the limits.",
  "Core loss is constant with load while copper loss rises as current squared, so efficiency "
  "peaks where the two are equal.",
  "Regulation measures the voltage fall from no load to full load and must be allowed for in "
  "downstream design.",
  "Only a two-winding transformer provides isolation; an autotransformer does not.",
  "Inrush current at energisation can be many times rated current and protection must tolerate it."],
 [["Turns ratio","V\u209a/V\u209b = N\u209a/N\u209b","Two-winding transformer"],
  ["Current ratio","I\u209b/I\u209a = N\u209a/N\u209b","Ideal transformer, power balance"],
  ["Impedance ratio","Z\u209a/Z\u209b = (N\u209a/N\u209b)\u00b2","Referring a load to the primary"],
  ["Apparent power","S = V I","Single-phase rating"],
  ["Copper loss at part load","P_cu = P_cu(full)(I/I_full)\u00b2","Any load current"],
  ["Efficiency","\u03b7 = P_out/(P_out + P_core + P_cu)","Any load"],
  ["Regulation","(V_nl \u2212 V_fl)/V_nl \u00d7 100","No load to full load"]],
 [["Turns ratio","The ratio of primary to secondary turns, which fixes the voltage ratio"],
  ["Galvanic isolation","Absence of any conductive path between two circuits"],
  ["Autotransformer","A single tapped winding serving as both primary and secondary, with no "
   "isolation"],
  ["Core loss","Hysteresis and eddy-current loss, present whenever the unit is energised"],
  ["Regulation","The percentage fall in secondary voltage from no load to full load"],
  ["Inrush current","The brief heavy current drawn at energisation as the core is driven toward "
   "saturation"],
  ["Tap","A connection point on a winding used to adjust the effective turns ratio"]],
 "A transformer converts voltage but produces no motion. Adding a rotating magnetic field to the "
 "same principles gives the induction motor, which the next chapter examines along with "
 "generators and machine control.",
)
