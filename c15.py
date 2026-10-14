# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH15=mkch(15,"Digital logic",
 "Two-state signals, gates, and the circuits that remember",
 "Once a signal is reduced to two states, it can be combined by logical rules rather than by "
 "Ohm's law. Every control panel built in the last forty years uses this idea, whether in "
 "discrete gates, in a programmable controller, or in the interlocking of a motor starter.",
 ["State the truth tables of the basic gates and recognise their symbols.",
  "Convert between binary, decimal and hexadecimal.",
  "Build and simplify a combinational function from a specification.",
  "Explain how a latch stores a state and why a seal-in contact is the same idea.",
  "Describe flip-flop operation and clocked behaviour.",
  "Interpret a control interlock drawn as either a ladder or a logic diagram."],
 ("c15_gates","The basic logic gates. Each symbol's outline identifies its function, and a small "
  "circle on the output indicates inversion.",46),
 [dict(h2="Two states and number systems",
   paras=["A digital signal is interpreted as one of two states. Any voltage above a defined "
    "threshold reads as one state and any voltage below a lower threshold reads as the other, "
    "with a forbidden band between them. That tolerance is the reason digital signals survive "
    "noise and long cable runs so much better than analogue ones.",
    "Because there are two states per digit, counting is naturally binary. Hexadecimal is used as "
    "a shorthand, because one hexadecimal digit represents exactly four binary digits, which "
    "makes long binary values readable without arithmetic."],
   eq=["Each bit position carries 2\u207f:  ... 16, 8, 4, 2, 1",
       "One hexadecimal digit = four bits",
       "n bits represent 2\u207f distinct values"],
   table=(["Decimal","Binary","Hexadecimal","Decimal","Binary","Hexadecimal"],
     [["0","0000","0","8","1000","8"],
      ["1","0001","1","9","1001","9"],
      ["2","0010","2","10","1010","A"],
      ["3","0011","3","11","1011","B"],
      ["4","0100","4","12","1100","C"],
      ["5","0101","5","13","1101","D"],
      ["6","0110","6","14","1110","E"],
      ["7","0111","7","15","1111","F"]],None)),
  dict(h2="The basic gates",
   paras=["Five functions account for almost everything. An AND output is active only when all "
    "inputs are active. An OR output is active when any input is active. A NOT output is the "
    "inverse of its single input. NAND and NOR are the inverted forms of AND and OR, and the "
    "exclusive-OR output is active when its inputs differ.",
    "The small circle on a symbol's output always means inversion, so recognising NAND as an AND "
    "outline with an output circle is all that is needed to read it. NAND and NOR are "
    "particularly important because either one alone can construct any other function, which is "
    "why real integrated circuits are built predominantly from them."],
   table=(["A","B","AND","OR","NAND","NOR","XOR"],
     [["0","0","0","0","1","1","0"],
      ["0","1","0","1","1","0","1"],
      ["1","0","0","1","1","0","1"],
      ["1","1","1","1","0","0","0"]],None),
   bh="Reading a logic symbol",
   bullets=["Flat back with a curved front: AND.",
     "Curved back with a pointed front: OR.",
     "Triangle with an output circle: NOT, or inverter.",
     "A circle on any output means that output is inverted.",
     "A double curve on the input side of an OR outline: exclusive-OR.",
     "A triangle without a circle: buffer, which drives rather than inverts."]),
  dict(h2="Combining gates into a function",
   paras=["A control requirement stated in words translates directly into gates. The phrase "
    "\u2018run when the start button is pressed and no trip is active\u2019 is an AND of two "
    "conditions, one of them inverted. Building the function is a matter of writing the statement "
    "precisely enough that each condition becomes a single input.",
    "Two simplifications are worth knowing, because they appear constantly. An inverted AND is "
    "the same as an OR of inverted inputs, and an inverted OR is the same as an AND of inverted "
    "inputs. These let a function be rearranged into whichever form uses fewer gates or matches "
    "the available devices."],
   eq=["NOT(A AND B) = (NOT A) OR (NOT B)",
       "NOT(A OR B) = (NOT A) AND (NOT B)",
       "A AND A = A       A OR NOT A = 1"],
   panel=("Safety conditions are wired as normally closed, not as logic",
     ["A logic NOT depends on the device working and being powered.",
      "A physically normally closed emergency-stop contact opens on demand or on a broken wire.",
      "Safety functions must therefore be hard-wired, not merely programmed.",
      "Use logic to coordinate a process; use hard wiring to make it safe."])),
  dict(h2="Latches and the seal-in contact",
   paras=["A latch holds a state after the input that set it has gone away. Cross-coupling two "
    "NAND or two NOR gates so that each drives the other produces exactly this: a brief input "
    "sets the output, and it stays set until a separate input resets it.",
    "An electrician has already met this circuit. A motor starter in which the contactor's own "
    "auxiliary contact maintains the coil after the start button is released is a latch built "
    "from a relay. The start button sets it, the stop button resets it, and the seal-in contact "
    "is the feedback path. Recognising the two as the same circuit makes both easier to "
    "troubleshoot."],
   fig=("c15_interlock","A control interlock. The seal-in path maintains the coil after the start "
     "button is released, and the stop contact breaks that path."),
   bullets=["Start button: the set input, acting momentarily.",
     "Seal-in auxiliary contact: the feedback that maintains the state.",
     "Stop button: the reset input, wired normally closed.",
     "Overload contact: a second reset, also wired normally closed.",
     "Loss of supply resets the latch, which is why the motor does not restart by itself."],
   bh="The starter circuit as a latch"),
  dict(h2="Flip-flops and clocked logic",
   paras=["A flip-flop is a latch whose inputs are only examined at a defined instant, usually "
    "the edge of a clock signal. That discipline matters because it stops the circuit responding "
    "to transient conditions while signals are still settling, and it allows many stages to "
    "advance together in step.",
    "From clocked flip-flops come counters, shift registers and timing chains. A counter is a "
    "cascade in which each stage changes state when the previous one completes a cycle, which is "
    "how a digital timer measures intervals and how a frequency is divided down."],
   eq=["Edge triggered: inputs sampled at the clock transition",
       "A chain of n flip-flops divides frequency by 2\u207f",
       "Counter range with n stages: 0 to 2\u207f \u2212 1"],
   fig=("c15_ff","A flip-flop. Its stored state changes only at the clock edge, so the output "
     "ignores input activity between edges.",46)),
  dict(h2="Logic families and interfacing",
   paras=["Different logic families use different thresholds and different supply voltages, and "
    "they differ widely in how much current an output can source or sink. Mixing families without "
    "checking those figures is a common source of intermittent faults, because a signal may be "
    "within the forbidden band for the receiving device even though it looks correct on a meter.",
    "Interfacing logic to real loads needs an intervening stage. A logic output cannot drive a "
    "contactor coil directly, so a transistor or an optically coupled driver is used, and the "
    "coil receives its suppression diode. In the other direction, field inputs are conditioned "
    "and often optically isolated before they reach the logic."],
   table=(["Concern","What to check","Consequence if ignored"],
     [["Supply voltage","Both devices rated for the same rail","Device damage or no output"],
      ["Threshold levels","Output levels fall outside the receiver's forbidden band",
       "Intermittent and temperature-dependent faults"],
      ["Output drive current","Fan-out against the receiving inputs","Degraded levels and slow "
       "edges"],
      ["Unused inputs","Tied to a defined level, never left floating","Random switching and noise "
       "pickup"],
      ["Load driving","A transistor or coupler stage with suppression","Logic output destroyed by "
       "the coil"],
      ["Field inputs","Conditioning and isolation","Induced transients reaching the logic"]],None),
   panel=("Never leave a logic input floating",
     ["A floating input has no defined state and picks up noise capacitively.",
      "The device may switch randomly or oscillate at high frequency.",
      "Tie every unused input to the supply or to the reference through a resistor.",
      "This is among the most common causes of unrepeatable digital faults."])),
 ],
 [ex("Converting between number systems",
   "The value 1011 0110 in binary.",
   "Its decimal and hexadecimal equivalents.",
   [("Split into four-bit groups","1011  0110"),
    ("First group","1011 = 8 + 2 + 1 = 11, which is B"),
    ("Second group","0110 = 4 + 2 = 6"),
    ("Hexadecimal","B6"),
    ("Decimal","(11 \u00d7 16) + 6 = 182")],
   "Grouping into four bits makes the hexadecimal conversion immediate with no arithmetic. The "
   "decimal value then follows from the place values of the hexadecimal digits."),
  ex("Translating a control requirement into logic",
   "A pump must run when the level switch calls for it and the selector is in automatic, or "
   "whenever the manual button is pressed, but never when the trip is active.",
   "The logic expression and the gates required.",
   [("First condition","Level AND Automatic"),
    ("Second condition","OR Manual"),
    ("Trip condition","AND NOT Trip"),
    ("Complete expression","Run = ((Level AND Auto) OR Manual) AND NOT Trip"),
    ("Gates needed","One AND for the pair, one OR, one inverter, one final AND"),
    ("Hard-wiring note","The trip must also break the coil circuit physically")],
   "The expression follows the wording directly. Note the final condition is implemented twice: "
   "once in logic for orderly operation, and once in hard wiring so that it still works if the "
   "logic fails."),
  ex("Applying the inversion rules",
   "The expression NOT(A AND B AND C) is to be built, but only OR gates and inverters are "
   "available.",
   "An equivalent form.",
   [("Original","NOT(A AND B AND C)"),
    ("Apply the rule","= (NOT A) OR (NOT B) OR (NOT C)"),
    ("Gates needed","Three inverters and one three-input OR"),
    ("Verification, all inputs active","Original gives 0; new form gives 0 OR 0 OR 0 = 0 \u2713"),
    ("Verification, A inactive","Original gives 1; new form gives 1 OR 0 OR 0 = 1 \u2713")],
   "The two forms are identical in every case, which is what makes the substitution safe. "
   "Checking two rows, one where the result differs from the others, is a quick confidence test."),
  ex("Counter range and frequency division",
   "A chain of eight flip-flops is clocked at 32 768 Hz.",
   "The count range and the output frequency of the final stage.",
   [("Count range","0 to 2\u2078 \u2212 1, that is 0 to 255"),
    ("Division per stage","Each stage divides by two"),
    ("Total division","2\u2078 = 256"),
    ("Output frequency","32 768/256 = 128 Hz"),
    ("For a 1 Hz output","A division of 32 768 is needed, requiring fifteen stages")],
   "The relationship between stage count and division is why 32 768 Hz crystals are standard in "
   "timekeeping: fifteen divisions produce exactly one hertz."),
  ex("Driving a contactor from a logic output",
   "A logic output can source 20 mA at 5 V. A contactor coil draws 150 mA at 24 V.",
   "Why the output cannot drive the coil, and what is required.",
   [("Coil current required","150 mA"),
    ("Logic output capability","20 mA"),
    ("Voltage mismatch","Coil needs 24 V; logic provides 5 V"),
    ("Required interface","A transistor switch with a base resistor"),
    ("Base current needed","With a minimum gain of 50, I_B = 3 mA, driven to 12 mA"),
    ("Additional component","A suppression diode across the coil")],
   "Both the current and the voltage are wrong, so an interface stage is unavoidable. The "
   "suppression diode protects the transistor, and an optical coupler would be added if isolation "
   "between field and logic were required.")],
 lab("gate truth tables, a latch, and the starter circuit as logic",
  "Verify the truth table of each basic gate by measurement, confirm the inversion rules "
  "experimentally, build a cross-coupled latch and relate it to a motor starter seal-in circuit, "
  "then observe clocked flip-flop behaviour.",
  ["Logic integrated circuits: quad NAND, quad NOR, hex inverter, quad AND, quad OR, and a "
   "dual flip-flop.",
   "Breadboard, 5 V regulated supply, and 100 nF decoupling capacitors.",
   "Light-emitting diodes with 1.5 k\u03a9 series resistors for output indication.",
   "Switches or links with 10 k\u03a9 pull-down resistors for inputs.",
   "Two push buttons, one normally open and one normally closed.",
   "Relay with an auxiliary contact, 24 V coil, with a transistor driver and suppression diode.",
   "Signal generator for a slow clock, and a two-channel oscilloscope."],
  ["Fit a decoupling capacitor across the supply pins of every integrated circuit before applying "
   "power.",
   "Tie all unused inputs to a defined level through resistors and note why this is necessary.",
   "Wire the AND gate with switched inputs and an indicator output. Record the output for all "
   "four input combinations.",
   "Repeat for the OR, NAND, NOR and exclusive-OR gates, tabulating each full truth table.",
   "Build NOT(A AND B) using a NAND gate, and separately build (NOT A) OR (NOT B) using inverters "
   "and an OR gate.",
   "Drive both circuits from the same two switches and confirm their outputs agree for all four "
   "combinations.",
   "Cross-couple two NAND gates so that each output feeds the other's input, with the remaining "
   "input of each brought out as set and reset.",
   "Pulse the set input briefly and confirm the output stays set after the input is released.",
   "Pulse the reset input and confirm the output clears.",
   "Apply both inputs simultaneously and record what happens. Note why this condition is avoided.",
   "Build the relay starter: a normally open start button, a normally closed stop button, the coil "
   "through its transistor driver, and the auxiliary contact wired as a seal-in.",
   "Operate the start button momentarily and confirm the relay stays energised.",
   "Operate the stop button and confirm it drops out.",
   "Interrupt the supply briefly and confirm the relay does not re-energise by itself.",
   "Apply a slow clock to the flip-flop, change its input between clock edges, and observe on the "
   "oscilloscope when the output actually responds."],
  ("c15_interlock","The starter circuit built as a latch. The seal-in contact provides the "
   "feedback path that corresponds to the cross-coupling in the gate version.",46),
  ["Circuit","Input combination","Output","Matches prediction?","Observation"],
  [["AND gate","All four","","",""],["OR gate","All four","","",""],
   ["NAND gate","All four","","",""],["NOR gate","All four","","",""],
   ["Exclusive-OR","All four","","",""],["Inversion rule check","All four","","",""],
   ["Latch, set then release","","","",""],["Latch, reset","","","",""],
   ["Relay seal-in circuit","","","",""],["Flip-flop at clock edge","","","",""]],
  ["Did every measured truth table match the predicted one? Note any discrepancy and its cause.",
   "Did your two circuits for NOT(A AND B) agree in all four cases? What does that confirm?",
   "Explain in your own words how the cross-coupled latch retains its state after the set input "
   "is released.",
   "What happened when both latch inputs were applied together, and why is that condition "
   "designed out of real circuits?",
   "Identify which part of the relay starter corresponds to the set input, which to the reset, "
   "and which to the cross-coupling.",
   "Why did the relay not re-energise after the supply was restored? What safety purpose does "
   "that serve?",
   "When did the flip-flop output actually change relative to your input change, and what does "
   "that tell you about edge triggering?",
   "Deliberately leave one unused gate input floating and describe what the output does. Then tie "
   "it off again."],
  ["Confirm supply polarity and voltage before inserting any integrated circuit.",
   "Fit decoupling capacitors before applying power.",
   "Never connect a logic output directly to a relay coil; use the transistor driver and its "
   "suppression diode.",
   "Observe the polarity of every light-emitting diode and fit its series resistor.",
   "Remove power before inserting or removing an integrated circuit.",
   "Keep the relay coil circuit at low voltage and separate from any mains wiring on the bench."]),
 [["Logic output switches randomly with no input change","An unused input left floating and "
   "picking up noise","Check every input pin for a defined level","Tie all unused inputs to the "
   "supply or the reference through a resistor"],
  ["Circuit works intermittently and worse when warm","Output levels falling within the "
   "receiver's forbidden band, often from mixed families","Measure the actual output levels and "
   "compare with the receiving device's thresholds","Match the logic families or insert a proper "
   "level-translating buffer"],
  ["Logic output destroyed when it was connected to a coil","Coil current and voltage far beyond "
   "the output rating","Compare coil current with the output drive rating","Fit a transistor or "
   "optically coupled driver with a suppression diode"],
  ["Outputs glitch whenever a nearby contactor operates","Inadequate decoupling and induced "
   "transients on field wiring","Observe the supply rail on an oscilloscope during switching",
   "Fit decoupling at every device, and isolate and condition field inputs"],
  ["Latch sets itself at power-up","Both inputs momentarily active, or no defined reset at "
   "start-up","Observe the inputs during the power-up transition","Add a power-up reset and "
   "ensure the inputs cannot both be active"],
  ["Counter occasionally skips or doubles a count","Input contact bouncing, producing multiple "
   "edges from one operation","Observe the input on an oscilloscope while operating the contact",
   "Debounce the input with a filter or a latch stage"],
  ["Programmed interlock did not stop the machine on emergency stop","Safety function implemented "
   "in logic rather than hard wired","Trace the emergency-stop circuit through to the coil",
   "Hard wire the emergency-stop contacts in series with the coil, normally closed"],
  ["Flip-flop output changes at unexpected times","Input changing too close to the clock edge, so "
   "the sampled value is uncertain","Observe input and clock together on two channels",
   "Ensure the input is stable for the required interval around the clock edge"]],
 ("c15_ff","Observing clocked behaviour. The input is changed between clock edges and the output "
  "is seen to respond only at the edge itself.",46),
 ["Tie off every unused logic input; floating inputs cause the least repeatable faults you will "
  "ever chase.",
  "Hard wire every safety function and treat the programmed version as coordination only.",
  "Fit decoupling capacitors at each device as part of the build, not as a later remedy.",
  "Always interpose a driver and a suppression diode between logic and any coil.",
  "Check output levels against the receiving device's thresholds when mixing logic families."],
 ["State the truth table of a two-input NAND gate.",
  "Convert 1101 0011 to hexadecimal and to decimal.",
  "Convert decimal 205 to binary and to hexadecimal.",
  "State how many distinct values twelve bits can represent.",
  "State what a small circle on a gate output indicates.",
  "Write the equivalent of NOT(A OR B) using AND and inverters.",
  "Express in logic: a fan runs when the thermostat calls and the system is enabled, unless the "
  "door is open.",
  "Explain why an emergency stop must be hard wired rather than implemented in logic.",
  "Explain how a cross-coupled pair of gates retains its state.",
  "Identify the three parts of a motor starter circuit that correspond to set, reset and "
  "cross-coupling.",
  "Explain why a motor does not restart by itself after a supply interruption.",
  "A chain of ten flip-flops is clocked at 1.024 MHz. Find the final stage frequency.",
  "State the count range of a twelve-stage counter.",
  "Explain why an unused logic input must not be left floating.",
  "State two reasons a 5 V logic output cannot drive a 24 V contactor coil."],
 [["1","Output is 0 only when both inputs are 1","It is an AND with an inverted output"],
  ["2","D3; 211","1101 = D, 0011 = 3; decimal is 13\u00d716 + 3"],
  ["3","1100 1101; CD","128 + 64 + 8 + 4 + 1 = 205"],
  ["4","4096","2\u00b9\u00b2 distinct values"],
  ["5","That the output is inverted","It converts AND to NAND and OR to NOR"],
  ["6","(NOT A) AND (NOT B)","The inverted OR equals the AND of the inverted inputs"],
  ["7","Run = Thermostat AND Enable AND NOT Door","Each stated condition becomes one input"],
  ["8","It must work when the logic has failed or lost supply","A normally closed contact also "
   "opens on a broken wire, which logic does not"],
  ["9","Each output drives the other's input","The state is self-maintaining once established"],
  ["10","Start button, stop button, seal-in auxiliary contact","They are the set, reset and "
   "feedback path respectively"],
  ["11","Loss of supply resets the latch","The seal-in path is broken, so the coil needs a fresh "
   "start command"],
  ["12","1 kHz","1.024 MHz divided by 2\u00b9\u2070, that is 1024"],
  ["13","0 to 4095","2\u00b9\u00b2 \u2212 1"],
  ["14","It has no defined state and picks up noise","The device may switch randomly or oscillate"],
  ["15","Insufficient current and wrong voltage","The coil needs far more current than the output "
   "can source and a higher supply rail"]],
 ["A digital signal is interpreted against thresholds with a forbidden band between, which is why "
  "it tolerates noise so well.",
  "Five functions, AND, OR, NOT, and the inverted and exclusive forms, account for almost all "
  "combinational logic.",
  "A circle on a symbol output always means inversion, and NAND or NOR alone can build any function.",
  "The two inversion rules allow a function to be rearranged into whichever form suits the "
  "available devices.",
  "A latch retains state through cross-coupled feedback, and a motor starter seal-in circuit is "
  "the same circuit built from a relay.",
  "A flip-flop samples its inputs only at a clock edge, which makes counters and timing chains "
  "possible.",
  "Safety functions must be hard wired, because logic depends on the device working and powered.",
  "Floating inputs, mismatched thresholds and direct coil driving are the three commonest "
  "practical failures."],
 [["Bit place value","Position n carries 2\u207f","Binary number"],
  ["Values from n bits","2\u207f distinct values","Any binary field"],
  ["Hexadecimal grouping","One hex digit = four bits","Conversion shorthand"],
  ["Inverted AND","NOT(A AND B) = NOT A OR NOT B","Any number of inputs"],
  ["Inverted OR","NOT(A OR B) = NOT A AND NOT B","Any number of inputs"],
  ["Frequency division","f_out = f_in / 2\u207f","Chain of n flip-flops"],
  ["Counter range","0 to 2\u207f \u2212 1","n-stage counter"]],
 [["Forbidden band","The voltage range between the two valid logic thresholds"],
  ["Truth table","A complete listing of a function's output for every input combination"],
  ["Latch","A circuit that retains its state after the setting input is removed"],
  ["Seal-in contact","The auxiliary contact that maintains a contactor coil after the start button "
   "is released"],
  ["Flip-flop","A latch whose inputs are sampled only at a clock edge"],
  ["Fan-out","The number of inputs a single output can drive within its ratings"],
  ["Debounce","Conditioning applied to remove multiple edges from one contact operation"]],
 "Logic and analogue circuits both need a stable supply, and the quality of that supply "
 "determines whether either works reliably. The next chapter examines power supplies, regulation "
 "and the protection built around them.",
)
