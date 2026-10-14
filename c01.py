# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES

CH1=dict(n=1,title="Charge, voltage, current and energy",
 sub="The four quantities that every later chapter depends on",
 why="Every circuit calculation you will ever make reduces to four quantities and the "
     "relationships between them. Get these definitions precise now and the rest of the book "
     "becomes bookkeeping; leave them vague and even Ohm's law feels like guesswork.",
 objs=["State what charge, current, voltage, power and energy measure, and in which unit.",
   "Convert between coulombs, amperes, joules, volts and watts without a calculator.",
   "Choose a reference node and assign consistent polarity and current directions.",
   "Connect an ammeter and a voltmeter correctly and predict how each loads the circuit.",
   "Estimate the energy a load consumes over time and the cost of running it."],
 openfig=("c1_model","The quantities of a simple circuit. The source maintains a potential "
   "difference across the load; charge circulates; energy is transferred at the load.",46),
 secs=[
  dict(h2="Charge is the quantity being moved",
   paras=["Electric charge, symbol <i>Q</i>, is measured in coulombs (C). One coulomb is the "
     "charge carried by about 6.24 \u00d7 10<sup>18</sup> electrons. The electron charge itself is "
     "1.602 \u00d7 10<sup>\u221219</sup> C, negative by convention. Charge is conserved: it is never "
     "created or destroyed in a circuit, only relocated. That single fact is what later becomes "
     "Kirchhoff's current law.",
    "A battery does not store charge in any useful quantity; it stores chemical energy and uses "
     "it to push charge that is already present in the conductor. A copper conductor is already "
     "crowded with mobile electrons before the supply is connected. Switching on does not inject "
     "new carriers, it organises the drift of the carriers already there, which is why a lamp "
     "lights apparently instantly even though individual electrons drift at a fraction of a "
     "millimetre per second."],
   panel=("Why drift is slow but switching is fast",
     ["Drift velocity in a 2.5 mm\u00b2 conductor carrying 10 A is roughly 0.3 mm/s.",
      "The electric field that sets the drift propagates at a large fraction of the speed of "
      "light, so the far end of the circuit responds in nanoseconds.",
      "Practical consequence: conductor length changes resistance and voltage drop, not response time."])),
  dict(h2="Current is charge flow per unit time",
   paras=["Current, symbol <i>I</i>, is the rate at which charge passes a chosen cross-section. "
     "One ampere is one coulomb per second. Because current is defined through a surface, it is "
     "meaningless to speak of the current <i>at</i> a component without saying through which "
     "terminal; it is equally meaningless to speak of current flowing <i>to</i> a load, because "
     "the same current must return.",
    "Conventional current is drawn from the positive terminal, through the external circuit, to "
     "the negative terminal. Electrons in a metal move the opposite way. Both descriptions give "
     "identical answers, and every schematic in this book uses conventional current. The only "
     "rule that matters is that you declare a reference direction on the drawing and keep it; a "
     "negative answer then simply means the real flow opposes your arrow."],
   eq=["I = Q / t          Q = I t",
       "1 A = 1 C/s        1 mA = 10\u207b\u00b3 A"],
   bh="Direction conventions worth writing on your drawing",
   bullets=["Mark one node as the reference (0 V) before anything else.",
     "Draw a current arrow on every branch you intend to solve for.",
     "Place the voltmeter's black lead at the reference node and leave it there.",
     "A negative reading is information, not a mistake: it means the arrow is reversed."]),
  dict(h2="Voltage is energy per unit charge",
   paras=["Voltage, symbol <i>V</i> or <i>U</i>, is the work done per unit charge in moving "
     "charge between two points. One volt is one joule per coulomb. Voltage is therefore always "
     "a difference between two points, which is why a meter has two leads and why the phrase "
     "\u201cthe voltage at the motor\u201d is incomplete until you name the second point.",
    "Treating voltage as a difference removes a large family of beginner errors. A conductor "
     "floating at 480 V relative to earth but at 0 V relative to its neighbour will register "
     "nothing on a meter placed across the pair, and will still injure anyone who bridges it to "
     "earth. Potential is relative; hazard is not."],
   eq=["V = W / Q          W = V Q",
       "1 V = 1 J/C"],
   fig=("c1_meas","Correct instrument connections. The voltmeter sits across the component, the "
     "ammeter is inserted in the branch so that the branch current passes through it.",46)),
  dict(h2="Power and energy: the quantities on the bill",
   paras=["Power, symbol <i>P</i>, is the rate of energy transfer, measured in watts. One watt "
     "is one joule per second. In a circuit the product of the voltage across an element and the "
     "current through it gives the power that element absorbs. Energy is power accumulated over "
     "time, and utilities sell it in kilowatt-hours: one kilowatt sustained for one hour, equal "
     "to 3.6 megajoules.",
    "Power is where theory becomes thermal reality. A resistor dissipating 2 W in free air will "
     "reach a surface temperature high enough to discolour a circuit board; the same 2 W spread "
     "over a heatsink is unremarkable. Always calculate dissipation, then ask whether the part "
     "can shed it."],
   eq=["P = V I            W = P t",
       "1 kWh = 3.6 MJ = 3.6 \u00d7 10\u2076 J"],
   table=(["Quantity","Symbol","Unit","Defining relation"],
     [["Charge","Q","coulomb, C","Q = I t"],
      ["Current","I","ampere, A","I = Q / t"],
      ["Voltage","V","volt, V","V = W / Q"],
      ["Power","P","watt, W","P = V I"],
      ["Energy","W","joule, J","W = P t"],
      ["Resistance","R","ohm, "+OH,"R = V / I"]],None),
   after=["These six rows are the vocabulary of the whole book. Every equation that follows is "
     "either one of them rearranged or a statement about how several of them combine."]),
  dict(h2="Prefixes, and why they cause more errors than algebra",
   paras=["Most field mistakes are decimal mistakes. A result expressed as 0.000047 F invites "
     "error; the same value as 47 \u00b5F does not. Learn to carry prefixes through the "
     "calculation rather than converting everything to base units and back.",
    "A useful habit is to pair prefixes so that they cancel. Volts divided by kilohms gives "
     "milliamperes directly. Milliamperes multiplied by kilohms gives volts. Microfarads "
     "multiplied by kilohms gives milliseconds. These three pairings cover most of the "
     "arithmetic in electronics work."],
   table=(["Prefix","Symbol","Multiplier","Typical use"],
     [["mega","M","10\u2076","M"+OH+" insulation resistance, MW generation"],
      ["kilo","k","10\u00b3","k"+OH+" resistors, kW loads, kV distribution"],
      ["milli","m","10\u207b\u00b3","mA signal currents, mH chokes, mV offsets"],
      ["micro","\u00b5","10\u207b\u2076","\u00b5F capacitors, \u00b5A leakage"],
      ["nano","n","10\u207b\u2079","nF coupling capacitors, ns switching"],
      ["pico","p","10\u207b\u00b9\u00b2","pF stray capacitance, crystal loading"]],None),
   panel=("The three cancelling pairs",
     ["V \u00f7 k"+OH+" = mA, so 12 V across 4.7 k"+OH+" is 2.55 mA with no powers of ten.",
      "mA \u00d7 k"+OH+" = V, so 2.55 mA through 1.8 k"+OH+" drops 4.59 V.",
      "\u00b5F \u00d7 k"+OH+" = ms, so 100 \u00b5F with 10 k"+OH+" gives "+TAU+" = 1000 ms."])),
  dict(h2="Energy accounting around a loop",
   paras=["Because voltage is energy per unit charge, a complete trip around any loop must "
     "return a charge to its starting potential. Energy supplied by sources equals energy "
     "absorbed by everything else, including the resistance of the conductors themselves. This "
     "is the conservation statement that becomes Kirchhoff's voltage law in the next chapter.",
    "Treating conductor resistance as part of the accounting, rather than as an annoyance, "
     "explains a great deal of field behaviour: why a long run dims a lamp, why a motor starting "
     "surge makes lights flicker, and why voltage measured at the panel differs from voltage "
     "measured at the load."],
   fig=("c1_energy","Energy flow in a supply, conductor and load. The conductors are not ideal: "
     "part of the supplied energy is dissipated before it reaches the intended load.",46)),
 ],
 examples=[
  dict(title="Charge delivered by a lamp circuit",
   given="A 24 V lamp draws a steady 0.75 A and is left on for 20 minutes.",
   find="The charge circulated, the power and the energy transferred.",
   steps=[("Convert the time to seconds","t = 20 \u00d7 60 = 1200 s"),
     ("Charge from current and time","Q = I t = 0.75 \u00d7 1200 = 900 C"),
     ("Power from voltage and current","P = V I = 24 \u00d7 0.75 = 18 W"),
     ("Energy from power and time","W = P t = 18 \u00d7 1200 = 21 600 J = 21.6 kJ"),
     ("Energy as a billed quantity","W = 21 600 / 3.6\u00d710\u2076 = 0.006 kWh")],
   check="Cross-check through charge: W = V Q = 24 \u00d7 900 = 21 600 J. The two routes agree, "
     "which confirms the time conversion."),
  dict(title="Voltage drop along a supply cable",
   given="A load draws 16 A through a two-core run whose total loop resistance is 0.21 "+OH+". "
     "The panel measures 232 V.",
   find="The voltage at the load, the power lost in the cable and the percentage drop.",
   steps=[("Drop across the conductors","V_cable = I R = 16 \u00d7 0.21 = 3.36 V"),
     ("Voltage reaching the load","V_load = 232 \u2212 3.36 = 228.64 V"),
     ("Power dissipated in the cable","P_cable = I\u00b2 R = 16\u00b2 \u00d7 0.21 = 53.8 W"),
     ("Drop as a percentage","3.36 / 232 \u00d7 100 = 1.45 %")],
   check="1.45 % is inside the 3 % branch-circuit guidance of NFPA 70 (2023) 210.19(A) "
     "Informational Note 4, so the run is acceptable on voltage-drop grounds. Note that the "
     "53.8 W lost in the cable is real heat inside the wiring method."),
  dict(title="Running cost of a continuous load",
   given="A 1.8 kW immersion heater runs 2.5 hours per day. Energy costs 0.19 per kWh.",
   find="Daily energy, monthly cost over 30 days, and the current at 240 V.",
   steps=[("Daily energy","W = 1.8 \u00d7 2.5 = 4.5 kWh"),
     ("Monthly energy","4.5 \u00d7 30 = 135 kWh"),
     ("Monthly cost","135 \u00d7 0.19 = 25.65"),
     ("Current drawn","I = P / V = 1800 / 240 = 7.5 A")],
   check="7.5 A on a 240 V circuit is consistent with a 15 A branch circuit at 50 % loading, "
     "and the heater is a continuous load for sizing purposes.")],
 lab=dict(title="measuring current, voltage and power in a lamp circuit",
  aim="Establish by measurement that the current entering a load equals the current leaving it, "
      "that voltage is a difference between two points, and that the product of the two predicts "
      "the power the lamp actually dissipates.",
  gear=["Regulated DC supply, 0\u201330 V, current limit set to 1 A.",
    "Two digital multimeters, or one meter used twice with the supply switched off between moves.",
    "Filament lamp, 24 V 10 W, in a holder with screw terminals.",
    "Series resistor, 10 "+OH+" 5 W, to make the supply current limit meaningful.",
    "Insulated test leads, a screwdriver, and a notebook."],
  steps=["Draw the circuit before touching the equipment. Mark the reference node and the "
    "intended current direction.",
   "With the supply off and set to zero, connect the lamp in series with the 10 "+OH+" resistor.",
   "Insert the ammeter in the branch between the resistor and the lamp. The branch current must "
    "pass through the meter, so the circuit has to be opened to admit it.",
   "Connect the voltmeter across the lamp only. Leave its black lead on the reference node.",
   "Raise the supply in 4 V steps to 24 V, recording both readings at each step.",
   "Move the ammeter to the return conductor and repeat two of the steps. The reading must not "
    "change; this is conservation of charge, measured.",
   "Switch off, then place the voltmeter across the resistor and confirm that the two component "
    "voltages add to the supply voltage.",
   "Return the supply to zero and disconnect before dismantling."],
  fig=("c1_meas","Lab connections for the measurement sequence. Opening the branch to insert the "
    "ammeter is the step most often done wrongly.",44),
  thdr=["Supply (V)","Lamp voltage (V)","Current (A)","P = V I (W)","Lamp resistance ("+OH+")"],
  trows=[["4.0","","","",""],["8.0","","","",""],["12.0","","","",""],
    ["16.0","","","",""],["20.0","","","",""],["24.0","","","",""]],
  questions=["Plot lamp current against lamp voltage. The line is not straight. Explain why, in "
    "terms of filament temperature.",
   "Compute lamp resistance at 4 V and at 24 V. State the ratio and account for it.",
   "Did the ammeter reading change when you moved it to the return conductor? What would a "
    "change have told you about your connections?",
   "At 24 V, compare the measured power with the lamp's 10 W rating and comment on the series "
    "resistor's share.",
   "The ammeter has its own resistance. Estimate the error it introduces at 24 V and say whether "
    "it matters here."],
  safety=["Keep the supply below 30 V and the current limit at 1 A throughout this activity.",
    "Switch off and verify zero before changing any connection; moving an ammeter in a live "
    "circuit is how meters and fingers are damaged.",
    "The series resistor becomes hot. Allow it to cool before handling.",
    "Never place an ammeter across a source. The meter is a near short circuit on its current "
    "ranges."]),
 trouble=[["Lamp dark, meter shows full supply voltage across the lamp","Open filament or open "
   "holder contact","Measure resistance of the cold lamp out of circuit","Replace the lamp; "
   "inspect the holder for burnt contacts"],
  ["Lamp dim, voltage at the lamp well below the panel voltage","Excessive drop in the supply "
   "run or a high-resistance joint","Measure voltage at the panel and at the load under load","Re-terminate the joint or increase conductor size"],
  ["Ammeter reads zero but the lamp is lit","Meter on the wrong jack or a blown current fuse","Short the meter leads on the current range","Move the lead to the correct jack; replace the meter fuse"],
  ["Meter fuse blows the moment the supply is energised","Ammeter connected across the source "
   "rather than in series","Trace the meter leads against the drawing","Open the branch and "
   "insert the ammeter in it"],
  ["Readings drift upward over a minute","Filament heating, so resistance is rising","Record the "
   "reading at a fixed time after switch-on","Report readings with the timing stated"],
  ["Voltage reading unstable, current steady","Poor voltmeter lead contact","Wiggle the probes "
   "while watching the display","Clean and retighten the measuring points"]],
 tfig=("c1_energy","Where the supplied energy ends up. A fault that adds unwanted resistance "
   "moves energy out of the load and into the wiring.",44),
 habits=["State the reference point in every reading you write down. \u201c228 V\u201d means "
   "nothing; \u201c228 V line to neutral at the load terminals\u201d is a measurement.",
  "Predict before you probe. A meter confirms or refutes a prediction; used without one it only "
  "produces numbers.",
  "Record the supply voltage at the same instant as the branch current, because both move "
  "together when a fault is present.",
  "Treat conductor resistance as a component. It appears in the loop whether or not you drew it."],
 exercises=["A conductor passes 3.2 A for 4 minutes. How much charge has moved?",
  "A charge of 540 C is moved through a potential difference of 12 V. Find the energy transferred.",
  "Convert: 0.047 F to microfarads; 2 200 000 "+OH+" to megohms; 0.0056 A to milliamperes.",
  "A 9 V battery delivers 150 mA. Find the power and the energy supplied in 5 minutes.",
  "A 2.4 kW load runs on 240 V. Find the current and the resistance.",
  "A cable run has a loop resistance of 0.34 "+OH+" and carries 22 A. Find the voltage drop and "
  "the power lost in the conductors.",
  "A load is measured at 11.6 V while the supply terminals read 12.0 V. What is dropped in the "
  "wiring, and what fraction of the supply is that?",
  "Explain, using the definition of voltage, why a bird on a single energised conductor is not "
  "injured.",
  "A 60 W lamp runs 6 hours a day. Find the monthly energy at 30 days in kWh.",
  "An ammeter has 0.1 "+OH+" of internal resistance and is inserted in a branch of total "
  "resistance 4.9 "+OH+" fed from 12 V. Find the current with and without the meter, and the "
  "percentage error introduced."],
 answers=[["1","768 C","Q = I t with t = 240 s"],
  ["2","6.48 kJ","W = V Q = 12 \u00d7 540"],
  ["3","47 000 \u00b5F; 2.2 M"+OH+"; 5.6 mA","Shift the decimal point by the prefix exponent"],
  ["4","1.35 W; 405 J","P = V I, then W = P t with t = 300 s"],
  ["5","10 A; 24 "+OH,"I = P / V, then R = V / I"],
  ["6","7.48 V; 165 W","V = I R, then P = I\u00b2 R"],
  ["7","0.4 V; 3.3 %","Difference divided by the supply voltage"],
  ["8","No potential difference across the bird","Both feet are at essentially the same potential, "
   "so no appreciable current flows through it"],
  ["9","10.8 kWh","0.06 kW \u00d7 6 h \u00d7 30 d"],
  ["10","2.449 A with the meter, 2.4 A without, 2.0 % error","The meter adds series resistance; "
   "compare 12/4.9 with 12/5.0"]],
 summary=["Charge is the quantity moved, current its rate of flow, voltage the energy carried per "
  "unit charge, and power the rate at which that energy is delivered.",
  "Voltage exists only between two points; every reading needs a stated reference.",
  "Current is defined through a surface, so it must be measured in series and is the same "
  "entering and leaving a two-terminal element.",
  "Conductors are components. Their resistance takes a share of the supplied energy and converts "
  "it to heat inside the wiring method.",
  "Prefix arithmetic causes more field errors than algebra does; use cancelling pairs such as "
  "V \u00f7 k"+OH+" = mA.",
  "Energy billed in kilowatt-hours is the same quantity as energy in joules: 1 kWh = 3.6 MJ."],
 formulas=[["Charge and current","Q = I t","Steady current over an interval t"],
  ["Voltage and energy","W = V Q","Work to move charge Q through a difference V"],
  ["Power","P = V I","Instantaneous, or steady DC values"],
  ["Energy","W = P t","Constant power over an interval t"],
  ["Resistance","R = V / I","Defines resistance from a measured pair"],
  ["Conductor loss","P = I\u00b2 R","Heat generated in a run of known resistance"]],
 vocab=[["Reference node","The point chosen as 0 V, against which all other potentials are quoted"],
  ["Conventional current","Flow direction taken from positive to negative in the external circuit"],
  ["Drift velocity","Average speed of charge carriers along a conductor, typically under 1 mm/s"],
  ["Potential difference","Energy per unit charge between two named points"],
  ["Meter loading","The change a measuring instrument causes in the circuit it is measuring"]],
 bridge="You now have the quantities and the habit of declaring references and directions. "
  "The next chapter turns the two conservation statements behind them \u2014 charge is conserved "
  "at a junction, energy is conserved around a loop \u2014 into Kirchhoff's two laws, the tools "
  "that solve circuits Ohm's law alone cannot.",
)
