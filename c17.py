# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH17=mkch(17,"Three-phase systems",
 "Star and delta, line and phase quantities, and how power is measured",
 "Industrial power is generated, transmitted and consumed in three phases, because three-phase "
 "transmission carries more power for a given weight of conductor and because three-phase motors "
 "are self-starting and smooth-running. Nearly every mistake made with three-phase systems comes "
 "from confusing line quantities with phase quantities.",
 ["Describe a balanced three-phase supply and the 120-degree relationship between phases.",
  "Distinguish line and phase voltages and currents in star and delta connections.",
  "Apply the root-three relationships correctly in each connection.",
  "Compute three-phase power, apparent power and power factor.",
  "Explain the function of the neutral conductor and the effect of unbalance.",
  "Describe the two-wattmeter method and interpret its readings."],
 ("c17_star","A star-connected load. The three phase windings meet at a common star point, which "
  "may be brought out as a neutral conductor.",46),
 [dict(h2="The balanced three-phase supply",
   paras=["A three-phase supply consists of three alternating voltages of equal magnitude, "
    "separated in phase by 120 degrees. Taken together they sum to zero at every instant, which "
    "is the property that makes the whole system efficient: in a balanced system the return "
    "currents cancel and no neutral current flows at all.",
    "The order in which the three phases reach their maxima is the phase sequence, and it "
    "determines the direction in which a connected motor will rotate. Reversing any two "
    "conductors reverses the sequence, which is why phase sequence must be verified before "
    "connecting rotating machinery."],
   eq=["Three voltages, equal magnitude, 120\u00b0 apart",
       "Instantaneous sum of a balanced set = 0",
       "Phase sequence determines rotation direction"],
   panel=("The neutral carries only the unbalance",
     ["In a perfectly balanced star-connected load the neutral current is zero.",
      "The neutral exists to carry the difference when phases are unequally loaded.",
      "It also holds each phase voltage fixed relative to the star point.",
      "Losing the neutral on an unbalanced load lets phase voltages shift severely."])),
  dict(h2="Star connection",
   paras=["In a star connection, one end of each phase winding is joined at a common point. The "
    "voltage measured between any two line conductors is root three times the voltage across any "
    "one phase, because the two phase voltages involved are 120 degrees apart rather than in "
    "line. The current in each line conductor is the same as the current through the phase "
    "winding it feeds.",
    "This is the connection used for distribution to mixed loads, because the star point provides "
    "a neutral. A 400-volt line voltage gives 230 volts to neutral, so three-phase machines and "
    "single-phase loads can be served from the same supply."],
   eq=["V_L = \u221a3 V_ph      so V_ph = V_L / \u221a3",
       "I_L = I_ph",
       "Example: 400 V line gives 400/1.732 = 231 V to neutral"]),
  dict(h2="Delta connection",
   paras=["In a delta connection the three windings are joined end to end in a closed loop, with "
    "the line conductors taken from the three junctions. Here the relationship is reversed: each "
    "phase winding sees the full line voltage, while the line current is root three times the "
    "current in any one phase winding.",
    "Delta has no star point and therefore no neutral, so it suits balanced three-phase loads "
    "such as motors rather than mixed single-phase loads. The absence of a neutral also means a "
    "delta load is unaffected by the kind of voltage shift that a lost neutral produces in a "
    "star system."],
   eq=["V_ph = V_L",
       "I_L = \u221a3 I_ph      so I_ph = I_L / \u221a3",
       "No star point, so no neutral available"],
   table=(["Quantity","Star connection","Delta connection"],
     [["Phase voltage","V_L / \u221a3","Equal to V_L"],
      ["Line voltage","\u221a3 V_ph","Equal to V_ph"],
      ["Phase current","Equal to I_L","I_L / \u221a3"],
      ["Line current","Equal to I_ph","\u221a3 I_ph"],
      ["Neutral available","Yes, at the star point","No"],
      ["Typical use","Distribution to mixed loads","Balanced loads, motor windings"]],None),
   fig=("c17_delta","A delta-connected load. Each winding sees the full line voltage, and the "
     "line current divides between two windings at each junction.",46)),
  dict(h2="Three-phase power",
   paras=["Total power in a balanced three-phase system is three times the power in one phase, "
    "and when expressed in terms of line quantities this reduces to a single formula that holds "
    "for both star and delta. The root-three factor appears once, and the power factor is the "
    "cosine of the angle between the phase voltage and the phase current.",
    "The convenience of this is that total power can be found from line measurements alone, "
    "without opening the load to find out whether it is star or delta connected. The same formula "
    "applies either way, which is why it is worth memorising in the line-quantity form."],
   eq=["P = \u221a3 V_L I_L cos\u03c6      (watts, either connection)",
       "S = \u221a3 V_L I_L      (volt-amperes)",
       "Q = \u221a3 V_L I_L sin\u03c6      (reactive volt-amperes)",
       "Power factor = P / S"],
   after=["Note that a load reconnected from star to delta on the same supply draws three times "
    "the power, because each winding then sees root three times the voltage and the current rises "
    "by the same factor. This is exactly the relationship exploited by star-delta starting."]),
  dict(h2="Unbalance and the neutral",
   paras=["Real installations are rarely balanced, because single-phase loads are connected "
    "between each line and neutral and cannot be matched exactly. The neutral conductor then "
    "carries the resultant unbalance current, which in normal circumstances is modest.",
    "Two situations change that. A lost or high-resistance neutral on an unbalanced star load "
    "allows the star point to shift, so lightly loaded phases rise well above their nominal "
    "voltage while heavily loaded phases fall; equipment is damaged on both sides. And harmonic "
    "currents from electronic loads, particularly the third harmonic, add arithmetically in the "
    "neutral rather than cancelling, so the neutral can carry more current than any line "
    "conductor despite an apparently balanced installation."],
   eq=["Balanced load:  I_N = 0",
       "Unbalanced load:  I_N = phasor sum of the three line currents",
       "Triplen harmonics add in the neutral rather than cancelling"],
   panel=("A lost neutral is a destructive fault, not an inconvenience",
     ["With the neutral intact, each phase voltage is fixed at the nominal value.",
      "With it lost, the star point floats and divides the line voltage by load impedance.",
      "A lightly loaded phase can rise toward the line voltage and destroy its equipment.",
      "Suspect a lost neutral whenever several phases show simultaneous and opposite errors."])),
  dict(h2="Measuring three-phase power",
   paras=["A single wattmeter measures total power only in a balanced four-wire system, where one "
    "phase can be measured and the result multiplied by three. For a three-wire system, balanced "
    "or not, the two-wattmeter method gives the total power from two instruments connected "
    "between the three conductors.",
    "The two readings are added to obtain total power, and their ratio reveals the power factor. "
    "At unity power factor the readings are equal; as power factor falls one reading diminishes "
    "and at a power factor of 0.5 it reads zero. Below that, one wattmeter reads negative and "
    "its reading must be subtracted, which is the step most often got wrong."],
   eq=["P_total = P\u2081 + P\u2082",
       "tan\u03c6 = \u221a3 (P\u2081 \u2212 P\u2082)/(P\u2081 + P\u2082)",
       "Below 0.5 power factor, one reading is negative"],
   fig=("c17_meas3","Two-wattmeter measurement on a three-wire supply. The sum of the two "
     "readings is the total power regardless of balance.",46),
   bh="Interpreting two-wattmeter readings",
   bullets=["Equal readings: unity power factor.",
     "One reading zero: power factor of 0.5.",
     "One reading negative: power factor below 0.5, so subtract it.",
     "Both readings negative: check the connections, not the load.",
     "Sum is always the total power, whether the load is balanced or not."]),
 ],
 [ex("Star-connected load: phase and line quantities",
   "A balanced star-connected load of 25 \u03a9 per phase is supplied at 400 V line voltage.",
   "The phase voltage, the phase and line currents, and the total power.",
   [("Phase voltage","V_ph = 400/\u221a3 = 231 V"),
    ("Phase current","I_ph = 231/25 = 9.24 A"),
    ("Line current","I_L = I_ph = 9.24 A in star"),
    ("Total power, phase quantities","3 \u00d7 231 \u00d7 9.24 = 6.40 kW"),
    ("Total power, line quantities","\u221a3 \u00d7 400 \u00d7 9.24 \u00d7 1 = 6.40 kW \u2713")],
   "Both routes give the same answer, which is a useful check. With a purely resistive load the "
   "power factor is unity, so the real and apparent powers are equal."),
  ex("The same load reconnected in delta",
   "The 25 \u03a9 per phase load above is reconnected in delta on the same 400 V supply.",
   "The new phase and line currents and the total power, compared with the star case.",
   [("Phase voltage now","V_ph = V_L = 400 V"),
    ("Phase current","I_ph = 400/25 = 16 A"),
    ("Line current","I_L = \u221a3 \u00d7 16 = 27.7 A"),
    ("Total power","\u221a3 \u00d7 400 \u00d7 27.7 = 19.2 kW"),
    ("Ratio to the star case","19.2/6.40 = 3 exactly")],
   "Delta draws three times the power of star from the same supply. This is the basis of "
   "star-delta starting: starting in star applies a reduced voltage to each winding and draws a "
   "third of the current and develops a third of the torque."),
  ex("Three-phase motor current from its rating",
   "A motor is rated 15 kW output at 400 V, with an efficiency of 0.91 and a power factor of 0.86.",
   "The input power, the apparent power and the line current.",
   [("Input power","P_in = 15 000/0.91 = 16 484 W"),
    ("Apparent power","S = 16 484/0.86 = 19 168 VA"),
    ("Line current","I_L = 19 168/(\u221a3 \u00d7 400) = 27.7 A"),
    ("Alternative route","I_L = 16 484/(\u221a3 \u00d7 400 \u00d7 0.86) = 27.7 A \u2713")],
   "Both efficiency and power factor must be applied: efficiency converts shaft output to "
   "electrical input, and power factor converts real power to the apparent power that determines "
   "the current."),
  ex("Two-wattmeter readings and power factor",
   "Two wattmeters on a three-wire supply read 7.2 kW and 2.4 kW.",
   "The total power and the power factor.",
   [("Total power","7.2 + 2.4 = 9.6 kW"),
    ("Difference","7.2 \u2212 2.4 = 4.8 kW"),
    ("Tangent of the angle","tan\u03c6 = \u221a3 \u00d7 4.8/9.6 = 0.866"),
    ("Phase angle","\u03c6 = 40.9\u00b0"),
    ("Power factor","cos 40.9\u00b0 = 0.756")],
   "The unequal readings indicate a lagging load. Had one reading been negative, it would have "
   "been subtracted in the total, and the power factor would have been below 0.5."),
  ex("Neutral current in an unbalanced installation",
   "Three single-phase loads draw 32 A, 26 A and 18 A from the three phases of a four-wire "
   "supply, at unity power factor.",
   "An estimate of the neutral current.",
   [("Resultant of a balanced portion","18 A in each phase cancels in the neutral"),
    ("Remaining unbalance","14 A and 8 A on two phases"),
    ("Phasor sum of the remainder","\u221a(14\u00b2 + 8\u00b2 \u2212 14\u00d78) = \u221a(196 + 64 \u2212 112)"),
    ("Neutral current","\u221a148 = 12.2 A"),
    ("Check against the simple difference","32 \u2212 18 = 14 A, so 12.2 A is plausible")],
   "The neutral carries only the unbalance, and because the remaining currents are 120 degrees "
   "apart they partly cancel. Note this calculation assumes no harmonic content; with electronic "
   "loads the neutral current could exceed any line current.")],
 lab("star and delta relationships, power measurement and the effect of a lost neutral",
  "Verify the root-three relationships in both connections, measure three-phase power by the "
  "two-wattmeter method, confirm the three-to-one power ratio between delta and star, and observe "
  "safely the voltage shift caused by an interrupted neutral on an unbalanced load.",
  ["Three-phase supply, reduced voltage, through an isolating transformer with a residual current "
   "device and lockable isolator.",
   "Three-phase resistive load bank with individually switchable phases and accessible star and "
   "delta links.",
   "Two wattmeters, or a three-phase power analyser.",
   "Three true rms voltmeters and three true rms ammeters, or a clamp meter.",
   "Phase rotation indicator.",
   "Low-voltage lamp loads of unequal rating for the unbalance test.",
   "Lock-off devices, voltage proving unit and insulated tools."],
  ["Prove the supply dead, lock off, and confirm the isolation before making any connection.",
   "Verify the phase sequence with the rotation indicator and record it.",
   "Connect the load bank in star with all three phases equal. Prove dead again before energising.",
   "Measure all three line voltages and all three phase voltages. Compute the ratio and compare "
   "with root three.",
   "Measure line and phase currents in one phase and confirm they are equal in star.",
   "Measure the neutral current with the load balanced and record it.",
   "Connect the two wattmeters and record both readings. Compute total power and power factor.",
   "Compute total power independently from your line voltage and current measurements and compare.",
   "Prove dead, lock off, and reconnect the same load bank in delta.",
   "Energise and measure line and phase voltages, confirming they are now equal.",
   "Measure line and phase currents and compute their ratio, comparing with root three.",
   "Record the total power in delta and compare it with the star figure. Confirm the ratio.",
   "Prove dead, lock off, and reconnect in star with deliberately unequal lamp loads on the three "
   "phases, with the neutral connected.",
   "Energise and record all three phase voltages and the neutral current.",
   "With the supply reduced to the lowest usable voltage, and under direct supervision, open the "
   "neutral link and immediately record the three phase voltages.",
   "Restore the neutral at once, then prove dead and lock off."],
  ("c17_star","The star-connected test arrangement, with the neutral link accessible and all "
   "three phase and line measurement points brought out.",46),
  ["Connection and condition","Line voltage (V)","Phase voltage (V)","Current (A)",
   "Power and comment"],
  [["Star, balanced","","","",""],["Star, phase current","","","",""],
   ["Star, neutral current","","","",""],["Delta, balanced","","","",""],
   ["Delta, phase current","","","",""],["Wattmeter 1 and 2 readings","","","",""],
   ["Star, unbalanced, neutral intact","","","",""],["Star, unbalanced, neutral open","","","",""]],
  ["What was the measured ratio of line to phase voltage in star? Compare it with root three and "
   "account for the difference.",
   "What was the measured ratio of line to phase current in delta? Compare with root three.",
   "Confirm from your measurements that line and phase currents are equal in star, and that line "
   "and phase voltages are equal in delta.",
   "What was the neutral current with the load balanced, and why was it not exactly zero?",
   "Compare the total power in delta with that in star. How close was the ratio to three, and why "
   "does that ratio arise?",
   "Compute the power factor from your two wattmeter readings and compare it with the value "
   "implied by your load.",
   "How did the three phase voltages behave when the neutral was opened on the unbalanced load? "
   "Which rose and which fell, and why?",
   "Explain in terms of the star point what happens when the neutral is lost.",
   "What would the consequence of that voltage shift be for equipment connected to the lightly "
   "loaded phase in a real installation?",
   "Why does the two-wattmeter method work regardless of whether the load is balanced?"],
  ["This work involves three-phase voltages. It must be carried out at the lowest practicable "
   "voltage, on a supply fed through an isolating transformer and a residual current device, and "
   "under direct supervision.",
   "Prove dead and lock off before every reconnection, and confirm isolation with a proving unit.",
   "Line voltage is root three times phase voltage. A circuit that seems safe phase to neutral is "
   "not safe line to line.",
   "The neutral-interruption test must be performed only at reduced voltage, momentarily, under "
   "supervision, and never on a live installation.",
   "Never open a neutral conductor on an energised unbalanced load in service; the resulting "
   "voltage shift destroys equipment and is dangerous.",
   "Confirm instrument ranges before connecting; three-phase currents and voltages exceed "
   "single-phase bench values.",
   "Use insulated tools and keep one hand clear when working near energised terminals.",
   "Load banks become hot. Allow them to cool before handling."]),
 [["One phase voltage high and another low at the same time","Lost or high-resistance neutral on "
   "an unbalanced star load","Measure all three phase voltages and the neutral-to-earth voltage",
   "Locate and repair the neutral connection; inspect all equipment on the high phase"],
  ["Motor rotates in the wrong direction after a supply alteration","Phase sequence reversed",
   "Check with a phase rotation indicator","Exchange any two line conductors, leaving the "
   "protective conductor undisturbed"],
  ["Motor runs hot and noisy and current is unequal between phases","Single phasing or supply "
   "voltage unbalance","Measure current in all three conductors and all three line voltages",
   "Restore the lost phase or correct the unbalance at source"],
  ["Neutral conductor hotter than the line conductors","Triplen harmonic currents adding in the "
   "neutral rather than cancelling","Measure neutral current with a true rms instrument and "
   "compare with the line currents","Increase the neutral cross-section or fit harmonic "
   "mitigation"],
  ["Load draws three times the expected current","Connected in delta where star was intended",
   "Inspect the terminal links against the nameplate and supply voltage","Reconnect to the "
   "correct configuration for the supply voltage"],
  ["Two-wattmeter total disagrees with a computed figure","One wattmeter reading negative and "
   "added instead of subtracted","Note the sign of each reading and recompute","Subtract the "
   "negative reading; verify the instrument connections"],
  ["Star-delta starter trips during the changeover","Open transition causing a current surge, or "
   "incorrect changeover timing","Record current through the changeover with a logging instrument",
   "Adjust the changeover timing or fit a closed-transition starter"],
  ["Single-phase loads on one phase cause flicker on another","Severe unbalance combined with a "
   "high-impedance neutral or supply","Measure phase voltages while the offending load switches",
   "Redistribute single-phase loads across the three phases and verify neutral integrity"]],
 ("c17_meas3","The two-wattmeter connection. Both readings are recorded with their signs, and "
  "their sum gives total power for any degree of unbalance.",46),
 ["State explicitly whether a quoted voltage or current is a line or a phase quantity; most "
  "three-phase errors begin here.",
  "Verify phase sequence before connecting any rotating machine.",
  "Treat a lost neutral as an urgent and destructive fault, and inspect equipment on the phases "
  "that rose.",
  "Measure neutral current with a true rms instrument on installations with electronic loads.",
  "Check terminal links against the nameplate and the supply voltage before energising a motor.",
  "Record the sign of each wattmeter reading, because a negative reading must be subtracted.",
  "Distribute single-phase loads across all three phases as evenly as the design allows."],
 ["State the phase displacement between the three voltages of a three-phase supply.",
  "A star-connected supply has a 415 V line voltage. Find the phase voltage.",
  "A delta-connected load draws 12 A per phase. Find the line current.",
  "State the relationship between line and phase current in a star connection.",
  "State the relationship between line and phase voltage in a delta connection.",
  "A balanced star load of 40 \u03a9 per phase is supplied at 400 V line. Find the line current.",
  "Find the total power of the load above.",
  "The same load is reconnected in delta on the same supply. Find the new total power.",
  "Explain why reconnecting from star to delta triples the power.",
  "Find the line current of a 400 V three-phase load drawing 22 kW at 0.88 power factor.",
  "State the neutral current of a perfectly balanced star-connected load and explain why.",
  "Explain what happens to the phase voltages when the neutral is lost on an unbalanced star load.",
  "Explain why the neutral of an installation with many electronic loads may carry more current "
  "than any line conductor.",
  "Two wattmeters read 9.0 kW and 3.6 kW. Find the total power and the power factor.",
  "Two wattmeters read 8.0 kW and \u22121.2 kW. Find the total power and state what the negative "
  "reading indicates.",
  "State why phase sequence must be verified before connecting a three-phase motor."],
 [["1","120 degrees","Three equal voltages equally spaced through the cycle"],
  ["2","240 V","V_ph = V_L/\u221a3"],
  ["3","20.8 A","I_L = \u221a3 I_ph"],
  ["4","They are equal","Each line conductor carries the current of the phase it feeds"],
  ["5","They are equal","Each winding is connected directly between two lines"],
  ["6","5.77 A","V_ph = 231 V, so I = 231/40"],
  ["7","4.0 kW","P = \u221a3 V_L I_L cos\u03c6 with unity power factor"],
  ["8","12.0 kW","Three times the star value"],
  ["9","Each winding sees \u221a3 times the voltage","Current also rises by \u221a3, so power rises "
   "by three"],
  ["10","36.1 A","I = P/(\u221a3 V_L cos\u03c6)"],
  ["11","Zero","The three equal currents are 120 degrees apart and sum to zero"],
  ["12","The star point shifts, so lightly loaded phases rise and loaded phases fall","Voltage "
   "divides according to load impedance instead of being fixed"],
  ["13","Triplen harmonics add rather than cancel","Third-harmonic currents are in phase in all "
   "three conductors, so they sum in the neutral"],
  ["14","12.6 kW; power factor 0.76","Sum gives power; tan\u03c6 = \u221a3(P\u2081\u2212P\u2082)/(P\u2081+P\u2082)"],
  ["15","6.8 kW; power factor below 0.5","The negative reading is subtracted and indicates a "
   "strongly reactive load"],
  ["16","It determines the direction of rotation","Connecting without checking may drive a pump "
   "or compressor backwards"]],
 ["A three-phase supply is three equal voltages 120 degrees apart, which sum to zero and so need "
  "no return current when balanced.",
  "In star, line voltage is root three times phase voltage and the currents are equal; in delta, "
  "the voltages are equal and line current is root three times phase current.",
  "Total power is root three times line voltage times line current times power factor, for either "
  "connection.",
  "Reconnecting a load from star to delta on the same supply triples its power, which is the "
  "basis of star-delta starting.",
  "The neutral carries only the unbalance, and losing it on an unbalanced star load shifts the "
  "phase voltages destructively.",
  "Triplen harmonics add in the neutral instead of cancelling, so neutral current can exceed line "
  "current.",
  "The two-wattmeter method gives total power for any three-wire load, with a negative reading "
  "subtracted and indicating a power factor below 0.5."],
 [["Star voltage relation","V_L = \u221a3 V_ph","Star connection"],
  ["Star current relation","I_L = I_ph","Star connection"],
  ["Delta voltage relation","V_ph = V_L","Delta connection"],
  ["Delta current relation","I_L = \u221a3 I_ph","Delta connection"],
  ["Three-phase power","P = \u221a3 V_L I_L cos\u03c6","Balanced load, either connection"],
  ["Three-phase apparent power","S = \u221a3 V_L I_L","Balanced load"],
  ["Two-wattmeter total","P = P\u2081 + P\u2082","Any three-wire load"],
  ["Power factor from wattmeters","tan\u03c6 = \u221a3(P\u2081\u2212P\u2082)/(P\u2081+P\u2082)","Two-wattmeter method"]],
 [["Phase voltage","The voltage across one winding or one phase of the load"],
  ["Line voltage","The voltage between any two line conductors"],
  ["Phase sequence","The order in which the three phases reach their maxima"],
  ["Star point","The common junction of three windings in a star connection"],
  ["Unbalance","Inequality between the three phase loads or voltages"],
  ["Triplen harmonics","Harmonics at multiples of three times the fundamental, which add in the "
   "neutral"],
  ["Two-wattmeter method","Measuring total three-wire power with two instruments"]],
 "Three-phase distribution brings substantial energy to the point of use, which makes the "
 "consequences of a fault correspondingly serious. The next chapter turns to safety, fault paths "
 "and the discipline of safe isolation.",
)
