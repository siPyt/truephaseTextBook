# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH20=mkch(20,"Diagnosis, design review and the habits that last",
 "A single ordered method for finding a fault, and a checklist for reviewing work before it is energised",
 "The previous nineteen chapters supplied models, equations and instruments. This one supplies "
 "method. A competent electrical worker is not distinguished by knowing more formulae but by "
 "following an order of operations that converges on the answer instead of wandering towards it.",
 ["Apply a structured diagnostic sequence rather than replacing parts speculatively.",
  "Divide a circuit at a measurable boundary to halve the search space at each step.",
  "Choose the measurement that distinguishes between competing hypotheses.",
  "Distinguish an open circuit, a short circuit, a high-resistance joint and a wrong value by measurement.",
  "Review a completed design against supply, loading, protection, and safety criteria.",
  "Record a fault and its resolution so that the next person benefits.",
  "Identify which code edition applies and verify a requirement at its source."],
 ("c20_tshoot","The diagnostic sequence. Each measurement is chosen to divide the remaining "
  "possibilities roughly in half rather than to confirm a guess.",46),
 [dict(h2="Why speculative replacement fails",
   paras=["The commonest diagnostic error is to form a hypothesis from the symptom alone and "
    "then replace the suspected component. Sometimes this works, which is precisely why the "
    "habit survives. When it fails it costs the price of the part, the time to fit it, and the "
    "loss of information, because the original fault condition has now been disturbed.",
    "A structured sequence costs a few minutes of measurement and returns a definite answer. It "
    "also leaves a record: the measurements themselves tell the next person what was ruled out. "
    "The sequence below is not specific to any one kind of circuit, which is what makes it "
    "worth learning once."],
   numbered=["Establish the symptom precisely. What does the circuit do, and under what "
    "conditions? A fault that appears only when warm or only under load is a different problem "
    "from one that is always present.",
    "Confirm the supply. Measure the voltage at the point of use, not at the source, and measure "
    "it under load. More apparent faults are supply faults than any other single cause.",
    "Establish what the circuit should do. Write the expected voltage or current at two or three "
    "accessible points from the circuit model before measuring anything.",
    "Divide the circuit at an accessible boundary and measure there. The result eliminates one "
    "half of the remaining circuit.",
    "Repeat the division within the half that failed, until the fault is localised to a single "
    "component or connection.",
    "Identify the mechanism, not just the component. A resistor that has failed open was "
    "probably overloaded by something else.",
    "Correct the cause, then retest under the original conditions that produced the symptom.",
    "Record the symptom, the decisive measurement, the cause and the correction."]),
  dict(h2="Dividing the circuit: the halving principle",
   paras=["A chain of ten elements with one fault requires ten tests if each is checked in turn, "
    "but only four if the chain is halved each time. The principle is the same one used in "
    "searching a sorted list, and it applies to any series arrangement: a supply chain, a "
    "control circuit, a signal path through several stages.",
    "The requirement is an accessible boundary and a known expected value at that boundary. A "
    "terminal block, a connector, a test point or the input of an identifiable stage will all "
    "serve. Where the circuit is not a simple chain, divide it functionally instead: supply, "
    "input conditioning, processing, output stage, load."],
   eq=["tests in sequence " + AP + " n",
       "tests by halving " + AP + " log\u2082 n",
       "n = 64:  64 tests versus 6"],
   bullets=["Measure voltage with the circuit live and the load connected; it reveals what the circuit is actually doing.",
    "Measure resistance only with the circuit isolated and discharged; it reveals what the circuit is made of.",
    "Measure current when you need to know whether a path is carrying what it should.",
    "Compare against a written expected value, never against a vague impression of normality.",
    "Record each measurement as you take it; a diagnosis reconstructed from memory is unreliable."],
   bh="Choosing the quantity to measure"),
  dict(h2="The four basic fault conditions",
   paras=["Almost every electrical fault reduces to one of four conditions, and each has a "
    "measurement that identifies it unambiguously. Learning these four and their signatures "
    "removes most of the guesswork from the final stage of a diagnosis.",
    "An open circuit carries no current and shows the full supply voltage across the break. A "
    "short circuit carries excessive current and shows almost no voltage across the shorted "
    "part. A high-resistance joint is the most troublesome: it passes some current, develops a "
    "voltage drop proportional to that current, and therefore appears and disappears with load. "
    "A wrong value gives a circuit that works but not correctly, and is found by comparing "
    "measured values against calculated ones."],
   fig=("c20_design","The four fault conditions on one circuit. Each has a distinct voltage and "
    "current signature that identifies it without removing components.",46),
   table=(["Condition","Current","Voltage signature","Decisive test"],
    [["Open circuit","Zero in that branch","Full supply across the break","Voltage across the suspected break, live"],
     ["Short circuit","Excessive, device operates","Near zero across the shorted section","Resistance with the circuit isolated"],
     ["High-resistance joint","Reduced, falls under load","Drop across the joint, rises with current","Voltage across the joint while on load"],
     ["Wrong value fitted","Wrong but steady","Wrong but consistent with the fitted value","Compare measured value with calculated"],
     ["Intermittent","Varies with time or temperature","Changes when disturbed","Monitor while flexing, warming or loading"]],
    None)),
  dict(h2="Reviewing a design before it is energised",
   paras=["The same discipline applies before the circuit is built. A design review is a short, "
    "ordered set of questions whose purpose is to find the error that would otherwise be found "
    "by the protective device. The questions are the ones a competent assessor would ask.",
    "The order matters. Supply before load, load before conductor, conductor before protection, "
    "protection before enclosure, and safety considerations throughout rather than appended at "
    "the end. An error in the supply assumption invalidates everything downstream of it."],
   numbered=["Supply: what voltage, what frequency, what phase arrangement, and what is the "
    "available fault current at the point of connection?",
    "Load: what is the full-load current, what is the starting or inrush current, what is the "
    "duty cycle, and is the load inductive, capacitive or resistive?",
    "Conductor: is the cross-sectional area adequate for the current after all derating, and is "
    "the voltage drop at full load within the permitted limit over the actual route length?",
    "Protection: does the device carry the normal load without operating, and does it clear a "
    "fault at the furthest point within the required time?",
    "Isolation: can the circuit be isolated, locked off and proved dead by one person at one place?",
    "Earthing: is the protective conductor continuous, correctly sized and terminated throughout?",
    "Environment: temperature, moisture, dust, vibration, and mechanical damage risk along the route.",
    "Documentation: is the circuit recorded so that someone unfamiliar with it can work on it safely?"],
   panel=("Questions that catch the most errors",
    ["Was the voltage drop computed over the real route length, not the straight-line distance?",
     "Does the protective device characteristic actually clear a fault at the far end of the run?",
     "Were derating factors applied for grouping, ambient temperature and insulation together?",
     "Does the starting current pass without nuisance operation of the protective device?",
     "Is every protective conductor sized against the fault current it may have to carry?"])),
  dict(h2="Codes, editions and verifying at the source",
   paras=["Technical requirements are set by codes that are revised on a cycle, and a "
    "requirement remembered from an earlier edition may no longer be current. The habit worth "
    "forming is to identify which edition applies to the work in hand, then verify the specific "
    "requirement in that edition rather than relying on recollection.",
    "The principles developed in this book do not change with an edition. Ohm's law, the "
    "conservation laws, the behaviour of reactive elements and the physiological effect of "
    "current are stable. What changes is the particular numerical limit, the required "
    "disconnection time, the permitted method. Keep the principles in your head and look the "
    "numbers up.",
    "Where this book states a numerical limit, treat it as illustrative of the method rather "
    "than as the authority. The authority is the edition of the code in force in the "
    "jurisdiction where the work is carried out."],
   bullets=["Identify the code and edition that applies before quoting any numerical requirement.",
    "Verify the clause in that edition rather than reproducing it from memory or from a course note.",
    "Record which edition a design was assessed against, so later reviewers know the basis.",
    "Expect limits, disconnection times and permitted methods to change between editions.",
    "Expect the underlying physics and the diagnostic method not to change at all."],
   bh="Working with a code you do not have memorised"),
 ],
 [ex("Locating a fault by halving a chain",
   "A lighting circuit has eight luminaires in a chain through seven accessible junction boxes. "
   "Nothing operates, and the supply measures 230 V at the distribution board.",
   "The number of measurements needed to find a single open circuit, and the sequence.",
   [("Measure at the middle box, box 4","230 V present: fault is downstream"),
    ("Measure at box 6","0 V present: fault is between boxes 4 and 6"),
    ("Measure at box 5","230 V present: fault is between boxes 5 and 6"),
    ("Inspect that section","Open conductor or loose terminal located"),
    ("Total measurements","3 rather than 7")],
   "Three measurements replaced seven. The saving grows with the length of the chain, and the "
   "method needs no assumption about which component is most likely to fail."),
  ex("Identifying a high-resistance joint",
   "A 12 V, 2 A lamp circuit gives a dim lamp. The supply measures 12.0 V at no load and 9.4 V "
   "at the lamp terminals with the lamp connected.",
   "The nature of the fault and the resistance of the offending joint.",
   [("Voltage lost in the circuit","12.0 - 9.4 = 2.6 V"),
    ("Current actually flowing","Measured as 1.6 A, reduced by the added resistance"),
    ("Resistance causing the loss","R = 2.6 / 1.6 = 1.63 " + OH),
    ("Why resistance testing missed it","1.63 " + OH + " is hard to see in series with the lamp cold resistance"),
    ("Confirmation","Voltage measured directly across each joint while on load")],
   "The decisive test is a voltage measurement across each joint while current flows. A "
   "resistance test with the circuit dead would not have found this reliably."),
  ex("Design review of a motor supply",
   "A 400 V three-phase motor draws 18 A at full load with a starting current of six times "
   "full load. The run is 70 m. The permitted voltage drop is 5 per cent.",
   "The review findings in order.",
   [("Supply check","400 V three-phase confirmed at the point of connection"),
    ("Full-load current","18 A continuous, 108 A for a few seconds at start"),
    ("Permitted voltage drop","5 per cent of 400 V = 20 V"),
    ("Conductor check","Area selected so that drop over 70 m at 18 A stays under 20 V"),
    ("Protection check","Device must pass 108 A briefly yet clear a far-end fault in time")],
   "The starting current governs the choice of protective device while the full-load current and "
   "route length govern the conductor. Reviewing them in order prevents the common error of "
   "sizing the conductor for the starting current or the device for the running current."),
 ],
 lab("a structured fault-finding exercise on a prepared board",
  "Diagnose three faults introduced into a prepared low-voltage board using the halving method, "
  "recording the measurement sequence and identifying the fault condition in each case.",
  ["Prepared fault board with switchable faults, 12 V direct supply.",
   "Regulated direct-voltage supply, 12 V, current limited.",
   "Digital multimeter with test leads in good condition.",
   "Circuit diagram of the board with expected voltages marked.",
   "Record sheet for the measurement sequence."],
  ["Study the diagram and write the expected voltage at every accessible test point before any measurement.",
   "Energise the board with no fault set and verify your expected values. Resolve any disagreement now.",
   "Have a partner set fault one without telling you which it is.",
   "Record the symptom precisely before measuring anything.",
   "Confirm the supply voltage at the board under load.",
   "Choose a mid-circuit test point, predict the reading, then measure it and record both.",
   "Continue halving, recording prediction and measurement at each step, until the fault is localised.",
   "State the fault condition: open, short, high resistance or wrong value, and the evidence for it.",
   "Repeat the whole sequence for faults two and three.",
   "Count your measurements for each fault and compare with the number a sequential search would need."],
  ("c20_review","The prepared fault board. Test points divide the circuit into sections that can "
   "each be eliminated by a single measurement.",46),
  ["Fault","Symptom","Measurements used","Condition identified","Decisive reading"],
  [["1","","","",""],["2","","","",""],["3","","","",""],
   ["","","","",""],["","","","",""],["","","","",""]],
  ["For which fault did the halving method save the most measurements, and why?",
   "Which fault condition was hardest to identify by measurement, and what made it difficult?",
   "Did any prediction disagree with a measurement on the healthy board? What did that reveal?",
   "How would your sequence change if the board were a parallel rather than a series arrangement?",
   "Which single measurement in each sequence was genuinely decisive?",
   "Write the fault record for one fault as you would leave it for the next person."],
  ["Keep the exercise at 12 V; the method is identical at any voltage and the risk is not.",
   "Current-limit the supply so that a set short circuit cannot overheat the board.",
   "Inspect test leads for damaged insulation before starting.",
   "Isolate and discharge before any resistance measurement."]),
 [["Nothing operates at all","Supply, main protective device, or a common open circuit","Measure voltage at the point of use under load","Restore supply, then find why the device operated"],
  ["Works unloaded, fails under load","High-resistance joint or undersized conductor","Voltage across each joint and along the run while loaded","Remake the joint, or recalculate the conductor size"],
  ["Protective device operates immediately on energising","Short circuit or wrong connection","Resistance between conductors with the circuit isolated","Find and clear the short before re-energising"],
  ["Protective device operates after several minutes","Overload rather than a fault","Measure the actual load current and compare with the rating","Reduce the load or correct the device and conductor sizing"],
  ["Correct voltage but wrong behaviour","Wrong component value fitted","Compare every measured value against the calculated value","Fit the correct value and recheck the whole stage"],
  ["Fault appears only when warm","Thermal effect on a marginal joint or component","Monitor the suspect point while warming it gently","Remake the joint or replace the marginal component"],
  ["Fault clears when the enclosure is disturbed","Mechanical: loose terminal or fractured conductor","Monitor voltage while gently flexing each section","Remake the termination, support the cable properly"],
  ["Intermittent with no pattern","Vibration, moisture ingress, or a cracked joint","Monitor over time while varying one condition","Address the environmental cause, not just the symptom"]],
 ("c20_tshoot","The complete method, from symptom to record. The final step is the one most often "
  "omitted and the one that saves the most time later.",46),
 ["Write the expected value before taking the measurement; otherwise any reading looks plausible.",
  "Confirm the supply at the point of use and under load before suspecting anything downstream.",
  "Divide the circuit to halve the search space; do not test components in the order you remember them.",
  "Measure voltage live and under load, resistance only when isolated and discharged.",
  "Find the mechanism, not only the failed component, or the same fault will return.",
  "Retest under the conditions that produced the original symptom, not under easier ones.",
  "Record the symptom, the decisive measurement, the cause and the correction.",
  "Verify any numerical requirement in the edition of the code that applies to the work."],
 ["List the eight steps of the diagnostic sequence in order, and justify the position of each.",
  "Explain why speculative component replacement sometimes works and why it is still poor practice.",
  "A chain has 32 accessible test points and one open circuit. How many measurements does halving need?",
  "State the voltage and current signature of an open circuit, and the test that confirms it.",
  "State the voltage and current signature of a high-resistance joint, and why load is needed to find it.",
  "Why must resistance measurements be made only on an isolated and discharged circuit?",
  "A 24 V, 3 A circuit loses 4.2 V somewhere in the supply path at 2.4 A. Find the offending resistance.",
  "List the design review questions in order and explain why supply must precede load.",
  "Explain why starting current governs the protective device while route length governs the conductor.",
  "A circuit works but a measured voltage disagrees with calculation by thirty per cent. How do you proceed?",
  "Describe how you would diagnose a fault that appears only after twenty minutes of operation.",
  "Write a fault record for a loose neutral terminal found in a lighting circuit.",
  "Explain why a requirement remembered from an earlier code edition should not be relied upon.",
  "Name three things this book has taught that will not change with a code revision.",
  "Choose any chapter and state how its content would appear in a diagnostic sequence."],
 [["3","Five measurements","Log to base two of 32 is 5."],
  ["4","No current, full supply voltage across the break","The break carries the whole source voltage because no current flows elsewhere."],
  ["7","1.75 " + OH,"Resistance equals voltage lost divided by current, 4.2 divided by 2.4."],
  ["9","Starting current is brief but large, running current is continuous","The device must tolerate the brief peak; the conductor must carry the continuous current with acceptable drop."],
  ["13","Limits and methods change between editions","Only the edition in force in that jurisdiction is authoritative."]],
 ["A structured diagnostic sequence converges on a fault; speculative replacement does not.",
  "Confirming the supply at the point of use and under load eliminates the commonest cause first.",
  "Halving the circuit at an accessible boundary reduces the number of tests from n to about log base two of n.",
  "Four conditions cover almost every fault: open, short, high resistance and wrong value.",
  "A high-resistance joint is found by measuring voltage across it while current flows, not by resistance testing.",
  "A design review asks supply, load, conductor, protection, isolation, earthing, environment and documentation, in that order.",
  "Codes change by edition; principles do not. Keep the method in your head and verify the numbers at source.",
  "Recording a fault and its resolution is part of the repair, not an optional addition."],
 [["Sequential search","tests " + AP + " n","Testing elements one at a time along a chain"],
  ["Halving search","tests " + AP + " log\u2082 n","Dividing at an accessible boundary each time"],
  ["Joint resistance from loss","R = V_lost / I","Voltage measured across a joint while on load"],
  ["Permitted voltage drop","V_drop = percentage " + TIMES + " V_supply","Checking conductor adequacy over the route"],
  ["Power lost in a joint","P = I\u00b2 R","Assessing whether a joint will overheat"],
  ["Starting current","I_start = k " + TIMES + " I_FL","Sizing protection for motor and transformer loads"]],
 [["Symptom","The precisely stated observable behaviour of the faulty circuit"],
  ["Halving","Dividing the search space in two with each measurement"],
  ["Decisive test","The measurement that distinguishes between competing causes"],
  ["Open circuit","A break carrying no current, with full voltage across it"],
  ["Short circuit","An unintended low-resistance path carrying excessive current"],
  ["High-resistance joint","A connection passing current but developing a voltage drop"],
  ["Design review","An ordered set of checks applied before energising"],
  ["Derating","Reducing a conductor's permitted current for its installed conditions"],
  ["Fault record","The written symptom, measurement, cause and correction"]],
 "That completes the twenty chapters. The reference section that follows collects the equations, "
 "units, symbols, checklists and glossary in one place, so that the method in this chapter can be "
 "applied without turning back through the book.")
