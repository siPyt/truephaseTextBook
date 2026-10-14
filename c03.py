# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH3=mkch(3,"Series, parallel and divider rules",
 "Reducing networks by inspection, and the two shortcuts worth memorising",
 "Most real circuits are series-parallel combinations. Learning to reduce them by inspection, "
 "and to use the divider rules, removes simultaneous equations from the majority of your work "
 "and makes mental estimation possible on site.",
 ["Compute equivalent resistance for series, parallel and mixed networks.",
  "Apply the voltage divider and current divider rules correctly, including their conditions.",
  "Predict how adding a load changes a divider's output.",
  "Measure resistance correctly, including why the circuit must be de-energised.",
  "Use resistivity to find the resistance of a conductor run from its dimensions."],
 ("c3_series","A series string. The same current passes through every element, and the applied "
  "voltage divides in proportion to resistance.",44),
 [dict(h2="Series: one current, shared voltage",
   paras=["Elements are in series when they carry the identical current because there is only "
    "one path. The equivalent resistance is the sum, and the applied voltage divides in direct "
    "proportion to each resistance. The largest resistance therefore takes the largest share of "
    "the voltage, which is the basis of the divider rule.",
    "Series behaviour explains why a single open circuit stops everything, and why a "
    "high-resistance joint anywhere in a string starves the entire load. It also explains why "
    "measuring current anywhere in a series string gives the same answer."],
   eq=["R_eq = R\u2081 + R\u2082 + ... + R_n",
       "I is identical in every element"]),
  dict(h2="Parallel: one voltage, shared current",
   paras=["Elements are in parallel when they share both end nodes and therefore the identical "
    "voltage. Conductances add, so the reciprocal of the equivalent resistance is the sum of the "
    "reciprocals. The equivalent is always smaller than the smallest branch, which is a useful "
    "sanity check on any parallel calculation.",
    "For two resistors the product-over-sum form is quicker. For n identical resistors the "
    "equivalent is simply R divided by n. Both shortcuts are worth memorising because they let "
    "you check a calculator result instantly."],
   eq=["1/R_eq = 1/R\u2081 + 1/R\u2082 + ... + 1/R_n",
       "Two only:  R_eq = R\u2081 R\u2082 / (R\u2081 + R\u2082)",
       "n equal:   R_eq = R / n"],
   fig=("c3_parallel","A parallel group. Every branch sees the same voltage and the branch "
     "currents sum to the supply current.",44),
   panel=("Checks that catch parallel errors",
     ["The equivalent must be smaller than the smallest branch.",
      "Adding a branch always lowers the equivalent resistance and raises the total current.",
      "If two equal resistors give anything other than half their value, the arithmetic is wrong."])),
  dict(h2="The voltage divider rule",
   paras=["In a series pair the voltage across one element is the supply voltage multiplied by "
    "that element's resistance over the total. This holds only while no current is drawn from "
    "the junction, which is the condition beginners most often forget.",
    "A divider loaded by a finite resistance no longer follows the simple ratio. The loaded "
    "output is found by first combining the lower resistor with the load in parallel, then "
    "reapplying the rule. If the load resistance is at least ten times the lower resistor the "
    "error stays under ten percent, which is the usual design guideline."],
   eq=["V_out = V_in \u00d7 R\u2082 / (R\u2081 + R\u2082)",
       "Loaded:  R\u2082\u2032 = R\u2082 R_L / (R\u2082 + R_L)"],
   fig=("c3_divider","A voltage divider with and without a load. Drawing current from the "
     "junction lowers the output below the unloaded ratio.",46)),
  dict(h2="The current divider rule",
   paras=["In a parallel pair the current in one branch is the total current multiplied by the "
    "opposite resistance over the sum. The inversion is deliberate: the smaller resistance takes "
    "the larger current, which is the opposite of the voltage divider's behaviour and a frequent "
    "source of confusion.",
    "The current divider is the rule that explains parallel fault paths. When an unintended "
    "low-resistance path appears alongside the intended load, it takes most of the current, "
    "which is both why fuses operate and why earth faults are dangerous."],
   eq=["I\u2081 = I_total \u00d7 R\u2082 / (R\u2081 + R\u2082)",
       "The smaller resistance carries the larger current"]),
  dict(h2="Resistivity: resistance from conductor dimensions",
   paras=["The resistance of a uniform conductor is proportional to its length and inversely "
    "proportional to its cross-sectional area, with resistivity as the material constant. "
    "Doubling the run doubles the resistance; doubling the area halves it.",
    "Resistivity rises with temperature in metals, which is why a motor winding measures higher "
    "resistance hot than cold, and why insulation resistance measurements must be recorded with "
    "the temperature noted. A measured winding resistance can in fact be used as a thermometer."],
   eq=["R = \u03c1 L / A",
       "R_hot = R_cold [1 + \u03b1 (T_hot \u2212 T_cold)]"],
   table=(["Material","Resistivity at 20 "+DEG+"C ("+OH+"\u00b7m)","Temperature coefficient (per "+DEG+"C)","Typical use"],
     [["Silver","1.59 \u00d7 10\u207b\u2078","0.0038","Contacts, plating"],
      ["Copper","1.68 \u00d7 10\u207b\u2078","0.00393","Conductors, windings"],
      ["Aluminium","2.65 \u00d7 10\u207b\u2078","0.00403","Feeders, busbar"],
      ["Nichrome","1.10 \u00d7 10\u207b\u2076","0.0004","Heating elements"],
      ["Carbon","3.5 \u00d7 10\u207b\u2075","\u22120.0005","Brushes, resistors"]],None)),
 ],
 [ex("Mixed series-parallel reduction",
   "A 24 V source feeds 100 "+OH+" in series with a parallel pair of 300 "+OH+" and 600 "+OH+".",
   "The equivalent resistance, the supply current and the current in each parallel branch.",
   [("Combine the parallel pair","R_p = 300\u00d7600/900 = 200 "+OH),
    ("Add the series element","R_eq = 100 + 200 = 300 "+OH),
    ("Supply current","I = 24/300 = 0.08 A = 80 mA"),
    ("Voltage across the pair","V_p = 0.08 \u00d7 200 = 16 V"),
    ("Branch currents","I\u2083\u2080\u2080 = 16/300 = 53.3 mA ; I\u2086\u2080\u2080 = 16/600 = 26.7 mA")],
   "53.3 + 26.7 = 80 mA, equal to the supply current, so KCL is satisfied at the junction."),
  ex("A divider that sags under load",
   "A 12 V supply drives a divider of R\u2081 = 10 k"+OH+" and R\u2082 = 10 k"+OH+". A 10 k"+OH+" load is then connected across the output.",
   "The unloaded and loaded output voltages, and the percentage error.",
   [("Unloaded ratio","V = 12 \u00d7 10/20 = 6.00 V"),
    ("Combine R\u2082 with the load","R\u2082\u2032 = 10\u00d710/20 = 5 k"+OH),
    ("Reapply the rule","V = 12 \u00d7 5/15 = 4.00 V"),
    ("Error introduced","(6.00 \u2212 4.00)/6.00 = 33 %")],
   "The load equals R\u2082, far below the ten-times guideline, so a third of the output is lost. "
   "Raising the load to 100 k"+OH+" would give 5.71 V, an error of under 5 %."),
  ex("Resistance of a conductor run",
   "A 60 m run of copper with a 2.5 mm\u00b2 cross-section carries current to a load, and the "
   "return conductor is the same length.",
   "The loop resistance at 20 "+DEG+"C and the drop at 16 A.",
   [("Total conductor length","L = 2 \u00d7 60 = 120 m"),
    ("Convert the area","A = 2.5 mm\u00b2 = 2.5 \u00d7 10\u207b\u2076 m\u00b2"),
    ("Apply the resistivity relation","R = 1.68\u00d710\u207b\u2078 \u00d7 120 / 2.5\u00d710\u207b\u2076 = 0.806 "+OH),
    ("Voltage drop at 16 A","V = 16 \u00d7 0.806 = 12.9 V"),
    ("Drop as a percentage of 230 V","12.9/230 \u00d7 100 = 5.6 %")],
   "5.6 % exceeds the 3 % branch-circuit guidance in the NFPA 70 (2023) 210.19(A) informational "
   "note, so this run needs a larger conductor.")],
 lab("series and parallel resistance, and a loaded divider",
  "Confirm the series and parallel equivalence formulas against measurement, then demonstrate "
  "experimentally that drawing current from a divider lowers its output below the simple ratio.",
  ["DC supply, 0\u201320 V, current limited to 0.25 A.",
   "Resistors: two 10 k"+OH+", one 1 k"+OH+", one 100 k"+OH+", one 330 "+OH+", one 470 "+OH+".",
   "Two multimeters, one used as an ohmmeter and one as a voltmeter.",
   "Breadboard or terminal strip and marked leads."],
  ["With the supply disconnected, measure and record every resistor individually. Use these "
   "values, not the printed ones, in your predictions.",
   "Connect the 330 "+OH+" and 470 "+OH+" in series. Predict, then measure, the equivalent "
   "resistance with the circuit de-energised.",
   "Connect the same pair in parallel. Predict, then measure, the equivalent resistance.",
   "Build the divider from two 10 k"+OH+" resistors and set the supply to 12.0 V.",
   "Measure the unloaded output voltage and compare it with the predicted 6 V.",
   "Connect the 1 k"+OH+" as a load across the output, measure, and record the sag.",
   "Replace the load with 10 k"+OH+", then 100 k"+OH+", measuring each time.",
   "Plot output voltage against load resistance and mark where the error falls below 5 %."],
  ("c3_divider","The divider under test. The load is connected across the output, between the "
   "junction and the reference node.",46),
  ["Load ("+OH+")","Predicted V_out","Measured V_out","Error (%)","Comment"],
  [["none (open)","6.00","","",""],["100 k","","","",""],["10 k","","","",""],
   ["1 k","","","",""],["470","","","",""],["330","","","",""]],
  ["At which load resistance did the error first exceed 5 %? Compare that with the ten-times "
   "guideline.",
   "Why must the ohmmeter measurements be made with the supply disconnected?",
   "Your voltmeter has a finite input resistance. Treat it as a load and estimate the error it "
   "introduces on the unloaded reading.",
   "Measured series equivalents are usually very close to prediction while parallel equivalents "
   "deviate more. Suggest why.",
   "Design a divider that delivers 5 V from 12 V into a 10 k"+OH+" load with under 2 % error, "
   "and state your resistor values."],
  ["Keep the supply at or below 20 V with the current limit at 0.25 A.",
   "Never apply an ohmmeter to an energised circuit; the reading is meaningless and the meter "
   "may be damaged.",
   "Check the dissipation in the lowest-value resistor before energising.",
   "Discharge and de-energise before changing any connection."]),
 [["Load runs at reduced output, divider output sags","The divider is loaded far below the "
   "ten-times guideline","Measure the output open and loaded","Lower the divider resistances or "
   "add a buffer stage"],
  ["Parallel group draws far more current than predicted","A branch is short circuited or an "
   "extra branch is present","Isolate and measure each branch resistance","Repair the shorted "
   "branch; account for the extra load"],
  ["Series string dead, full supply voltage across one point","An open element or joint in the "
   "string","Measure voltage across each element in turn","Replace the open element or "
   "re-terminate the joint"],
  ["Measured resistance much higher than the marked value","Measuring in circuit, with parallel "
   "paths included","Disconnect one end of the component and re-measure","Measure components out "
   "of circuit, de-energised"],
  ["Long run delivers low voltage under load only","Conductor resistance, correctly predicted by "
   "resistivity","Measure at the panel and the load, both under load","Increase conductor size "
   "or shorten the run"],
  ["Winding resistance reads high on a hot machine","Normal temperature coefficient of copper",
   "Record the winding temperature with the reading","Correct the value to 20 "+DEG+"C before comparing"]],
 ("c3_series","Fault location in a series string. The open element is the one with the supply "
  "voltage across it while the others read nothing.",44),
 ["Measure resistance out of circuit and de-energised, or you are measuring the whole network.",
  "Use measured resistor values in predictions; tolerance bands are wide enough to matter.",
  "Treat the voltmeter as a load whenever the circuit resistance is above about 100 k"+OH+".",
  "Record conductor length and size when you log a voltage drop, because the two together "
  "explain the reading."],
 ["Find the equivalent of 220 "+OH+", 330 "+OH+" and 470 "+OH+" in series.",
  "Find the equivalent of 220 "+OH+" and 330 "+OH+" in parallel.",
  "Find the equivalent of four 1 k"+OH+" resistors in parallel.",
  "A 20 V supply feeds 1.2 k"+OH+" in series with 1.8 k"+OH+". Find the voltage across each.",
  "A 2 A total current divides between 50 "+OH+" and 150 "+OH+" in parallel. Find each branch current.",
  "A 9 V supply drives a divider of two 4.7 k"+OH+" resistors loaded by 4.7 k"+OH+". Find the output.",
  "A 100 m length of copper of 1.5 mm\u00b2 cross-section is used as a single conductor. Find its "
  "resistance at 20 "+DEG+"C.",
  "A copper winding measures 4.0 "+OH+" at 20 "+DEG+"C. Find its resistance at 75 "+DEG+"C.",
  "Explain why a parallel equivalent must always be less than the smallest branch.",
  "Design a divider giving 3.3 V from 12 V with a total current near 1 mA, and state your values."],
 [["1","1020 "+OH,"Series resistances add"],
  ["2","132 "+OH,"Product over sum: 220\u00d7330/550"],
  ["3","250 "+OH,"R/n for n equal resistors"],
  ["4","8 V and 12 V","Divider ratios 1.2/3.0 and 1.8/3.0 of 20 V"],
  ["5","1.5 A and 0.5 A","Current divider inverts: the smaller resistance takes more"],
  ["6","3.0 V","R\u2082 in parallel with the load gives 2.35 k"+OH+", then 9\u00d72.35/7.05"],
  ["7","1.12 "+OH,"R = \u03c1L/A with L = 100 m, A = 1.5\u00d710\u207b\u2076 m\u00b2"],
  ["8","4.86 "+OH,"R = 4.0[1 + 0.00393\u00d755]"],
  ["9","Adding any branch adds conductance","Total conductance exceeds that of the smallest "
   "branch alone, so the resistance is lower"],
  ["10","About 8.7 k"+OH+" and 3.3 k"+OH,"Ratio 3.3/12 with a total near 12 k"+OH+" for 1 mA"]],
 ["Series elements share one current and divide the voltage; parallel elements share one voltage "
  "and divide the current.",
  "A parallel equivalent is always lower than the smallest branch, which is a one-second check.",
  "The voltage divider rule holds only for an unloaded output; a load must be combined with the "
  "lower resistor first.",
  "The current divider inverts the resistance ratio, so the smaller resistance carries the larger "
  "current.",
  "Conductor resistance follows R = \u03c1L/A and rises with temperature, so runs and hot "
  "windings both read higher.",
  "A load of at least ten times the lower divider resistor keeps the output error under about "
  "ten percent."],
 [["Series equivalent","R_eq = \u03a3 R","One current path only"],
  ["Parallel equivalent","1/R_eq = \u03a3 1/R","Shared end nodes, one voltage"],
  ["Two in parallel","R\u2081R\u2082/(R\u2081+R\u2082)","Quick form for a pair"],
  ["Voltage divider","V_out = V_in R\u2082/(R\u2081+R\u2082)","Unloaded output only"],
  ["Current divider","I\u2081 = I R\u2082/(R\u2081+R\u2082)","Two parallel branches"],
  ["Resistivity","R = \u03c1L/A","Uniform conductor at a stated temperature"],
  ["Temperature correction","R_T = R\u2080[1+\u03b1\u0394T]","Metals over moderate ranges"]],
 [["Equivalent resistance","The single resistance that would draw the same current from the same supply"],
  ["Loaded divider","A divider whose output supplies current, so the simple ratio no longer applies"],
  ["Conductance","The reciprocal of resistance, in siemens; it adds for parallel branches"],
  ["Resistivity","The material property linking resistance to length and cross-section"],
  ["Temperature coefficient","The fractional change in resistance per degree of temperature rise"]],
 "Series and parallel reduction handles resistive networks. The next chapter introduces the "
 "capacitor, an element whose current depends on the rate of change of voltage, and with it the "
 "idea of a circuit whose behaviour unfolds over time.",
)
