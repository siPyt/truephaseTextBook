# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH13=mkch(13,"Transistors",
 "Switching and amplifying with a controlled third terminal",
 "A diode's conduction is decided entirely by the polarity across it. A transistor adds a third "
 "terminal that controls conduction between the other two, which makes electronic switching and "
 "amplification possible. Every logic gate, every solid-state relay and every variable-speed "
 "drive rests on this one capability.",
 ["Identify bipolar and field-effect transistors and their terminals from the symbols.",
  "Describe the three operating regions and state which are used for switching.",
  "Compute base, collector and emitter currents using current gain.",
  "Design a transistor switch to drive a relay or lamp, including the base resistor.",
  "Explain why a field-effect transistor is voltage controlled and what that implies.",
  "Compute switching and conduction losses and explain why saturation matters."],
 ("c13_switch","A transistor as a low-side switch driving a relay coil. The base resistor sets "
  "the drive current and the suppression diode handles the coil's reverse voltage.",46),
 [dict(h2="The bipolar junction transistor",
   paras=["A bipolar transistor has three terminals: emitter, base and collector. A small current "
    "into the base allows a much larger current to flow from collector to emitter, and the ratio "
    "between them is the current gain. Because a current controls a current, the bipolar device "
    "always consumes drive current while it is on.",
    "Two polarities exist. In an n-p-n device the collector sits positive and base current flows "
    "into the base; in a p-n-p device the polarities are reversed throughout. The symbols are "
    "distinguished only by the direction of the emitter arrow, which always points in the "
    "direction of conventional current through the emitter."],
   eq=["I_E = I_B + I_C      (currents always balance)",
       "\u03b2 = I_C / I_B      (current gain, often 50 to 400)",
       "I_C = \u03b2 I_B      in the active region only"],
   bh="Reading a bipolar transistor symbol",
   bullets=["The arrow is always on the emitter, never on the collector.",
     "Arrow pointing out of the device: n-p-n.",
     "Arrow pointing into the device: p-n-p.",
     "The base is the terminal on the flat bar.",
     "A second arrow on the base region indicates a phototransistor.",
     "Two transistors drawn in cascade within one outline indicates a Darlington."]),
  dict(h2="The three operating regions",
   paras=["With no base current the device is cut off: essentially no collector current flows and "
    "the full supply appears across the device. With a large base current the device is "
    "saturated: the collector current is limited by the external circuit rather than by the gain, "
    "and the collector-to-emitter voltage falls to a few tenths of a volt.",
    "Between those two states lies the active region, where collector current is proportional to "
    "base current. Amplifiers work in the active region; switches deliberately avoid it, because "
    "a device carrying substantial current with substantial voltage across it dissipates "
    "substantial heat. A switch should pass through the active region quickly and settle in "
    "saturation or cut-off."],
   table=(["Region","Base drive","Collector-emitter voltage","Dissipation","Used for"],
     [["Cut-off","None","Full supply","Negligible","Switch off state"],
      ["Active","Proportional","Intermediate","High","Amplification"],
      ["Saturation","Generous excess","0.2 to 0.4 V","Low","Switch on state"]],None),
   panel=("A switch must be driven hard into saturation",
     ["In saturation the device drops a few tenths of a volt and dissipates little.",
      "Partial drive leaves it in the active region, where it dissipates heavily.",
      "Provide base current well above I_C divided by the minimum gain.",
      "A transistor switch that runs hot is almost always underdriven."])),
  dict(h2="Designing a transistor switch",
   paras=["The design sequence is short. Establish the load current the collector must carry, "
    "take the worst-case minimum gain from the data sheet, and compute the base current needed. "
    "Then multiply that by a factor of three to five to guarantee saturation across temperature "
    "and device spread.",
    "The base resistor follows from the drive voltage less the base-emitter drop of about 0.7 "
    "volts, divided by the chosen base current. Where the load is a coil or any other inductive "
    "device, a suppression diode across the load is essential: interrupting coil current produces "
    "a reverse voltage that will otherwise exceed the transistor's rating and destroy it."],
   eq=["I_B(min) = I_C / \u03b2(min)",
       "I_B(design) = 3 to 5 \u00d7 I_B(min)",
       "R_B = (V_drive \u2212 0.7) / I_B(design)",
       "P = V_CE(sat) \u00d7 I_C      in the on state"],
   fig=("c13_amp","A single-stage amplifier. The bias network holds the device in the active "
     "region and the signal is superimposed on that operating point.",46)),
  dict(h2="Field-effect transistors",
   paras=["A field-effect transistor controls current between drain and source by means of a "
    "voltage on an insulated or reverse-biased gate, rather than by a current. Once switched, the "
    "gate draws almost no current, so the drive circuit need supply only the brief charge that "
    "the gate capacitance requires.",
    "In the metal-oxide-semiconductor type, the gate is insulated by a thin oxide layer that is "
    "easily punctured by static discharge or by gate overvoltage, so handling precautions and "
    "gate protection matter. Junction types use a reverse-biased junction instead and are more "
    "robust but offer less switching performance."],
   eq=["Gate voltage controls drain current; gate current \u2248 0",
       "On-state loss:  P = I_D\u00b2 R_DS(on)",
       "Gate charge:  Q = C_gate V_gate"],
   table=(["Property","Bipolar transistor","Field-effect transistor"],
     [["Controlled by","Base current","Gate voltage"],
      ["Steady drive power","Continuous base current","Almost none once switched"],
      ["On-state loss","V_CE(sat) \u00d7 I_C","I_D\u00b2 \u00d7 R_DS(on)"],
      ["Parallel operation","Difficult, current hogging","Straightforward, resistance rises with "
       "temperature"],
      ["Static sensitivity","Low","High for insulated-gate types"],
      ["Typical switching speed","Moderate","Fast"]],None),
   fig=("c13_mosfet","A metal-oxide-semiconductor field-effect transistor switching a load. The "
     "gate is driven by voltage and draws current only while the gate capacitance charges.",46)),
  dict(h2="Heat, saturation and parallel devices",
   paras=["On-state loss differs fundamentally between the two families. A bipolar device drops a "
    "roughly fixed saturation voltage, so its loss rises in proportion to current. A field-effect "
    "device behaves as a resistance, so its loss rises as the square of current, which makes it "
    "excellent at low current and progressively worse at high current.",
    "That resistance rises with temperature, which has a useful consequence: paralleled "
    "field-effect devices share current automatically, because the hottest device becomes the "
    "most resistive and sheds load to the others. Bipolar devices do the opposite and must be "
    "ballasted with emitter resistors if paralleled at all."],
   panel=("Switching loss is separate from conduction loss",
     ["Conduction loss occurs while the device is fully on.",
      "Switching loss occurs during each transition through the active region.",
      "Switching loss is proportional to switching frequency.",
      "A device cool at low frequency may overheat at high frequency with the same current."]),
   bh="Keeping a solid-state switch alive",
   bullets=["Drive the gate or base hard enough to reach full saturation or full enhancement.",
     "Fit a suppression diode across every inductive load.",
     "Provide a thermal path sized on the computed on-state loss.",
     "Include a gate resistor and a gate-to-source resistor on insulated-gate devices.",
     "Observe static-handling precautions for insulated-gate parts.",
     "Check the device rating against the load's inrush, not only its running current."]),
 ],
 [ex("Base current and base resistor for a relay driver",
   "A relay coil draws 90 mA at 24 V. The transistor has a minimum current gain of 60 and is "
   "driven from a 5 V logic output.",
   "The minimum base current, a suitable design base current, and the base resistor.",
   [("Collector current","I_C = 90 mA"),
    ("Minimum base current","I_B = 90/60 = 1.5 mA"),
    ("Design base current, factor of 4","I_B = 6 mA"),
    ("Voltage across the base resistor","5 \u2212 0.7 = 4.3 V"),
    ("Base resistor","R_B = 4.3/0.006 = 717 \u03a9, so use 680 \u03a9"),
    ("Resulting base current","4.3/680 = 6.3 mA")],
   "The factor of four guarantees saturation despite gain spread and temperature. Note the "
   "suppression diode across the coil is not optional: without it the collapsing field will "
   "exceed the transistor's collector rating."),
  ex("On-state dissipation compared across device types",
   "A load draws 3 A. A bipolar device saturates at 0.3 V; a field-effect device has an on "
   "resistance of 40 m\u03a9.",
   "The on-state loss of each, and which is preferable if the current rises to 10 A.",
   [("Bipolar loss at 3 A","P = 0.3 \u00d7 3 = 0.9 W"),
    ("Field-effect loss at 3 A","P = 3\u00b2 \u00d7 0.04 = 0.36 W"),
    ("Bipolar loss at 10 A","P = 0.3 \u00d7 10 = 3.0 W"),
    ("Field-effect loss at 10 A","P = 10\u00b2 \u00d7 0.04 = 4.0 W"),
    ("Conclusion","The field-effect device wins at 3 A, loses at 10 A with this resistance")],
   "Because one loss is linear in current and the other is quadratic, there is a crossover "
   "current. For high-current duty a field-effect device must have a correspondingly lower on "
   "resistance to stay ahead."),
  ex("Underdriven switch running in the active region",
   "A transistor with a gain of 100 is given only 0.2 mA of base current while its load demands "
   "60 mA from a 24 V supply through a 400 \u03a9 load.",
   "What the device actually does, and the dissipation.",
   [("Collector current the gain permits","I_C = 100 \u00d7 0.0002 = 20 mA"),
    ("Load current demanded at saturation","24/400 = 60 mA"),
    ("Actual state","Active region, limited to 20 mA by insufficient drive"),
    ("Voltage across the load","0.020 \u00d7 400 = 8 V"),
    ("Voltage across the device","24 \u2212 8 = 16 V"),
    ("Dissipation","P = 16 \u00d7 0.020 = 0.32 W")],
   "Compare that 0.32 W with a properly saturated device, which would dissipate about 0.3 V times "
   "60 mA, or 18 mW. Underdriving multiplied the heat by nearly twenty times while delivering a "
   "third of the current."),
  ex("Gate drive charge and switching frequency",
   "A field-effect transistor has a gate charge of 50 nC and is driven to 10 V at a switching "
   "frequency of 40 kHz.",
   "The average gate drive current and the drive power.",
   [("Charge per switching cycle","Q = 50 nC, delivered twice per cycle"),
    ("Average gate current","I = Q f = 50\u00d710\u207b\u2079 \u00d7 40 000 = 2 mA"),
    ("Gate drive power","P = Q f V = 50\u00d710\u207b\u2079 \u00d7 40 000 \u00d7 10 = 20 mW"),
    ("Steady-state gate current","Essentially zero between transitions")],
   "The drive requirement is almost entirely dynamic. This is why a field-effect device needs "
   "negligible drive at low switching rates but a substantial gate driver at high frequency.")],
 lab("transistor regions, a relay driver and comparing two switch devices",
  "Map the three operating regions of a bipolar transistor, build and verify a relay driver "
  "including its suppression diode, then compare the on-state dissipation of a bipolar and a "
  "field-effect switch at the same load current.",
  ["Bipolar transistors, n-p-n, medium power, with a data sheet.",
   "Field-effect transistor, n-channel enhancement type, logic-level gate.",
   "Relay, 24 V coil, and a suppression diode.",
   "Resistors: 220 \u03a9, 680 \u03a9, 4.7 k\u03a9, 100 k\u03a9 and a 0 to 100 k\u03a9 decade box.",
   "Two variable direct supplies, 0 to 24 V, current limited.",
   "Two multimeters, an oscilloscope, and a clip-on or infrared thermometer.",
   "Antistatic wrist strap and mat for handling insulated-gate devices."],
  ["Identify the terminals of each device from the data sheet before wiring anything.",
   "Build the bipolar device with a 400 \u03a9 collector load from a 12 V supply and a decade box "
   "feeding the base from a separate 5 V supply.",
   "Set the decade box to its maximum and record collector current and collector-emitter voltage. "
   "Note which region this is.",
   "Reduce the base resistance in steps, recording base current, collector current and "
   "collector-emitter voltage at each step.",
   "Continue until collector-emitter voltage stops falling. Record the base current at which "
   "saturation was reached.",
   "Compute the current gain from a mid-range pair of readings and compare with the data sheet.",
   "Plot collector current against base current and mark the three regions on your graph.",
   "At one clearly active-region point, compute the device dissipation and measure its "
   "temperature after two minutes.",
   "Repeat the temperature measurement in saturation at the same collector current and compare.",
   "Build the relay driver with the 680 \u03a9 base resistor and the suppression diode fitted.",
   "Confirm the relay operates, then observe the collector waveform on switch-off.",
   "Remove the suppression diode, switch off once, and observe the collector voltage spike. "
   "Refit the diode immediately.",
   "Wearing the wrist strap, build the field-effect device switching the same relay from a gate "
   "voltage, with a gate resistor and a gate-to-source resistor fitted.",
   "Measure the on-state voltage across each device at the same load current and compute the "
   "dissipation of each."],
  ("c13_switch","The switch test arrangement. The suppression diode across the coil is fitted "
   "for all tests except the single deliberate observation of the switch-off spike.",46),
  ["Base current (mA)","Collector current (mA)","V_CE (V)","Region","Dissipation and comment"],
  [["0","","","",""],["0.05","","","",""],["0.2","","","",""],
   ["0.5","","","",""],["1.0","","","",""],["3.0","","","",""],
   ["Field-effect device, on","","","",""]],
  ["From your graph, over what range of base current was collector current proportional to base "
   "current? What limited it beyond that?",
   "How did your computed current gain compare with the data sheet figure, and why would a "
   "designer use the minimum rather than the typical value?",
   "Compare the measured device temperature in the active region with that in saturation at the "
   "same collector current. Explain the difference.",
   "What collector voltage did you observe on switch-off with the suppression diode removed? "
   "Compare it with the supply voltage and with the device rating.",
   "Explain, using Lenz's law, why the spike appears and why its polarity is such that the diode "
   "can conduct it.",
   "Compare the on-state dissipation of the two devices at the same load current. At what current "
   "would the comparison reverse?",
   "Why does the field-effect device need almost no steady drive current, and what does it need "
   "instead?",
   "Why were a gate resistor and a gate-to-source resistor fitted to the field-effect device?"],
  ["Wear an antistatic wrist strap when handling insulated-gate devices; their gate oxide is "
   "destroyed by static discharge.",
   "Limit both supplies in current before connecting any device.",
   "Interrupting the relay coil without the suppression diode produces a voltage spike well above "
   "the supply. Do this once, briefly, and do not touch the circuit while switching.",
   "Devices in the active region become hot quickly. Use the thermometer rather than a finger.",
   "Check the computed dissipation against the device rating before applying power.",
   "Allow devices and heatsinks to cool before handling or rewiring."]),
 [["Transistor switch runs hot but the load works","Insufficient base or gate drive, so the "
   "device sits in the active region","Measure the voltage across the device while it is on; it "
   "should be a few tenths of a volt","Reduce the base resistor or raise the gate drive voltage"],
  ["Transistor fails whenever an inductive load is switched off","No suppression diode, so the "
   "coil's reverse voltage exceeds the device rating","Observe the device voltage at switch-off "
   "on an oscilloscope","Fit a suppression diode across the coil, cathode to the positive supply"],
  ["Insulated-gate device fails on the bench but not in service","Static discharge during "
   "handling, or gate overvoltage","Inspect for gate-to-source short with a meter","Observe "
   "antistatic precautions and fit a gate resistor and gate-to-source resistor"],
  ["Paralleled bipolar devices share current unevenly and one fails","Current hogging, because "
   "forward drop falls as temperature rises","Measure current in each device branch separately",
   "Fit emitter ballast resistors, or use field-effect devices instead"],
  ["Switch works at low frequency but overheats at high frequency","Switching loss rising in "
   "proportion to frequency","Compute conduction and switching loss separately",
   "Improve gate drive to shorten transitions, or reduce the switching frequency"],
  ["Field-effect device turns on by itself","Gate left floating and charged by leakage or "
   "capacitive coupling","Check for a gate-to-source resistor","Fit a gate-to-source resistor to "
   "define the off state"],
  ["Logic output cannot drive the transistor into saturation","Logic source current too low for "
   "the required base current","Compare the required base current with the logic output rating",
   "Use a Darlington, a field-effect device, or a buffer stage"]],
 ("c13_mosfet","Measuring on-state loss. The voltage across the conducting device at a known load "
  "current gives its dissipation directly.",46),
 ["Drive a switch to full saturation; a transistor switch running hot is usually underdriven, not "
  "undersized.",
  "Fit a suppression diode across every inductive load as a matter of routine.",
  "Use the minimum current gain from the data sheet, never the typical value, when sizing base "
  "drive.",
  "Treat insulated-gate devices as static sensitive from the moment they leave the packaging.",
  "Compute conduction and switching loss separately when the switching frequency is appreciable."],
 ["State which terminal of a bipolar transistor symbol carries the arrow, and what its direction "
  "indicates.",
  "A transistor has a base current of 0.4 mA and a collector current of 48 mA. Find the gain.",
  "For the device above, find the emitter current.",
  "Name the three operating regions and state which two a switch should use.",
  "Explain why a switching transistor must be driven into saturation rather than the active region.",
  "A load draws 120 mA and the minimum gain is 40. Find the minimum base current.",
  "Using a factor of four on the answer above, find the base resistor for a 5 V drive.",
  "State what a suppression diode across a relay coil does and why it is necessary.",
  "State the fundamental difference between how a bipolar and a field-effect transistor are "
  "controlled.",
  "A field-effect device has 25 m\u03a9 on resistance and carries 8 A. Find its on-state loss.",
  "A bipolar device saturating at 0.35 V carries the same 8 A. Find its loss and compare.",
  "Explain why paralleled field-effect devices share current but paralleled bipolar devices do not.",
  "State two handling precautions required for insulated-gate devices.",
  "Explain why a device that is cool at 1 kHz switching may overheat at 100 kHz with the same "
  "current."],
 [["1","The emitter; its direction shows conventional current","Pointing out is n-p-n, pointing "
   "in is p-n-p"],
  ["2","120","\u03b2 = I_C/I_B"],
  ["3","48.4 mA","I_E = I_B + I_C"],
  ["4","Cut-off, active, saturation; a switch uses cut-off and saturation","The active region "
   "dissipates heavily"],
  ["5","To minimise dissipation","In saturation the device drops a few tenths of a volt rather "
   "than a large fraction of the supply"],
  ["6","3 mA","I_B = I_C/\u03b2(min)"],
  ["7","358 \u03a9, so use 330 \u03a9","R_B = (5 \u2212 0.7)/0.012"],
  ["8","It conducts the coil's collapsing current","Without it the induced reverse voltage "
   "exceeds the transistor's rating"],
  ["9","Current control against voltage control","The bipolar needs continuous base current; the "
   "field-effect device needs only gate charge"],
  ["10","1.6 W","P = I\u00b2 R_DS(on)"],
  ["11","2.8 W; the field-effect device is better here","P = V_CE(sat) I, which is linear in "
   "current"],
  ["12","On resistance rises with temperature","The hottest field-effect device sheds current; a "
   "bipolar device's drop falls with temperature, so it takes more"],
  ["13","Antistatic strap and a gate-to-source resistor","The gate oxide is destroyed by static "
   "and a floating gate can self-trigger"],
  ["14","Switching loss is proportional to frequency","Each transition dissipates energy, so a "
   "hundredfold frequency increase multiplies that component accordingly"]],
 ["A transistor's third terminal controls conduction between the other two, which makes "
  "electronic switching and amplification possible.",
  "Bipolar devices are current controlled and consume base current continuously; field-effect "
  "devices are voltage controlled and need only gate charge.",
  "Cut-off and saturation are the switching states; the active region is for amplification and "
  "dissipates heavily.",
  "Base drive for a switch is computed from minimum gain and then multiplied by three to five to "
  "guarantee saturation.",
  "Every inductive load switched by a semiconductor needs a suppression diode.",
  "Bipolar on-state loss is linear in current; field-effect loss is quadratic, so each wins in a "
  "different current range.",
  "Switching loss rises with frequency and is separate from conduction loss."],
 [["Current balance","I_E = I_B + I_C","Any bipolar transistor"],
  ["Current gain","\u03b2 = I_C / I_B","Active region"],
  ["Minimum base drive","I_B = I_C / \u03b2(min)","Switch design"],
  ["Base resistor","R_B = (V_drive \u2212 0.7)/I_B","Bipolar switch"],
  ["Bipolar on-state loss","P = V_CE(sat) I_C","Saturated switch"],
  ["Field-effect on-state loss","P = I_D\u00b2 R_DS(on)","Conducting channel"],
  ["Gate drive power","P = Q f V","Switching at frequency f"]],
 [["Current gain","The ratio of collector current to base current in the active region"],
  ["Saturation","The fully on state, where collector current is set by the external circuit"],
  ["Cut-off","The fully off state, with negligible collector current"],
  ["Active region","The proportional region used for amplification"],
  ["On resistance","The effective resistance of a conducting field-effect channel"],
  ["Suppression diode","A diode across an inductive load that conducts its collapsing current"],
  ["Current hogging","The tendency of paralleled bipolar devices to share current unequally"]],
 "A single transistor amplifies, but its gain varies between devices and with temperature. "
 "Building a feedback amplifier from many transistors in one package gives the operational "
 "amplifier, whose behaviour depends on external components instead. The next chapter develops it.",
)
