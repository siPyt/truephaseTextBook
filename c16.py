# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH16=mkch(16,"Power supplies and protection",
 "Delivering a stable supply, and surviving what the installation does to it",
 "Every circuit in the previous four chapters assumes a clean, steady supply of the right "
 "voltage. Producing that from an alternating mains input, holding it steady as load and input "
 "vary, and protecting both the supply and its load are what a power supply does. Most "
 "electronic equipment failures trace back to this part of the circuit.",
 ["Describe the stages of a linear power supply and the function of each.",
  "Compute the dissipation of a series regulator and size its heatsink requirement.",
  "Explain how a switching supply differs and why its efficiency is so much higher.",
  "Compute line and load regulation from measurements.",
  "Select overcurrent and overvoltage protection appropriate to a supply.",
  "Explain earthing, isolation and the purpose of a protective conductor in equipment supplies."],
 ("c16_psu","A complete linear supply. The transformer isolates and steps down, the bridge "
  "rectifies, the reservoir capacitor smooths, and the regulator holds the output steady.",46),
 [dict(h2="Stages of a linear supply",
   paras=["A linear supply performs four distinct jobs in sequence. The transformer isolates the "
    "output from the mains and steps the voltage down. The rectifier converts the alternating "
    "waveform to unidirectional. The reservoir capacitor smooths that into a roughly steady "
    "voltage with ripple on it. The regulator then removes the remaining ripple and holds the "
    "output constant despite changes in input voltage and load current.",
    "Each stage must be sized for what the next one demands. The regulator needs a minimum input "
    "above its output, called the dropout voltage, maintained even at the bottom of the ripple "
    "and at the lowest expected mains voltage. Designing the reservoir capacitor without "
    "accounting for that minimum is why some supplies work on the bench and fail on a low mains."],
   eq=["V_in(min) at the ripple trough > V_out + V_dropout",
       "Headroom = V_in \u2212 V_out",
       "Stages: isolate \u2192 rectify \u2192 smooth \u2192 regulate"],
   panel=("Headroom must survive the worst case, not the typical case",
     ["The regulator sees the lowest input at the ripple trough, on a low mains, at full load.",
      "Too little headroom and the output follows the input down, with ripple appearing on it.",
      "Too much headroom and the regulator dissipates the surplus as heat.",
      "Design for the minimum case and then check dissipation at the maximum case."])),
  dict(h2="The series regulator and its heat",
   paras=["A linear regulator works by dropping the surplus voltage across a series device, "
    "adjusting that drop continuously so the output stays constant. It is simple, quiet and has "
    "excellent output purity, which is why it remains the choice for sensitive analogue work.",
    "The cost is heat. Every volt of surplus multiplied by every ampere of load becomes heat in "
    "the regulator, and none of it reaches the load. A supply dropping twelve volts to five at "
    "two amperes delivers ten watts and dissipates fourteen. Efficiency falls as the difference "
    "between input and output grows, so a linear supply is poorly suited to large voltage "
    "reductions or high currents."],
   eq=["P_reg = (V_in \u2212 V_out) \u00d7 I_load",
       "\u03b7 \u2248 V_out / V_in",
       "Required thermal path from P_reg and the permitted temperature rise"],
   fig=("c16_series_pass","A series regulator. The pass device carries the full load current and "
     "drops the difference between input and output, dissipating that product as heat.",46)),
  dict(h2="Switching supplies",
   paras=["A switching supply avoids the dissipation by not dropping voltage continuously. "
    "Instead it switches the input on and off rapidly into an inductor and capacitor, and varies "
    "the proportion of time it is on to set the average output. Because the switch is either "
    "fully on or fully off, it dissipates little in either state.",
    "The result is efficiency typically between eighty-five and ninety-five per cent, almost "
    "independent of the voltage ratio, and much smaller magnetic components because the switching "
    "frequency is far above mains frequency. The penalties are electrical noise at the switching "
    "frequency and its harmonics, greater circuit complexity, and a failure mode that can place "
    "the input voltage on the output if the switch fails short."],
   eq=["Duty ratio D = on time / period",
       "Step-down output:  V_out \u2248 D V_in",
       "Efficiency largely independent of the voltage ratio"],
   table=(["Property","Linear supply","Switching supply"],
     [["Efficiency","Low, falls as the ratio grows","High, 85 to 95 %"],
      ["Heat produced","Large, proportional to voltage dropped","Small"],
      ["Output noise","Very low","Switching frequency and harmonics present"],
      ["Size and mass","Large mains-frequency transformer","Small high-frequency magnetics"],
      ["Complexity","Low","High"],
      ["Best suited to","Sensitive analogue, small voltage drops","General supply, large drops, "
       "high current"]],None)),
  dict(h2="Regulation and measurement",
   paras=["A supply's quality is expressed in two figures. Line regulation is how much the output "
    "changes when the input voltage varies across its specified range. Load regulation is how "
    "much it changes from no load to full load. Both are quoted as a percentage of the nominal "
    "output and both are measured by deliberately varying one condition while holding the other "
    "fixed.",
    "Output impedance is the underlying cause of load regulation: a supply with low output "
    "impedance holds its voltage as current is drawn. Ripple rejection describes how much of the "
    "input ripple survives to the output, and is usually quoted in decibels."],
   eq=["Line regulation % = \u0394V_out / V_out(nom) \u00d7 100  for the input range",
       "Load regulation % = (V_noload \u2212 V_fullload)/V_nominal \u00d7 100",
       "Output impedance = \u0394V_out / \u0394I_load"]),
  dict(h2="Protecting the supply and the load",
   paras=["Protection is needed in both directions. The supply must be protected against an "
    "overload or short circuit in the load, which is the job of a fuse or a current limit; and "
    "the load must be protected against the supply failing in a way that raises the output "
    "voltage, which is the job of overvoltage protection.",
    "A fuse interrupts a sustained fault but is slow against a short-lived surge, so electronic "
    "current limiting is usually added to act immediately. Overvoltage protection matters because "
    "a shorted pass device in a linear supply, or a shorted switch in a switching supply, places "
    "the unregulated input directly on the load, which may destroy everything connected."],
   fig=("c16_prot","Protection arrangements. The fuse clears a sustained fault, while a voltage "
     "limiting device across the output absorbs transients and limits overvoltage.",46),
   bh="Layers of protection in a supply",
   bullets=["Input fuse, rated for inrush but clearing a genuine fault.",
     "Transformer thermal cut-out, where fitted.",
     "Electronic current limiting, acting immediately on an output short.",
     "Output fuse where several loads share one supply.",
     "Overvoltage protection against pass-device failure.",
     "Transient suppression at the input against mains surges.",
     "Thermal shutdown in the regulator against loss of cooling."]),
  dict(h2="Isolation, earthing and the protective conductor",
   paras=["A mains-supplied power supply must separate its output from the mains, and the "
    "transformer provides that separation. The quality of the separation is what distinguishes a "
    "supply suitable for accessible low-voltage circuits from one that is not, and it is defined "
    "by the insulation between the windings and the spacing within the unit.",
    "Where exposed conductive parts of equipment could become live through an insulation failure, "
    "they are connected to a protective conductor so that a fault produces enough current to "
    "operate the protective device. A supply whose output is referenced to the protective "
    "conductor cannot be connected in series with another similarly referenced supply without "
    "creating a parallel path, which is a frequent cause of unexplained circulating currents in "
    "multi-supply installations.",
    "National wiring rules set the detailed requirements for conductor sizing, protective device "
    "selection and isolation in these circuits. Where a specific national code is being applied, "
    "the edition in force must be identified before relying on any particular article."],
   panel=("Why two earthed supplies cannot simply be stacked",
     ["If both outputs reference the protective conductor, that conductor bridges them.",
      "The intended series connection is shorted out through the protective path.",
      "Circulating current flows and the voltages are not what was expected.",
      "Use one supply with a floating output, or a genuinely isolated second supply."])),
 ],
 [ex("Regulator dissipation and heatsink requirement",
   "A linear regulator produces 5 V at 1.5 A from an unregulated input of 14 V.",
   "The dissipation, the efficiency, and the implication for cooling.",
   [("Voltage dropped","14 \u2212 5 = 9 V"),
    ("Dissipation","P = 9 \u00d7 1.5 = 13.5 W"),
    ("Power delivered","5 \u00d7 1.5 = 7.5 W"),
    ("Efficiency","7.5/21 = 36 %"),
    ("Cooling","13.5 W demands a substantial heatsink")],
   "Nearly twice as much power is wasted as delivered. A switching supply at ninety per cent "
   "efficiency would dissipate under a watt for the same output, which is why linear regulators "
   "are confined to small drops or small currents."),
  ex("Reservoir capacitor sized for regulator headroom",
   "A 12 V regulator with a 2 V dropout requirement draws 1 A from a bridge rectifier on a 50 Hz "
   "supply. The rectified peak is 19 V.",
   "The maximum permissible ripple and the required capacitance.",
   [("Minimum acceptable input","12 + 2 = 14 V"),
    ("Available ripple allowance","19 \u2212 14 = 5 V peak to peak"),
    ("Ripple frequency","100 Hz for a bridge"),
    ("Required capacitance","C = I/(f V) = 1/(100 \u00d7 5) = 2000 \u00b5F"),
    ("With margin for low mains","Fit 4700 \u00b5F")],
   "The capacitor is sized by the regulator's headroom requirement, not by any ripple target of "
   "its own. The margin covers a low mains condition, where the peak falls and the headroom "
   "shrinks."),
  ex("Line and load regulation from measurements",
   "A 12 V supply measures 12.04 V at no load and 11.88 V at full load. Varying the input across "
   "its full range changes the output from 11.96 V to 12.02 V.",
   "The load regulation, the line regulation, and the output impedance if full load is 2 A.",
   [("Load regulation","(12.04 \u2212 11.88)/12 \u00d7 100 = 1.33 %"),
    ("Line regulation","(12.02 \u2212 11.96)/12 \u00d7 100 = 0.5 %"),
    ("Output impedance","\u0394V/\u0394I = 0.16/2 = 0.08 \u03a9"),
    ("Assessment","Both figures are typical of a competent linear supply")],
   "The output impedance of 80 milliohms is what produces the load regulation. A supply feeding a "
   "pulsed load would need a lower figure, or local decoupling at the load to supply the pulses."),
  ex("Switching supply duty ratio and efficiency comparison",
   "A step-down switching supply produces 5 V at 4 A from a 24 V input at 88 % efficiency.",
   "The duty ratio, the input power, the dissipation, and the dissipation a linear supply would "
   "have had.",
   [("Duty ratio","D \u2248 V_out/V_in = 5/24 = 0.21"),
    ("Output power","5 \u00d7 4 = 20 W"),
    ("Input power","20/0.88 = 22.7 W"),
    ("Switching supply dissipation","22.7 \u2212 20 = 2.7 W"),
    ("Linear equivalent dissipation","(24 \u2212 5) \u00d7 4 = 76 W"),
    ("Ratio","The linear supply would dissipate 28 times as much")],
   "Seventy-six watts in a pass device is impractical to cool in most enclosures. This comparison "
   "is why nearly all equipment supplies with large voltage ratios are switching types."),
  ex("Fuse selection for a supply",
   "A supply draws 0.9 A from the mains in normal operation, with an inrush of 12 A for 20 ms at "
   "switch-on.",
   "A suitable fuse rating and type.",
   [("Continuous requirement","Must carry 0.9 A indefinitely"),
    ("Inrush requirement","Must not clear on 12 A for 20 ms"),
    ("Rating","Choose 1.25 A or 1.6 A, above the continuous current"),
    ("Type","Time-delay, to ride through the inrush"),
    ("Fault requirement","Must clear a genuine sustained overload")],
   "A fast-acting fuse of the same rating would clear on the inrush at every switch-on. The "
   "selection must satisfy three separate conditions, and only the type distinguishes them.")],
 lab("supply stages, regulation, dissipation and protection",
  "Build a linear supply stage by stage and measure the waveform at each point, then measure line "
  "and load regulation, compute regulator dissipation against measured temperature rise, and "
  "verify current limiting and overvoltage protection.",
  ["Transformer, 230 V to 18 V, supplied through an isolating transformer and a residual current "
   "device.",
   "Bridge rectifier, 2 A, on a small heatsink.",
   "Electrolytic capacitors, 470 \u00b5F and 4700 \u00b5F, rated above 50 V.",
   "Three-terminal regulator, 12 V, with a heatsink and mounting hardware.",
   "Resistive load bank, switchable, and a decade resistance box.",
   "Variable alternating supply to simulate a varying mains input.",
   "Two multimeters, an oscilloscope with an isolated input, and an infrared thermometer.",
   "Fuses of assorted ratings and types, and a voltage limiting device for the output."],
  ["Confirm the bench supply is fed through an isolating transformer and a residual current device "
   "before beginning.",
   "Connect the transformer alone and measure its secondary open-circuit voltage. Compute the "
   "expected rectified peak.",
   "Add the bridge rectifier with a 1 k\u03a9 load and observe the unsmoothed waveform. Record its "
   "peak, mean and ripple frequency.",
   "Add the 470 \u00b5F capacitor and record the new mean output and the ripple at 0.2 A load.",
   "Replace it with the 4700 \u00b5F capacitor and record the ripple again at the same load.",
   "Add the regulator with its heatsink. Measure the regulated output and the ripple remaining "
   "on it.",
   "Compare the ripple before and after the regulator and express the reduction in decibels.",
   "Load regulation: record the output at no load and at four increasing load steps up to 1 A.",
   "At each step, measure the voltage across the regulator and compute its dissipation.",
   "Measure the regulator case temperature at the highest load after five minutes.",
   "Line regulation: hold the load at 0.5 A and vary the input from the variable supply across a "
   "range of plus and minus 10 per cent, recording the output at each setting.",
   "Reduce the input further until the output begins to fall, and record the input at which "
   "regulation is lost. Compare with the stated dropout voltage.",
   "Discharge the capacitors through a resistor and prove dead.",
   "Fit a fuse one size above the measured continuous current and confirm the supply starts "
   "without clearing it.",
   "Apply a short circuit to the output briefly through an ammeter and record the current the "
   "supply allows. Remove it immediately.",
   "Discharge, prove dead, and fit the voltage limiting device across the output. Note the "
   "voltage at which it would act."],
  ("c16_psu","The supply under test. Measurements are taken at the transformer secondary, after "
   "the rectifier, after the reservoir capacitor and at the regulated output.",46),
  ["Measurement point or condition","Voltage (V)","Ripple (V pk-pk)","Dissipation (W)","Comment"],
  [["Secondary, open circuit","","","",""],["After rectifier, unsmoothed","","","",""],
   ["After 470 \u00b5F at 0.2 A","","","",""],["After 4700 \u00b5F at 0.2 A","","","",""],
   ["Regulated output, no load","","","",""],["Regulated output, 0.25 A","","","",""],
   ["Regulated output, 0.5 A","","","",""],["Regulated output, 1.0 A","","","",""],
   ["Input at loss of regulation","","","",""],["Short-circuit current","","","",""]],
  ["How did your smoothed voltage compare with the rectified peak and with the unsmoothed mean? "
   "Explain which it approached and why.",
   "By what factor did ripple fall when you increased the capacitance tenfold? Compare with the "
   "prediction.",
   "Express the regulator's ripple reduction in decibels from your measurements before and after it.",
   "Compute your load regulation as a percentage. What output impedance does that imply at your "
   "full-load current?",
   "Compute your line regulation across the input range you tested.",
   "At what input voltage was regulation lost, and how does the difference between that and the "
   "output compare with the stated dropout voltage?",
   "Compute the regulator dissipation at 1 A and compare the measured temperature rise with what "
   "that dissipation implies for your heatsink.",
   "Compute the efficiency of your supply at 1 A. How would a switching supply of the same output "
   "compare?",
   "What short-circuit current did the supply allow, and is that consistent with an internal "
   "current limit?",
   "Why must a supply have both a fuse and electronic current limiting rather than only one of them?"],
  ["Supply the bench through an isolating transformer and a residual current device at all times.",
   "Do not connect an earthed oscilloscope ground to a mains-referenced point; use an isolated or "
   "differential input.",
   "Reservoir capacitors hold a dangerous charge after the supply is removed. Discharge through a "
   "resistor and prove dead before touching the circuit.",
   "Observe electrolytic capacitor polarity; a reversed electrolytic can rupture violently.",
   "Apply the output short circuit only momentarily and through an ammeter, never by hand.",
   "The regulator and its heatsink reach high temperatures. Use the thermometer, not a finger.",
   "Prove dead and discharge before fitting or removing any component."]),
 [["Output voltage correct at no load but falls under load","Regulator losing headroom at the "
   "ripple trough, or transformer undersized","Observe the regulator input on an oscilloscope "
   "while loaded","Increase the reservoir capacitance or use a higher secondary voltage"],
  ["Ripple appears on the regulated output only on a low mains","Dropout voltage reached at the "
   "trough of the ripple","Measure the minimum instantaneous input at full load","Raise the "
   "input voltage or increase the capacitance to reduce the ripple depth"],
  ["Regulator shuts down intermittently when warm","Thermal protection operating because "
   "dissipation exceeds the heatsink capability","Compute dissipation and measure case "
   "temperature","Fit a larger heatsink, improve airflow, or change to a switching supply"],
  ["Equipment downstream destroyed by overvoltage","Pass device or switch failed short, placing "
   "the unregulated input on the output","Measure the output with the load disconnected","Replace "
   "the supply and fit overvoltage protection across the output"],
  ["Input fuse clears at every switch-on","Fast-acting type fitted where the inrush requires a "
   "time-delay type","Measure the inrush current and duration","Fit a time-delay fuse of suitable "
   "rating"],
  ["Noise from a switching supply disturbs analogue measurements","Switching frequency and "
   "harmonics coupling into the signal circuit","Observe the analogue signal with the supply "
   "running and inhibited","Add filtering, improve layout and separation, or use a linear supply "
   "for that circuit"],
  ["Unexplained circulating current between two supplies","Both outputs referenced to the "
   "protective conductor, creating a parallel path","Test for continuity between the two output "
   "reference points","Use one floating output or a genuinely isolated supply"],
  ["Electrolytic capacitor has bulged or vented","Exceeded ripple current rating, excessive "
   "temperature, or reverse polarity","Inspect, and check the ripple current against the "
   "component rating","Replace with a component rated for the ripple current and verify polarity"]],
 ("c16_prot","Verifying protection. The current limit is checked through an ammeter and the "
  "overvoltage device is selected to act below the downstream equipment's limit.",46),
 ["Design headroom for the worst case: ripple trough, low mains and full load together.",
  "Compute regulator dissipation before selecting a package, and provide the thermal path to match.",
  "Discharge reservoir capacitors through a resistor and prove dead as a routine step.",
  "Fit overvoltage protection wherever a supply failure could destroy expensive downstream "
  "equipment.",
  "Check whether a supply output is referenced to the protective conductor before connecting two "
  "supplies together.",
  "Match the fuse type, not only its rating, to the inrush the supply actually draws."],
 ["Name the four stages of a linear power supply in order and state the function of each.",
  "A regulator drops 15 V to 9 V at 0.8 A. Find its dissipation.",
  "Find the efficiency of the supply above.",
  "Explain why a linear supply becomes impractical for large voltage reductions at high current.",
  "A 5 V regulator has a 2.5 V dropout. State the minimum input it requires.",
  "A bridge rectifier on 50 Hz feeds a regulator needing 3 V of ripple allowance at 0.75 A. Find "
  "the capacitance required.",
  "Explain how a switching supply achieves high efficiency.",
  "A step-down switching supply gives 12 V from 48 V. Find the approximate duty ratio.",
  "A supply gives 24.1 V at no load and 23.7 V at 3 A. Find the load regulation and the output "
  "impedance.",
  "State the difference between line regulation and load regulation.",
  "State one advantage and one disadvantage of a switching supply compared with a linear supply.",
  "Explain why a supply needs both a fuse and electronic current limiting.",
  "Explain what overvoltage protection guards against and why it is needed.",
  "Explain why two supplies whose outputs are both referenced to the protective conductor cannot "
  "be connected in series.",
  "State why the edition of a national wiring code must be identified before relying on a "
  "particular requirement."],
 [["1","Transformer, rectifier, reservoir capacitor, regulator","Isolate and step down, convert "
   "to unidirectional, smooth, then hold steady"],
  ["2","4.8 W","P = (V_in \u2212 V_out) I"],
  ["3","60 %","\u03b7 \u2248 V_out/V_in"],
  ["4","Dissipation is the dropped voltage times the current","Both the heat and the cooling "
   "requirement become impractical"],
  ["5","7.5 V","Output plus dropout"],
  ["6","2500 \u00b5F","C = I/(f_ripple V_ripple) with f_ripple = 100 Hz"],
  ["7","The switch is either fully on or fully off","It drops little voltage while conducting and "
   "carries none while off, so it dissipates little"],
  ["8","0.25","D \u2248 V_out/V_in"],
  ["9","1.67 %; 0.133 \u03a9","Regulation from the voltage change; impedance from \u0394V/\u0394I"],
  ["10","Line regulation responds to input change; load regulation to load change","They are "
   "measured by varying one while holding the other fixed"],
  ["11","High efficiency; switching noise","Less heat and smaller magnetics, but noise at the "
   "switching frequency"],
  ["12","The fuse is too slow for a transient fault","Current limiting acts immediately, while "
   "the fuse clears a sustained fault"],
  ["13","The pass device or switch failing short","That places the unregulated input directly on "
   "the load, destroying downstream equipment"],
  ["14","The protective conductor bridges both outputs","It shorts out the intended series "
   "connection and circulating current flows"],
  ["15","Requirements change between editions","A citation is only meaningful with its edition "
   "identified"]],
 ["A linear supply isolates, rectifies, smooths and regulates, and each stage must be sized for "
  "the demands of the next.",
  "Regulator headroom must be maintained at the ripple trough, on a low mains, at full load.",
  "A series regulator dissipates the dropped voltage times the load current, so efficiency falls "
  "as the voltage ratio grows.",
  "A switching supply varies duty ratio instead of dropping voltage, giving high efficiency and "
  "small magnetics at the cost of noise and complexity.",
  "Line and load regulation quantify supply quality, and output impedance is the underlying cause "
  "of load regulation.",
  "Protection is needed in both directions: current limiting and fusing for the supply, "
  "overvoltage protection for the load.",
  "Isolation and the protective conductor arrangement determine whether supplies can be combined "
  "safely, and national code requirements must be applied by edition."],
 [["Regulator dissipation","P = (V_in \u2212 V_out) I_load","Linear series regulator"],
  ["Linear efficiency","\u03b7 \u2248 V_out / V_in","Linear supply"],
  ["Minimum input","V_in > V_out + V_dropout","At the ripple trough, full load"],
  ["Reservoir capacitance","C = I/(f_ripple V_ripple)","Capacitor-smoothed rectifier"],
  ["Switching output","V_out \u2248 D V_in","Step-down switching converter"],
  ["Load regulation","(V_nl \u2212 V_fl)/V_nom \u00d7 100","No load to full load"],
  ["Output impedance","Z_out = \u0394V_out/\u0394I_load","From load regulation measurements"]],
 [["Dropout voltage","The minimum excess of input over output a regulator requires"],
  ["Headroom","The margin between the input and the output of a regulator"],
  ["Duty ratio","The proportion of each switching period for which the switch conducts"],
  ["Line regulation","Output change caused by a change in input voltage"],
  ["Load regulation","Output change caused by a change in load current"],
  ["Current limiting","Electronic restriction of output current during a fault"],
  ["Overvoltage protection","A device that limits the output if the regulator fails short"],
  ["Protective conductor","The conductor connecting exposed conductive parts for fault protection"]],
 "Single-phase supplies serve most electronic equipment, but industrial power is distributed and "
 "consumed in three phases. The next chapter develops three-phase systems, their connections and "
 "their measurement.",
)
