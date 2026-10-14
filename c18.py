# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH18=mkch(18,"Safety, fault paths and protection",
 "How electricity injures, how faults clear, and the discipline of safe isolation",
 "Everything in the previous chapters describes how circuits behave when they are working. This "
 "chapter concerns what happens when they are not, and what keeps the person working on them "
 "alive. The physics is the same; only the consequences of a mistake have changed.",
 ["Describe how electric current injures the body and why current, not voltage, is the hazard.",
  "Trace the fault-current path from source to earth and identify what limits it.",
  "Explain how an overcurrent device achieves disconnection within the required time.",
  "Describe residual current protection and what it does and does not detect.",
  "Carry out safe isolation in the correct sequence and justify each step.",
  "Recognise arc-flash hazard and describe the precautions that reduce it.",
  "Explain the role of national wiring codes and the need to identify the edition in force."],
 ("c18_fault","An earth fault path. Current returns to the source through the protective "
  "conductor, and the total impedance of that loop determines whether the device will operate.",46),
 [dict(h2="How current injures",
   paras=["It is current through the body, not voltage across it, that causes injury. The body's "
    "impedance varies enormously with skin condition, contact area and contact pressure, which is "
    "why the same voltage can be harmless in one circumstance and lethal in another. Dry, "
    "calloused skin may present tens of thousands of ohms, while wet skin or a break in it may "
    "present only a few hundred.",
    "Effects progress with current magnitude and with duration. A current of around one "
    "milliampere is perceptible; around ten milliamperes the muscles may contract so that the "
    "victim cannot let go; and in the region of tens of milliamperes through the chest, "
    "ventricular fibrillation becomes possible. Both the magnitude and the time matter, which is "
    "why protective devices are specified by disconnection time as well as by current."],
   table=(["Approximate current","Typical effect","Relevance to protection"],
     [["1 mA","Perception threshold","Below the level of concern for injury"],
      ["5 to 10 mA","Painful shock, muscular reaction","Startle reaction causes secondary injury"],
      ["10 to 20 mA","Muscular contraction, cannot let go","Duration now becomes the critical "
       "factor"],
      ["30 mA","Residual current device operating level","Chosen to act before fibrillation "
       "becomes likely"],
      ["50 mA and above","Ventricular fibrillation possible","Disconnection must be within "
       "fractions of a second"],
      ["Several amperes","Severe burns, cardiac arrest","Overcurrent protection territory"]],None),
   panel=("Low voltage is not the same as safe voltage",
     ["Body impedance varies by two orders of magnitude with conditions.",
      "Wet hands, perspiration or broken skin drastically reduce it.",
      "A voltage harmless in dry conditions can be lethal in wet ones.",
      "Treat every circuit as dangerous until it has been proved dead."])),
  dict(h2="The fault path",
   paras=["An earth fault occurs when a live conductor contacts an exposed conductive part. "
    "Current then flows from the source, through the line conductor, across the fault, through "
    "the protective conductor and back to the source. The total impedance of that complete loop "
    "determines how much current flows, and therefore whether the protective device will operate "
    "and how quickly.",
    "This is why the continuity and the cross-section of the protective conductor matter so much. "
    "A high-resistance protective connection limits the fault current, which may leave it below "
    "the level that operates the device while still being far above the level that is lethal. The "
    "exposed part then stays live, which is the precise condition protective bonding exists to "
    "prevent."],
   eq=["I_fault = V / Z_loop",
       "Z_loop = source + line conductor + protective conductor",
       "Disconnection requires I_fault above the device's operating level"],
   fig=("c18_chain","The protective conductor path. Its continuity and cross-section determine "
     "the fault current and therefore whether disconnection occurs.",46)),
  dict(h2="Overcurrent protection",
   paras=["Overcurrent devices respond to current magnitude and duration together. A fuse or a "
    "circuit breaker will carry its rated current indefinitely, clear a modest overload after a "
    "deliberate delay, and clear a heavy fault almost instantly. That shape of response is the "
    "device's time-current characteristic, and selecting a device means matching that curve to "
    "the circuit.",
    "Two separate requirements must be satisfied. The device must protect the conductor against "
    "thermal damage under overload, and it must disconnect an earth fault quickly enough to limit "
    "shock duration. The first depends on the conductor's current-carrying capacity; the second "
    "depends on the fault loop impedance. A device can satisfy one and fail the other, which is "
    "why both are verified."],
   bh="What an overcurrent device must achieve",
   bullets=["Carry the design current of the circuit continuously without operating.",
     "Operate before the conductor's thermal limit is reached under overload.",
     "Disconnect an earth fault within the required time at the measured loop impedance.",
     "Interrupt the maximum prospective fault current without damage.",
     "Discriminate with upstream devices so that only the affected circuit is lost.",
     "Tolerate the legitimate inrush of the connected load."]),
  dict(h2="Residual current protection",
   paras=["A residual current device compares the current flowing out in the line conductor with "
    "that returning in the neutral. In a healthy circuit they are equal. If some current is "
    "leaving by another route, through a person or through damaged insulation to earth, the "
    "difference is detected and the device opens.",
    "It is important to understand what this does not cover. A residual current device cannot "
    "detect a fault between line and neutral, because that current still balances, so it provides "
    "no protection against an ordinary overload or a line-to-neutral short circuit. Nor does it "
    "protect someone who contacts line and neutral simultaneously. It supplements overcurrent "
    "protection; it does not replace it."],
   eq=["Detects:  I_line \u2260 I_neutral",
       "Typical personal protection rating: 30 mA",
       "Does not detect line-to-neutral faults"],
   panel=("Two devices for two different hazards",
     ["Overcurrent protection guards the conductor against thermal damage.",
      "Residual current protection guards a person against earth leakage.",
      "Neither substitutes for the other, and most circuits need both.",
      "A residual current device sees nothing wrong with a line-to-neutral short."])),
  dict(h2="Safe isolation",
   paras=["Safe isolation is a fixed sequence, not a set of preferences, and it is followed in "
    "order every time. Identify the correct circuit from the drawings and the labelling. Isolate "
    "it at an appropriate point. Secure the isolation with a lock and retain the key. Post a "
    "warning notice. Then prove the circuit dead using an approved voltage indicator that has "
    "itself been proved on a known source immediately before and immediately after the test.",
    "The proving step before and after the test is what catches a failed indicator, and it is the "
    "step most often skipped. An indicator that has failed since its last use will show dead on a "
    "live circuit, and without the proving unit there is nothing to reveal that. Testing all "
    "combinations of conductors, not only line to earth, catches the circuit that has been "
    "isolated at the wrong pole."],
   fig=("c18_lockout","Securing an isolation. The isolator is locked in the off position, the key "
     "is retained by the person working, and a warning notice is fitted.",46),
   bh="The safe isolation sequence",
   bullets=["Identify the circuit from the drawings and confirm the labelling.",
     "Isolate at a point that removes all sources of supply.",
     "Secure with a lock and retain the key personally.",
     "Post a warning notice at the point of isolation.",
     "Prove the voltage indicator on a known live source.",
     "Test the circuit: all live conductors to earth and to each other.",
     "Re-prove the indicator on the known source.",
     "Only then begin work."]),
  dict(h2="Arc flash and stored energy",
   paras=["Not every electrical injury is a shock. An arc fault converts fault energy into heat, "
    "light, pressure and molten metal, and the resulting burns can be severe at distances where "
    "no contact was ever made. The energy available depends on the prospective fault current and "
    "on how long the protective device takes to clear, so an arc close to a large supply is far "
    "more dangerous than the same event on a small final circuit.",
    "Stored energy deserves the same respect. Capacitors retain charge after isolation, inductive "
    "circuits produce a voltage when interrupted, and rotating machines generate while they coast "
    "down. Each must be discharged or allowed to stop, and then proved dead, before work begins.",
    "National wiring codes set the detailed requirements for disconnection times, conductor "
    "sizing, protective device selection, bonding and isolation. These requirements change "
    "between editions, so the edition in force for the installation must be established before "
    "any particular requirement is relied upon, and the relevant national code always takes "
    "precedence over any general guidance in a textbook."],
   bullets=["Capacitors and reservoir capacitors hold charge after isolation; discharge and prove.",
     "Inductive circuits produce a reverse voltage when interrupted.",
     "Rotating machines generate while coasting down.",
     "Uninterruptible supplies and standby generators are additional sources.",
     "Photovoltaic arrays remain live in daylight regardless of any isolator.",
     "Prove dead after all stored energy has been dealt with, not before."],
   bh="Sources of energy that remain after isolation"),
 ],
 [ex("Body current from a contact voltage",
   "A person contacts a faulty appliance at 230 V. Their body impedance is 1300 \u03a9 with dry "
   "hands and 600 \u03a9 with wet hands.",
   "The current in each case and the likely effect.",
   [("Dry hands","I = 230/1300 = 177 mA"),
    ("Wet hands","I = 230/600 = 383 mA"),
    ("Comparison with the fibrillation region","Both far exceed 50 mA"),
    ("Significance of duration","At these currents, disconnection time is critical"),
    ("Residual current device response","A 30 mA device operates well below either value")],
   "Both cases are potentially lethal, and the difference between them is only a matter of degree. "
   "This is why a residual current device is specified at 30 milliamperes rather than at any value "
   "related to body impedance."),
  ex("Fault current and disconnection",
   "A circuit has a measured earth fault loop impedance of 1.15 \u03a9 on a 230 V supply, protected "
   "by a device requiring 150 A to operate instantaneously.",
   "The prospective fault current and whether the device will operate instantaneously.",
   [("Fault current","I = 230/1.15 = 200 A"),
    ("Device requirement","150 A for instantaneous operation"),
    ("Comparison","200 A exceeds 150 A"),
    ("Conclusion","The device operates in its instantaneous region"),
    ("Margin","A 33 % margin above the requirement")],
   "The verification is a simple comparison, but it depends entirely on the measured loop "
   "impedance. A deteriorated protective conductor connection raising the impedance to 1.6 ohms "
   "would reduce the fault current to 144 amperes and the device would no longer operate "
   "instantaneously."),
  ex("Effect of a high-resistance protective conductor",
   "The circuit above develops a corroded protective conductor joint adding 2.0 \u03a9 to the loop.",
   "The new fault current, the device response, and the voltage on the exposed part.",
   [("New loop impedance","1.15 + 2.0 = 3.15 \u03a9"),
    ("New fault current","230/3.15 = 73 A"),
    ("Device response","Below 150 A, so no instantaneous operation"),
    ("Voltage on the exposed part","73 \u00d7 2.0 = 146 V"),
    ("Hazard","The exposed part sits at 146 V while the device may not operate")],
   "This is the precise failure that protective conductor testing exists to find. The fault "
   "current is far too small to clear the device quickly, yet the voltage on the accessible metal "
   "is lethal, and it may persist indefinitely."),
  ex("What a residual current device detects",
   "A circuit draws 9.2 A in the line conductor. In one case 9.2 A returns in the neutral; in "
   "another 9.16 A returns and 40 mA flows to earth.",
   "Whether a 30 mA device operates in each case.",
   [("First case, difference","9.2 \u2212 9.2 = 0 mA, no operation"),
    ("Second case, difference","9.2 \u2212 9.16 = 40 mA"),
    ("Comparison with the rating","40 mA exceeds 30 mA, so the device operates"),
    ("A line-to-neutral fault of 200 A","Currents still balance, so no operation"),
    ("Protection in that case","Provided only by the overcurrent device")],
   "The device responds only to an imbalance. A heavy line-to-neutral fault produces no imbalance "
   "at all, which is why the overcurrent device remains essential alongside it."),
  ex("Stored energy in a capacitor after isolation",
   "A 4700 \u00b5F capacitor in an isolated supply remains charged to 45 V.",
   "The stored energy, and the discharge resistor to bring it to a safe level in two seconds.",
   [("Stored energy","E = \u00bd C V\u00b2 = 0.5 \u00d7 0.0047 \u00d7 45\u00b2 = 4.76 J"),
    ("Hazard assessment","Enough to produce a severe startle and an arc at the terminals"),
    ("Time constant for a 2 s discharge","Allow about five time constants, so \u03c4 = 0.4 s"),
    ("Resistor value","R = \u03c4/C = 0.4/0.0047 = 85 \u03a9"),
    ("Resistor dissipation at the instant of connection","45\u00b2/85 = 24 W briefly")],
   "Nearly five joules is a real hazard at the terminals even though the voltage is modest. The "
   "resistor must be rated for the initial pulse, and the capacitor must still be proved dead "
   "after discharging.")],
 lab("fault loop measurement, protective conductor continuity, residual current testing and "
  "safe isolation",
  "Practise the safe isolation sequence until it is automatic, measure protective conductor "
  "continuity and earth fault loop impedance on a training rig, verify residual current device "
  "operating current and time, and demonstrate what a residual current device does not detect.",
  ["Training rig or test board with simulated final circuits, fed through an isolating "
   "transformer and a supply-side residual current device.",
   "Approved voltage indicator complying with the relevant national requirements, and its "
   "matching proving unit.",
   "Low-resistance ohmmeter for continuity testing.",
   "Earth fault loop impedance tester.",
   "Residual current device tester with ramp and timing functions.",
   "Lock-off devices for several isolator types, padlocks with unique keys, and warning notices.",
   "Insulation resistance tester.",
   "Introduced resistance, 2 \u03a9, to simulate a degraded protective conductor."],
  ["Before any measurement, identify the circuit to be worked on from the drawings and confirm it "
   "against the labelling at the distribution board.",
   "Isolate the circuit at the correct device, secure it with a padlock, retain the key, and fit "
   "a warning notice.",
   "Prove the voltage indicator on the proving unit and confirm it functions.",
   "Test the isolated circuit between every pair of live conductors and between each live "
   "conductor and earth. Record each result.",
   "Re-prove the indicator on the proving unit and record that it still functions.",
   "Have the sequence checked by the supervisor before proceeding, and repeat it until it is "
   "performed without prompting.",
   "With the circuit still isolated, measure the continuity of the protective conductor end to "
   "end with the low-resistance ohmmeter. Record the value.",
   "Measure the insulation resistance between live conductors and earth. Record the value.",
   "Restore the supply under supervision and measure the earth fault loop impedance at the "
   "furthest point of the circuit.",
   "Compute the prospective fault current from your measured impedance and compare it with the "
   "protective device's requirement for instantaneous operation.",
   "Isolate again following the full sequence, introduce the 2 \u03a9 resistance into the protective "
   "conductor path, and restore the supply.",
   "Re-measure the loop impedance and recompute the fault current. Compare with the device "
   "requirement and compute the voltage that would appear on the exposed part.",
   "Isolate, remove the introduced resistance, and restore.",
   "Test the residual current device with the ramp function and record the current at which it "
   "operates.",
   "Test it at its rated residual current and record the operating time.",
   "Test at five times the rated residual current and record the operating time.",
   "Operate the device's test button and confirm it trips.",
   "With supervision, demonstrate on the rig that a simulated line-to-neutral fault does not "
   "operate the residual current device, and identify which device does respond."],
  ("c18_lockout","The isolation point secured with a lock and a warning notice, with the key "
   "retained by the person carrying out the work.",46),
  ["Test","Measured value","Required value","Pass or fail","Comment"],
  [["Proving unit, before test","","","",""],["Live to live conductors","","","",""],
   ["Live conductors to earth","","","",""],["Proving unit, after test","","","",""],
   ["Protective conductor continuity","","","",""],["Insulation resistance","","","",""],
   ["Loop impedance, healthy","","","",""],["Loop impedance, 2 \u03a9 introduced","","","",""],
   ["Residual device operating current","","","",""],["Operating time at rated current","","","",""],
   ["Operating time at five times rated","","","",""],["Line-to-neutral fault simulation","","","",""]],
  ["Why is the voltage indicator proved both before and after the test, and what failure does the "
   "second proving catch?",
   "Why is it necessary to test between all pairs of live conductors rather than only from line "
   "to earth?",
   "What fault current did your healthy loop impedance imply, and did it satisfy the device's "
   "requirement for instantaneous operation?",
   "How did the introduced 2 \u03a9 change the fault current, and what voltage would have appeared "
   "on the exposed conductive part?",
   "Explain why that condition is more dangerous than a dead short to earth.",
   "At what current did the residual current device actually operate, and how does that compare "
   "with its rated residual current?",
   "How did the operating time at five times rated current compare with the time at rated "
   "current? Why is the device designed that way?",
   "Why did the simulated line-to-neutral fault not operate the residual current device, and "
   "which device protects against it?",
   "What does the device's own test button prove, and what does it not prove?",
   "List, in order and from memory, the full safe isolation sequence, and state the purpose of "
   "each step."],
  ["This exercise must be carried out only on a purpose-built training rig, under direct "
   "supervision, and never on a live installation.",
   "The full safe isolation sequence must be followed every time, in order, without abbreviation.",
   "Use only an approved voltage indicator with its matching proving unit. Do not use a "
   "multimeter as the primary means of proving dead.",
   "Retain the padlock key personally. Never allow another person to hold it or to use a "
   "duplicate.",
   "Treat every circuit as live until it has been proved dead by the correct method.",
   "Discharge capacitors and prove dead before touching any conductor.",
   "Restore supplies only under supervision, after confirming all persons are clear.",
   "Do not work alone on this exercise.",
   "Apply the national wiring code in force for your installation; the values used here are for "
   "training illustration only."]),
 [["Exposed metal is live but the protective device has not operated","High-resistance protective "
   "conductor limiting fault current below the operating level","Measure protective conductor "
   "continuity and earth fault loop impedance","Locate and repair the high-resistance joint, then "
   "re-verify the loop impedance"],
  ["Residual current device trips without apparent cause","Accumulated standing leakage from "
   "several items of equipment, or a genuine deteriorating insulation fault","Measure standing "
   "leakage with the circuit loaded; test insulation resistance","Divide the circuit between "
   "devices, or locate and repair the failing insulation"],
  ["Residual current device did not operate on a line-to-neutral short circuit","It detects "
   "imbalance only, and such a fault remains balanced","Confirm which device operated","None "
   "required: the overcurrent device is the correct protection for that fault"],
  ["Voltage indicator showed dead on a circuit that was live","Indicator failed since its last "
   "use and was not proved before the test","Prove the indicator on a proving unit","Replace the "
   "indicator and prove it before and after every test, without exception"],
  ["Circuit still live after isolating the device labelled for it","Incorrect labelling, or a "
   "second source of supply such as a standby supply","Test all conductors and trace the circuit "
   "back to every possible source","Correct the labelling and isolate every source before working"],
  ["Protective device trips as soon as the load is reconnected","Insulation failure in the load, "
   "or a conductor damaged during the work","Insulation resistance test on the load and the final "
   "circuit separately","Repair or replace the faulty item and retest before re-energising"],
  ["Severe burns from an incident where no contact was made","Arc flash, with energy set by "
   "prospective fault current and clearing time","Assess the prospective fault current and the "
   "device clearing time at that point","Apply appropriate arc-rated protection and reduce "
   "clearing time where practicable"],
  ["Shock received from equipment that had been isolated for some time","Stored charge in "
   "capacitors, or a second live source","Discharge capacitors through a resistor and re-prove "
   "dead","Discharge all stored energy as part of the isolation procedure and prove dead again"]],
 ("c18_fault","Verifying the fault path. Protective conductor continuity and loop impedance "
  "together confirm that a fault will be disconnected in the required time.",46),
 ["Follow the safe isolation sequence in full, in order, every single time, regardless of how "
  "familiar the circuit is.",
  "Prove the voltage indicator before and after the test; this one step catches the failure that "
  "kills.",
  "Test all conductor combinations, not only line to earth.",
  "Treat a high-resistance protective conductor as an urgent fault, because it leaves metal live "
  "without operating the device.",
  "Discharge stored energy and re-prove dead before touching any conductor.",
  "Identify every source of supply, including standby supplies and photovoltaic arrays, before "
  "isolating.",
  "Establish which edition of the applicable national code governs the installation before "
  "relying on any specific requirement."],
 ["State whether current or voltage is the direct cause of electric shock injury, and explain why.",
  "State approximately the current at which a person may be unable to release their grip.",
  "Explain why body impedance varies so widely and give two conditions that reduce it.",
  "List, in order, the components of an earth fault current loop.",
  "A circuit has a loop impedance of 0.92 \u03a9 on a 230 V supply. Find the prospective fault "
  "current.",
  "The device above requires 200 A for instantaneous operation. State whether it is satisfied.",
  "A corroded joint adds 1.5 \u03a9 to that loop. Find the new fault current and the voltage on the "
  "exposed part.",
  "State the two separate requirements an overcurrent device must satisfy.",
  "Explain the principle by which a residual current device detects a fault.",
  "State one type of fault a residual current device cannot detect, and explain why.",
  "State the typical rated residual current chosen for personal protection.",
  "List the safe isolation sequence in order.",
  "Explain why the voltage indicator is proved both before and after the test.",
  "Explain why testing only line to earth is insufficient when proving a circuit dead.",
  "State what determines the severity of an arc flash incident.",
  "Name three sources of energy that may remain in equipment after it has been isolated.",
  "Explain why the edition of a national wiring code must be established before relying on a "
  "specific requirement."],
 [["1","Current, because it is what passes through tissue","Voltage only determines the current "
   "that flows for a given body impedance"],
  ["2","About 10 to 20 mA","Muscular contraction prevents release at this level"],
  ["3","Skin condition, contact area and pressure vary; moisture and broken skin reduce it",
   "Impedance can fall by two orders of magnitude"],
  ["4","Source, line conductor, fault, protective conductor, back to source","The total impedance "
   "of this loop sets the fault current"],
  ["5","250 A","I = V/Z_loop"],
  ["6","Yes, 250 A exceeds 200 A","The device operates in its instantaneous region"],
  ["7","95 A; about 143 V on the exposed part","Fault current falls below the operating level "
   "while the metal remains live"],
  ["8","Protect the conductor thermally; disconnect an earth fault in time","Both must be "
   "verified separately"],
  ["9","It compares line and neutral current","Any imbalance indicates current leaving by another "
   "route"],
  ["10","A line-to-neutral fault","That current still balances, so no imbalance is detected"],
  ["11","30 mA","Chosen to operate below the level at which fibrillation becomes likely"],
  ["12","Identify, isolate, secure, notice, prove indicator, test, re-prove indicator","Each step "
   "removes one way the isolation could be wrong"],
  ["13","To detect an indicator that has failed","A failed indicator reads dead on a live circuit"],
  ["14","The circuit may be isolated at the wrong pole","Line to neutral or neutral to earth may "
   "still be live"],
  ["15","Prospective fault current and the device clearing time","Together they determine the "
   "energy released"],
  ["16","Charged capacitors, inductive circuits, coasting machines","Standby supplies and "
   "photovoltaic arrays are also sources"],
  ["17","Requirements change between editions","A citation is meaningless without its edition, "
   "and the current edition governs the work"]],
 ["Current through the body causes injury, and body impedance varies so widely that no voltage "
  "can be assumed safe.",
  "Both magnitude and duration determine the severity of a shock, which is why devices are "
  "specified by disconnection time.",
  "Fault current is set by the impedance of the complete loop, so protective conductor continuity "
  "and cross-section are critical.",
  "A high-resistance protective conductor is especially dangerous because it leaves metal live "
  "without producing enough current to operate the device.",
  "Overcurrent devices protect conductors and clear faults; residual current devices detect earth "
  "leakage; neither replaces the other.",
  "Safe isolation is a fixed sequence, and proving the indicator before and after the test is the "
  "step that catches a failed instrument.",
  "Arc flash severity depends on prospective fault current and clearing time, and stored energy "
  "remains after isolation.",
  "National wiring codes govern the detailed requirements, and the edition in force must be "
  "identified."],
 [["Fault current","I = V / Z_loop","Earth fault loop"],
  ["Loop impedance","Z = source + line + protective conductor","Complete fault path"],
  ["Voltage on exposed part","V = I_fault \u00d7 R_protective","High-resistance protective conductor"],
  ["Residual detection","Operates when I_line \u2212 I_neutral exceeds the rating","Residual "
   "current device"],
  ["Stored capacitor energy","E = \u00bd C V\u00b2","Isolated but charged capacitor"],
  ["Discharge time constant","\u03c4 = R C","Discharge resistor fitted"]],
 [["Fault loop impedance","The total impedance of the path a fault current takes back to source"],
  ["Protective conductor","The conductor connecting exposed conductive parts for fault protection"],
  ["Disconnection time","The time within which a protective device must clear a fault"],
  ["Residual current","The difference between line and neutral current, indicating leakage"],
  ["Prospective fault current","The current that would flow at a given point in a fault"],
  ["Proving unit","A known source used to confirm a voltage indicator is working"],
  ["Arc flash","The thermal and pressure hazard produced by an arcing fault"],
  ["Discrimination","Coordination so that only the device nearest the fault operates"]],
 "Safety and fault clearance depend on measurement, and measurement depends on both the "
 "instruments and the judgement behind them. The next chapter turns to control, sensing and "
 "signal conversion: how a circuit measures the world, compares the result against what was "
 "wanted, and corrects the difference. The chapter after that closes the book with the "
 "diagnostic method that draws all of this together.",
)
