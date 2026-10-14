# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH9=mkch(9,"Magnetism and electromagnetism",
 "Fields, flux, force and induced voltage",
 "Every transformer, motor, relay, contactor and solenoid in an installation works because a "
 "current produces a magnetic field and a changing field produces a voltage. Those two "
 "statements, taken together, account for most of the equipment an electrician ever touches.",
 ["Describe a magnetic field in terms of flux and flux density.",
  "Apply the right-hand rule to find field direction around a conductor and inside a coil.",
  "Compute magnetomotive force, field strength and reluctance in a simple magnetic circuit.",
  "Compute the force on a current-carrying conductor in a field.",
  "State Faraday's and Lenz's laws and compute an induced voltage.",
  "Explain hysteresis and eddy-current losses and how laminated cores reduce them."],
 ("c9_coil","A coil wound on a core. The current in the winding drives flux around the magnetic "
  "circuit, and the core's permeability determines how much flux a given current produces.",46),
 [dict(h2="Flux and flux density",
   paras=["A magnetic field is described by its flux, measured in webers, and by how "
    "concentrated that flux is, measured as flux density in teslas. Flux density is simply flux "
    "divided by the area it passes through at right angles, so squeezing the same flux into a "
    "smaller cross-section raises the density.",
    "Flux density is the quantity that matters in practice, because force, induced voltage and "
    "core saturation all depend on it. A core driven beyond about 1.6 to 1.8 teslas saturates: "
    "further increases in current produce almost no further flux, and the equipment draws heavy "
    "current while doing no useful magnetic work."],
   eq=["B = \u03a6 / A",
       "\u03a6 in webers, A in square metres, B in teslas",
       "1 T = 1 Wb/m\u00b2"]),
  dict(h2="Field direction and the right-hand rules",
   paras=["Field direction is fixed by the current direction and found by a rule rather than by "
    "memory. Grip a straight conductor with the right hand, thumb pointing along conventional "
    "current, and the fingers wrap around it in the same sense as the circular field.",
    "For a coil, let the right-hand fingers follow the direction the current circulates in the "
    "turns and the thumb points to the north pole of the resulting field. Reversing the supply "
    "polarity reverses the poles, which is why a direct-current solenoid pulls in the same "
    "direction regardless of polarity only if its construction is deliberately "
    "polarity-independent."],
   bh="Working with field direction",
   bullets=["Thumb along current, fingers wrapping the conductor: straight conductor.",
     "Fingers following the turns, thumb to north: coil or solenoid.",
     "Reversing current reverses the poles of an electromagnet.",
     "Two conductors carrying current the same way attract; opposite ways repel.",
     "A permanent magnet has fixed poles, so a relay containing one will respond to polarity."]),
  dict(h2="The magnetic circuit",
   paras=["Flux around a core behaves much like current around an electric circuit, and the "
    "analogy is worth using. The driving quantity is magnetomotive force, the product of current "
    "and turns. The opposition is reluctance, which depends on path length, cross-sectional area "
    "and the permeability of the material.",
    "The crucial practical point is that air has a permeability thousands of times lower than "
    "iron, so even a small air gap dominates the reluctance of an otherwise iron path. This is "
    "why a contactor that fails to close fully draws heavy current: the residual gap keeps the "
    "reluctance high, the flux low, and the inrush current never falls to its sealed value."],
   eq=["F = N I      (ampere-turns)",
       "H = N I / l      (ampere-turns per metre)",
       "\u03a6 = F / S      S = l / (\u00b5\u2080 \u00b5_r A)",
       "B = \u00b5\u2080 \u00b5_r H      \u00b5\u2080 = 4\u03c0 \u00d7 10\u207b\u2077 H/m"],
   panel=("Why a small air gap matters so much",
     ["Relative permeability of transformer steel may be 4000; of air it is 1.",
      "A 1 mm gap in a 400 mm iron path can contribute more reluctance than all the iron.",
      "A contactor held partly open therefore keeps drawing its inrush current and overheats.",
      "Always investigate a buzzing or hot contactor coil as a mechanical problem first."])),
  dict(h2="Force on a conductor",
   paras=["A conductor carrying current across a magnetic field experiences a force at right "
    "angles to both. The force is proportional to flux density, current and the length of "
    "conductor in the field, and it is the mechanism by which every motor develops torque.",
    "The same effect explains why heavy fault currents are mechanically violent. Busbars "
    "carrying tens of kiloamperes exert large forces on each other, which is why switchgear "
    "bracing and bus supports are rated for short-circuit withstand and not merely for weight."],
   eq=["F = B I l sin\u03b8",
       "Maximum when the conductor is perpendicular to the field",
       "F in newtons, B in teslas, l in metres"],
   fig=("c9_relay","A relay: a coil drives flux through a magnetic circuit, the armature is "
     "attracted, and the contacts change state. Coil and contact circuits are electrically "
     "separate.",46)),
  dict(h2="Induced voltage: Faraday and Lenz",
   paras=["Faraday's law states that a voltage is induced in a circuit whenever the flux linking "
    "it changes, and that the magnitude is proportional to the rate of change and the number of "
    "turns. Nothing is induced by a steady field; only change produces voltage.",
    "Lenz's law fixes the polarity: the induced voltage always acts to oppose the change that "
    "produced it. This is not an arbitrary sign convention but a consequence of energy "
    "conservation, and it is the reason a generator becomes harder to turn as load is applied "
    "and the reason an inductor produces a large reverse voltage when its current is interrupted."],
   eq=["e = \u2212N d\u03a6/dt",
       "For a conductor moving through a field:  e = B l v sin\u03b8",
       "The minus sign is Lenz's law: opposition to the change"],
   after=["Both forms describe the same physics. The first is used for transformers and coils, "
    "where flux changes while the conductor stays still; the second is used for machines, where "
    "the conductor moves through a steady field."]),
  dict(h2="Core losses: hysteresis and eddy currents",
   paras=["Driving a core through repeated magnetisation cycles costs energy, because the "
    "material resists reversing its internal domains. The energy lost per cycle is proportional "
    "to the area of the hysteresis loop, so loss rises with frequency and with peak flux density.",
    "A solid core also behaves as a short-circuited turn: the changing flux induces circulating "
    "eddy currents in the iron itself, which dissipate heat. Laminating the core into thin "
    "insulated sheets interrupts those current paths while leaving the magnetic path intact, "
    "which is why transformer and motor cores are built from stacked laminations rather than "
    "solid blocks."],
   table=(["Loss mechanism","Cause","Varies with","Reduced by"],
     [["Hysteresis","Energy to reverse magnetic domains","Frequency and peak flux density",
       "Grain-oriented silicon steel"],
      ["Eddy current","Circulating current induced in the core","Square of frequency and of "
       "flux density","Thin insulated laminations"],
      ["Copper loss","Resistance of the windings","Square of the load current","Larger conductor "
       "cross-section"],
      ["Stray loss","Flux leaking into tanks and clamps","Load current","Magnetic shielding and "
       "layout"]],None),
   panel=("Core loss is present whenever the equipment is energised",
     ["Hysteresis and eddy-current loss depend on voltage and frequency, not on load.",
      "A lightly loaded transformer therefore still dissipates its full core loss.",
      "Copper loss varies with the square of the load current and falls away at light load.",
      "This is why leaving transformers energised to serve no load wastes energy continuously."])),
 ],
 [ex("Flux density and saturation",
   "A core of cross-section 25 mm \u00d7 40 mm carries a flux of 1.4 mWb.",
   "The flux density, and whether the core is likely to be saturated.",
   [("Cross-sectional area","A = 0.025 \u00d7 0.040 = 1.0 \u00d7 10\u207b\u00b3 m\u00b2"),
    ("Flux density","B = \u03a6/A = 1.4\u00d710\u207b\u00b3 / 1.0\u00d710\u207b\u00b3 = 1.4 T"),
    ("Compare with typical saturation","Silicon steel saturates near 1.6 to 1.8 T"),
    ("Conclusion","1.4 T is below saturation but with little margin")],
   "A design at 1.4 T is normal practice. A 15 % supply overvoltage would push the flux to about "
   "1.6 T and the magnetising current would rise sharply, which is why transformers hum louder "
   "and run hotter on a high supply."),
  ex("Ampere-turns and the effect of an air gap",
   "A coil of 600 turns carries 0.5 A on an iron path 300 mm long, area 1.0 \u00d7 10\u207b\u00b3 m\u00b2, "
   "relative permeability 3000. A 0.8 mm air gap is then introduced.",
   "The flux before and after the gap is introduced.",
   [("Magnetomotive force","F = N I = 600 \u00d7 0.5 = 300 ampere-turns"),
    ("Iron reluctance","S_Fe = 0.300/(4\u03c0\u00d710\u207b\u2077 \u00d7 3000 \u00d7 1\u00d710\u207b\u00b3) = 79 600 A/Wb"),
    ("Flux with no gap","\u03a6 = 300/79 600 = 3.77 mWb"),
    ("Gap reluctance","S_air = 0.0008/(4\u03c0\u00d710\u207b\u2077 \u00d7 1 \u00d7 1\u00d710\u207b\u00b3) = 636 600 A/Wb"),
    ("Total reluctance","S = 79 600 + 636 600 = 716 200 A/Wb"),
    ("Flux with the gap","\u03a6 = 300/716 200 = 0.42 mWb")],
   "A gap less than three thousandths of the path length cut the flux to about one ninth, because "
   "its reluctance is eight times that of all the iron. This is the quantitative reason a "
   "contactor must seal fully."),
  ex("Induced voltage in a moving conductor",
   "A conductor 250 mm long moves at 12 m/s perpendicular to a field of 0.8 T.",
   "The induced voltage, and the value if the conductor moves at 30\u00b0 to the field.",
   [("Perpendicular motion","e = B l v = 0.8 \u00d7 0.25 \u00d7 12 = 2.4 V"),
    ("At 30\u00b0 to the field","e = 2.4 \u00d7 sin30\u00b0 = 1.2 V"),
    ("At 0\u00b0, moving along the field","e = 2.4 \u00d7 sin0\u00b0 = 0 V")],
   "Only motion across the flux generates voltage. A conductor sliding along the field lines cuts "
   "no flux and generates nothing, which is why machine geometry places conductors across the "
   "field at the air gap."),
  ex("Force on a busbar during a fault",
   "Two parallel busbars 1.2 m long sit in a stray field of 0.35 T and carry 18 kA during a fault.",
   "The force on one bar.",
   [("Force equation","F = B I l"),
    ("Substitute","F = 0.35 \u00d7 18 000 \u00d7 1.2"),
    ("Result","F = 7560 N, about 770 kg equivalent"),
    ("Duration","Present only for the clearing time, perhaps 100 ms")],
   "Nearly a tonne of force applied for a tenth of a second explains why bus supports are rated "
   "for short-circuit withstand and why damaged bracing must be replaced after a major fault.")],
 lab("magnetic field, induced voltage and a relay's operating points",
  "Observe field direction around a coil, demonstrate that only changing flux induces a voltage, "
  "measure the pull-in and drop-out voltages of a relay, and show the effect of preventing the "
  "armature from sealing.",
  ["Air-cored and iron-cored coils, 600 turns.",
   "Bar magnet, plotting compass and iron filings with a covered tray.",
   "Direct-current supply, 0 to 24 V, current limited to 1 A.",
   "Centre-zero galvanometer or a multimeter on its most sensitive direct-voltage range.",
   "Relay, 12 V coil, with accessible contacts; a 24 V lamp as the contact load.",
   "Oscilloscope with a single channel."],
  ["With the coil de-energised, map the field of the bar magnet using the plotting compass and "
   "sketch the pattern.",
   "Energise the iron-cored coil at 6 V and use the compass to identify its north pole. Confirm "
   "the result against the right-hand rule and the winding direction.",
   "Reverse the supply polarity and confirm that the poles exchange.",
   "Connect the galvanometer across a second coil placed near the first. Switch the first coil "
   "on and off and record the direction of deflection in each case.",
   "Hold the first coil energised steadily and confirm that the galvanometer reads zero.",
   "Move the bar magnet into the second coil, hold it still, then withdraw it. Record the "
   "deflection for each of the three actions.",
   "Repeat the insertion at two clearly different speeds and compare the deflections.",
   "Wire the relay coil to the variable supply and the lamp through the relay contacts.",
   "Raise the coil voltage slowly and record the voltage at which the contacts close.",
   "Lower the voltage slowly and record the voltage at which they reopen. Repeat three times.",
   "Insert a 0.5 mm shim to prevent the armature sealing, re-energise at rated coil voltage and "
   "record the coil current. Compare with the sealed current."],
  ("c9_coil","The coil and core used for the field and induction tests. The second coil is "
   "placed to share the first coil's flux.",46),
  ["Test","Observation","Deflection or reading","Explanation"],
  [["Coil switched on","","",""],["Coil switched off","","",""],
   ["Coil held energised","","",""],["Magnet inserted slowly","","",""],
   ["Magnet inserted quickly","","",""],["Magnet held stationary","","",""],
   ["Relay pull-in voltage","","",""],["Relay drop-out voltage","","",""],
   ["Coil current, sealed","","",""],["Coil current, shimmed open","","",""]],
  ["Why did the galvanometer read zero while the coil was held energised, even though a strong "
   "field was present?",
   "Why were the switch-on and switch-off deflections in opposite directions? Relate your answer "
   "to Lenz's law.",
   "How did deflection depend on the speed of the magnet, and which term in Faraday's law does "
   "that confirm?",
   "Why is the drop-out voltage lower than the pull-in voltage? Explain using reluctance and the "
   "air gap.",
   "By what factor did the coil current rise when the armature was prevented from sealing, and "
   "what would that do to the coil over time?",
   "A relay in service chatters on and off rapidly. Using your pull-in and drop-out figures, "
   "explain how a sagging supply could produce this."],
  ["Limit the supply current to 1 A and do not exceed the coil's rated voltage for more than a "
   "few seconds.",
   "Do not leave the relay coil shimmed and energised for longer than the measurement requires; "
   "the coil overheats quickly.",
   "Interrupting an inductive coil produces a high reverse voltage. Do not hold bare coil "
   "terminals while switching.",
   "Keep iron filings in a sealed tray and clear of eyes and of the equipment.",
   "Energised coils and cores become hot. Allow them to cool before handling."]),
 [["Contactor buzzes loudly and the coil overheats","Armature not sealing, so the air gap keeps "
   "reluctance and current high","Measure coil current and compare with the sealed value; inspect "
   "the pole faces","Clean or dress the pole faces, free the mechanism, replace a worn armature"],
  ["Transformer hums louder than usual and runs hot at no load","Supply voltage high, driving the "
   "core toward saturation","Measure supply voltage and compare with the nameplate",
   "Correct the supply voltage or change the tap setting"],
  ["Relay drops out on motor starting","Supply sag takes the coil below its drop-out voltage",
   "Record coil voltage during the start with a logging meter","Supply the control circuit from a "
   "stiffer source, or fit a relay with a wider voltage window"],
  ["Solenoid valve will not pull in but the coil is energised","Mechanical obstruction, or coil "
   "voltage below pull-in","Measure coil voltage at the terminals and check free movement",
   "Clear the obstruction; verify the coil voltage rating matches the supply"],
  ["Core of a repaired transformer runs much hotter than before","Laminations shorted together "
   "during repair, allowing eddy currents","Compare no-load loss with the original test figure",
   "Restore the interlaminar insulation or replace the core assembly"],
  ["Permanent magnet motor or relay has weakened over time","Magnet partly demagnetised by heat "
   "or by an opposing field","Measure flux density at the pole face against the original value",
   "Replace the magnet assembly and remove the source of overheating"]],
 ("c9_thermo","A thermocouple: two dissimilar conductors produce a small voltage that depends on "
  "the junction temperature, used to monitor magnetic equipment for overheating.",44),
 ["Treat a buzzing contactor as a mechanical fault, not an electrical one, and check the pole "
  "faces before condemning the coil.",
  "Record pull-in and drop-out voltages when commissioning control gear, so later nuisance "
  "operation can be diagnosed against known figures.",
  "Fit a suppression diode or snubber across any coil switched by a semiconductor or a delicate "
  "contact.",
  "Investigate a transformer that has become noisier, because increased hum usually means flux "
  "density has risen."],
 ["A core of area 8 \u00d7 10\u207b\u2074 m\u00b2 carries 1.0 mWb. Find the flux density.",
  "Find the flux needed to produce 1.5 T in a core of area 1.2 \u00d7 10\u207b\u00b3 m\u00b2.",
  "A coil of 450 turns carries 0.8 A. Find the magnetomotive force.",
  "For the coil above on a 250 mm path, find the field strength H.",
  "State the two laws that together determine the magnitude and the polarity of an induced voltage.",
  "A conductor 0.4 m long moves at 15 m/s perpendicular to a 0.6 T field. Find the induced voltage.",
  "Explain why a steady direct current in a coil induces no voltage in a nearby coil.",
  "A conductor carrying 250 A lies 0.3 m long in a 0.5 T field. Find the force on it.",
  "Explain why transformer cores are laminated rather than solid.",
  "State which transformer losses depend on load current and which do not, and why that matters "
  "for a lightly loaded unit.",
  "Explain why a 1 mm air gap can dominate the reluctance of a 400 mm iron magnetic circuit.",
  "A relay pulls in at 9.2 V and drops out at 4.1 V. Explain the difference in terms of the air gap."],
 [["1","1.25 T","B = \u03a6/A"],
  ["2","1.8 mWb","\u03a6 = B A"],
  ["3","360 ampere-turns","F = N I"],
  ["4","1440 A/m","H = N I / l"],
  ["5","Faraday's law and Lenz's law","Faraday gives magnitude from rate of change; Lenz gives "
   "the opposing polarity"],
  ["6","3.6 V","e = B l v"],
  ["7","Flux is not changing","Faraday's law depends on d\u03a6/dt, which is zero for steady current"],
  ["8","37.5 N","F = B I l"],
  ["9","To interrupt eddy-current paths","Thin insulated sheets break the circulating current "
   "while keeping the magnetic path"],
  ["10","Core loss is load-independent; copper loss varies with current squared","A lightly "
   "loaded transformer still dissipates full core loss, so energising unused units wastes energy"],
  ["11","Air's permeability is thousands of times lower","Reluctance is inversely proportional to "
   "permeability, so a short air path can outweigh a long iron one"],
  ["12","Once sealed, the gap is gone and reluctance falls","Less current is needed to hold the "
   "armature than to pull it in, so drop-out is well below pull-in"]],
 ["Flux density, not total flux, determines force, induced voltage and saturation.",
  "Right-hand rules fix field direction from current direction for both straight conductors and coils.",
  "The magnetic circuit analogy relates ampere-turns, reluctance and flux, and shows why a small "
  "air gap dominates an iron path.",
  "Force on a conductor is B I l, which produces motor torque and makes heavy fault currents "
  "mechanically destructive.",
  "Only changing flux induces voltage; Faraday sets the magnitude and Lenz sets the opposing polarity.",
  "Hysteresis and eddy-current losses depend on voltage and frequency rather than load, and "
  "lamination addresses the eddy-current component."],
 [["Flux density","B = \u03a6 / A","Uniform flux through a known area"],
  ["Magnetomotive force","F = N I","Driving quantity of a magnetic circuit"],
  ["Field strength","H = N I / l","Along a uniform magnetic path"],
  ["Reluctance","S = l / (\u00b5\u2080 \u00b5_r A)","Opposition of a magnetic path to flux"],
  ["Magnetic Ohm's law","\u03a6 = F / S","Series magnetic circuit"],
  ["Force on a conductor","F = B I l sin\u03b8","Conductor crossing a field"],
  ["Faraday's law","e = \u2212N d\u03a6/dt","Changing flux linking a coil"],
  ["Motional voltage","e = B l v sin\u03b8","Conductor moving through a field"]],
 [["Flux","The total magnetic field passing through a surface, in webers"],
  ["Flux density","Flux per unit area, in teslas; the quantity that sets force and saturation"],
  ["Magnetomotive force","The ampere-turn product that drives flux around a magnetic circuit"],
  ["Reluctance","The opposition a magnetic path presents to flux"],
  ["Saturation","The condition where further magnetomotive force produces little further flux"],
  ["Hysteresis","Energy lost per magnetisation cycle in reversing magnetic domains"],
  ["Eddy current","Circulating current induced in a core, suppressed by lamination"]],
 "Faraday's law applied to two windings on a shared core gives the transformer, the single most "
 "important application of electromagnetism in power distribution. The next chapter develops it.",
)
