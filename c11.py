# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH11=mkch(11,"Rotating machines",
 "Motors, generators, slip, torque and starting",
 "Motors consume the majority of the electrical energy used in industry, and a motor that is "
 "wrongly started, wrongly protected or wrongly loaded is the most common cause of both energy "
 "waste and unplanned downtime. Understanding slip, torque and starting current explains most of "
 "what goes wrong.",
 ["Explain how a three-phase supply produces a rotating magnetic field.",
  "Compute synchronous speed, slip and rotor frequency.",
  "Relate torque, speed and mechanical power output.",
  "Explain why starting current is high and describe methods of reducing it.",
  "Interpret a motor nameplate and use it to select protection.",
  "Describe generator action and the effect of applying load."],
 ("c11_dol","A direct-on-line starter. The contactor seals in through its own auxiliary contact, "
  "and the overload relay opens the control circuit if the motor draws excessive current.",46),
 [dict(h2="The rotating magnetic field",
   paras=["Three windings spaced 120 mechanical degrees apart and fed from a three-phase supply "
    "produce a magnetic field of constant magnitude that rotates at a speed fixed by the supply "
    "frequency and the number of poles. Nothing mechanical rotates to produce it; the rotation "
    "comes from the sequential rise and fall of the three phase currents.",
    "This is the central elegance of the three-phase induction motor. The rotating field "
    "sweeps past the rotor conductors, inducing voltage and current in them, and the resulting "
    "force drags the rotor around after the field. Reversing any two supply phases reverses the "
    "direction of field rotation and therefore of the motor."],
   eq=["n\u209b = 120 f / p      (revolutions per minute)",
       "f in hertz, p the number of poles",
       "At 50 Hz: 4 poles gives 1500 rev/min; 60 Hz gives 1800 rev/min"],
   panel=("Reversing a three-phase motor",
     ["Exchanging any two of the three supply conductors reverses rotation.",
      "The third conductor and the protective conductor are left undisturbed.",
      "Confirm direction with the coupling removed or the load safely free to turn.",
      "Never reverse a motor by altering the protective earthing connection."])),
  dict(h2="Slip and rotor frequency",
   paras=["The rotor can never quite reach synchronous speed. If it did, there would be no "
    "relative motion between the field and the rotor conductors, no flux would be cut, no current "
    "would be induced, and no torque would be produced. The rotor therefore settles at a speed "
    "slightly below synchronous, and that difference is the slip.",
    "Slip is small at light load and grows as load increases, because more relative motion is "
    "needed to induce the larger rotor current that larger torque requires. Typical full-load "
    "slip for a general-purpose induction motor is 2 to 5 per cent. Rotor frequency is the supply "
    "frequency multiplied by the fractional slip, so at standstill the rotor sees full supply "
    "frequency and at running speed it sees only a few hertz."],
   eq=["s = (n\u209b \u2212 n\u1d63) / n\u209b      (fractional slip)",
       "Slip % = s \u00d7 100",
       "f\u1d63 = s f      (rotor frequency)",
       "n\u1d63 = n\u209b (1 \u2212 s)"],
   after=["The nameplate speed is the full-load speed, not the synchronous speed. A nameplate "
    "reading 1440 rev/min on a 50 Hz supply indicates a four-pole machine with 4 per cent slip."]),
  dict(h2="Torque, speed and power",
   paras=["Mechanical output power is the product of torque and angular speed. For the same "
    "output power, a slower machine must develop proportionally more torque, which is why "
    "low-speed motors and geared drives are physically larger for a given rating.",
    "Torque is not constant across the speed range. Starting torque is typically one and a half "
    "to two and a half times full-load torque, torque then rises to a pull-up and breakdown "
    "maximum and falls away as the machine approaches synchronous speed. A load whose torque "
    "demand exceeds the available torque at any speed will stall the motor there."],
   eq=["P = 2\u03c0 n T / 60      (n in rev/min, T in newton metres, P in watts)",
       "T = 9.55 P / n",
       "Efficiency \u03b7 = mechanical output / electrical input"],
   fig=("c11_rev","A reversing arrangement. Two contactors supply the motor with two phases "
     "exchanged, and they are interlocked so that both can never close together.",46)),
  dict(h2="Starting current and starting methods",
   paras=["At the instant of starting, the rotor is stationary, slip is unity and the machine "
    "behaves much like a transformer with a short-circuited secondary. The current drawn is "
    "typically five to eight times full-load current, and it persists until the rotor accelerates.",
    "Direct-on-line starting is simplest and gives full starting torque, but the current step may "
    "cause supply voltage dips that disturb other equipment. Star-delta starting reconnects the "
    "windings to reduce the starting current to about one third, but reduces starting torque in "
    "the same proportion, so it suits only loads that start lightly. Soft starters and variable "
    "frequency drives control the applied voltage or frequency electronically and give the "
    "smoothest start, at greater cost and complexity."],
   table=(["Starting method","Starting current","Starting torque","Suited to"],
     [["Direct on line","5 to 8 times full load","Full, 150 to 250 %","Small motors, stiff "
       "supplies, loads needing full torque"],
      ["Star-delta","About one third of direct on line","About one third","Fans, pumps, "
       "unloaded compressors"],
      ["Autotransformer","Selectable by tap","Reduced as the square of voltage","Larger machines "
       "needing a chosen compromise"],
      ["Soft starter","Ramped and adjustable","Ramped and adjustable","Belt drives and loads "
       "sensitive to shock"],
      ["Variable frequency drive","Near full-load current","Full torque from zero speed",
       "Variable-speed duty and high-inertia loads"]],None),
   panel=("Starting current is a design constraint, not a nuisance",
     ["A six-times starting current on a 40 A motor draws 240 A for several seconds.",
      "Protection must tolerate that without tripping, yet still clear a genuine fault.",
      "Supply impedance determines how far the resulting voltage dip propagates.",
      "Frequent starting accumulates heating; respect the stated starts-per-hour limit."])),
  dict(h2="Reading a nameplate",
   paras=["The nameplate is the authoritative source for protection and connection decisions. It "
    "states rated voltage and the connection it applies to, full-load current, output power, "
    "full-load speed, frequency, power factor, efficiency class, insulation class, enclosure "
    "rating and duty type.",
    "Two entries cause the most confusion. The stated power is mechanical output at the shaft, "
    "not electrical input, so input power is always higher by the efficiency. And where two "
    "voltages are shown, each corresponds to a particular winding connection, so a motor marked "
    "for both 400 V in star and 230 V in delta must be connected to suit the actual supply."],
   bh="Nameplate entries that drive decisions",
   bullets=["Full-load current sets the overload relay setting and the cable size.",
     "Rated voltage must be read together with the stated connection.",
     "Full-load speed reveals the pole count and the slip.",
     "Insulation class fixes the permitted temperature rise.",
     "Duty type states whether continuous running is permitted.",
     "Enclosure rating must suit the installed environment."]),
  dict(h2="Generator action",
   paras=["The same machine run as a generator reverses the energy flow. Driving the rotor "
    "mechanically while its field is excited induces voltage in the stator windings, and the "
    "frequency produced depends on the driven speed and the pole count.",
    "Applying electrical load makes the machine harder to turn. The load current produces its own "
    "field, which opposes the rotation by Lenz's law, so the prime mover must supply more "
    "mechanical power. This is why a generator's engine note changes audibly as load is applied "
    "and why governor response determines how well frequency is held."],
   eq=["f = p n / 120      (generated frequency)",
       "Mechanical input = electrical output + losses"],
   fig=("c11_gen","A generator supplying a load. Mechanical drive turns the excited rotor, and "
     "the load current produces an opposing field that the prime mover must work against.",46)),
 ],
 [ex("Synchronous speed, slip and rotor frequency",
   "A four-pole induction motor on a 50 Hz supply runs at 1440 rev/min at full load.",
   "The synchronous speed, the slip, and the rotor frequency.",
   [("Synchronous speed","n\u209b = 120 \u00d7 50/4 = 1500 rev/min"),
    ("Slip speed","1500 \u2212 1440 = 60 rev/min"),
    ("Fractional slip","s = 60/1500 = 0.04, that is 4 %"),
    ("Rotor frequency","f\u1d63 = 0.04 \u00d7 50 = 2 Hz"),
    ("At standstill","s = 1, so f\u1d63 = 50 Hz")],
   "Four per cent slip is normal for a general-purpose machine. Note that the rotor sees only 2 Hz "
   "when running but full supply frequency at the instant of starting, which is why starting "
   "conditions are so much more severe."),
  ex("Torque from rated output and speed",
   "A motor is rated 7.5 kW at 1440 rev/min.",
   "The full-load torque, and the torque if the same power were produced at 720 rev/min.",
   [("Torque equation","T = 9.55 P / n"),
    ("At 1440 rev/min","T = 9.55 \u00d7 7500/1440 = 49.7 N\u00b7m"),
    ("At 720 rev/min","T = 9.55 \u00d7 7500/720 = 99.5 N\u00b7m"),
    ("Observation","Halving the speed doubles the torque for the same power")],
   "The low-speed machine must develop twice the torque, so its shaft, bearings and frame are "
   "larger for the same rating. This is the reason an eight-pole motor is physically bigger than "
   "a four-pole motor of equal power."),
  ex("Starting current and overload setting",
   "A motor has a nameplate full-load current of 18 A and a starting current six times full load.",
   "The starting current, a suitable overload relay setting, and the implication for cable sizing.",
   [("Starting current","6 \u00d7 18 = 108 A"),
    ("Duration","Typically a few seconds until the rotor accelerates"),
    ("Overload relay setting","Set at the nameplate full-load current, 18 A"),
    ("Cable sizing","Sized on 18 A continuous, with voltage drop checked at 108 A"),
    ("Protective device","Must tolerate 108 A for the acceleration time without tripping")],
   "The overload relay is set on full-load current because it protects against sustained "
   "overloading; its time characteristic is what allows the starting surge through. The cable "
   "carries 18 A continuously, but the momentary 108 A must not cause an unacceptable voltage dip."),
  ex("Input power from mechanical output",
   "A 5.5 kW motor has an efficiency of 0.88 and a power factor of 0.85 on a 400 V three-phase "
   "supply.",
   "The electrical input power, the apparent power and the line current.",
   [("Input power","P_in = 5500/0.88 = 6250 W"),
    ("Apparent power","S = 6250/0.85 = 7353 VA"),
    ("Line current","I = 7353/(\u221a3 \u00d7 400) = 10.6 A"),
    ("Compare","A nameplate would show roughly 10.6 A full-load current")],
   "The nameplate kilowatt figure is shaft output, so input is always higher. Both efficiency and "
   "power factor must be applied to arrive at the current the cable and protection must handle.")],
 lab("motor nameplate, starting current, slip and direction",
  "Interpret a nameplate and predict the machine's behaviour, then measure starting current, "
  "running current, slip at two loads and verify the effect of exchanging two supply phases.",
  ["Three-phase cage induction motor, 0.75 to 1.5 kW, on a guarded test bed.",
   "Direct-on-line starter with an adjustable overload relay, and a star-delta starter if available.",
   "Clamp meter with inrush or peak-hold capability.",
   "Non-contact tachometer.",
   "Mechanical brake or dynamometer load, with a guard.",
   "True rms multimeter and a three-phase power meter.",
   "Lock-off devices and a voltage proving unit."],
  ["Record every entry from the nameplate before energising anything.",
   "From the nameplate speed and frequency, compute the pole count, the synchronous speed and the "
   "full-load slip, and write the predictions down.",
   "From the rated output, efficiency and power factor, predict the full-load line current and "
   "compare it with the nameplate figure.",
   "Prove the supply dead, lock off, and confirm the motor terminal connection matches the supply "
   "voltage and the nameplate.",
   "Set the overload relay to the nameplate full-load current.",
   "With the coupling guarded and the load disconnected, start the motor direct on line and "
   "capture the starting current with the clamp meter on inrush.",
   "Measure the no-load running current and the no-load speed.",
   "Apply the brake to roughly half of rated torque. Record current, speed and input power.",
   "Increase to full-load torque, then record current, speed and input power again.",
   "Compute slip at each load condition from your measured speeds.",
   "Stop the motor, prove dead, lock off, and exchange two supply conductors.",
   "Restart and confirm the direction of rotation has reversed.",
   "If a star-delta starter is available, repeat the starting-current measurement and compare."],
  ("c11_dol","The direct-on-line test arrangement, with the overload relay in the control "
   "circuit and the clamp meter positioned on one supply conductor.",46),
  ["Condition","Current (A)","Speed (rev/min)","Slip (%)","Input power and comment"],
  [["Starting, direct on line","","","",""],["No load, running","","","",""],
   ["Half load","","","",""],["Full load","","","",""],
   ["Starting, star-delta","","","",""],["Reversed rotation check","","","",""]],
  ["What was the ratio of your measured starting current to full-load current, and how does that "
   "compare with the usual five to eight times?",
   "How did slip change between no load, half load and full load? Explain the trend using "
   "induced rotor current.",
   "Why does the motor draw appreciable current at no load, and what is that current doing?",
   "Compare your predicted full-load current with the measured value and account for any difference.",
   "If you used the star-delta starter, by what factor did starting current fall, and what "
   "happened to starting torque?",
   "The nameplate speed is below synchronous speed. Explain why a cage induction motor can never "
   "run at synchronous speed.",
   "Compute the full-load torque from your measured output and speed, and compare it with the "
   "brake reading."],
  ["Rotating machinery must be fully guarded, with couplings and shaft ends enclosed before "
   "energising.",
   "Prove dead and lock off before touching any motor terminal, and before exchanging phases.",
   "Confirm the direction of rotation with the load disconnected or safely free to turn.",
   "Tie back long hair, remove loose clothing, jewellery and lanyards near the shaft.",
   "Starting current is many times running current. Confirm the clamp meter range before "
   "capturing it.",
   "Respect the stated starts-per-hour limit; repeated starting overheats the windings.",
   "Allow the brake and the motor frame to cool before handling."]),
 [["Motor hums but will not start, and draws heavy current","Single phasing from one lost supply "
   "conductor or one open winding","Measure current in all three conductors; they should be "
   "nearly equal","Restore the lost phase or rewind; investigate why the conductor opened"],
  ["Overload relay trips a few seconds after each start","Relay set below full-load current, or "
   "the starting time exceeds the relay class","Compare the setting with the nameplate and time "
   "the acceleration","Set the relay to nameplate full-load current and select a suitable trip class"],
  ["Motor runs hot at normal current","Blocked ventilation, high ambient temperature, or "
   "excessive starts per hour","Check airflow and measure frame temperature; count the starts",
   "Clear the cooling path, reduce start frequency, or fit a machine rated for the duty"],
  ["Motor runs in the wrong direction after rewiring","Two supply conductors exchanged relative "
   "to the original connection","Confirm rotation with the load uncoupled","Exchange any two "
   "supply conductors, leaving the protective conductor alone"],
  ["Speed is well below the nameplate figure under load","Mechanical overload, or reduced supply "
   "voltage lowering available torque","Measure terminal voltage under load and compare current "
   "with full load","Reduce the load, correct the voltage, or fit a larger machine"],
  ["Motor stalls partway through acceleration","Load torque exceeds the machine's torque at that "
   "speed, often with reduced-voltage starting","Compare the load torque curve with the motor "
   "torque curve","Start direct on line, use a soft starter, or fit a machine with higher pull-up "
   "torque"],
  ["Bearing noise and rising vibration over weeks","Bearing wear, shaft misalignment or an "
   "unbalanced coupling","Measure vibration and check alignment at the coupling","Replace the "
   "bearings and realign; correct the cause of the misalignment"]],
 ("c11_rev","Interlocked reversing contactors. The interlock prevents both contactors closing "
  "together, which would short the supply between two phases.",46),
 ["Set overload relays to the nameplate full-load current, not to a convenient round number.",
  "Measure current in all three conductors when a motor misbehaves; an imbalance points straight "
  "to single phasing.",
  "Confirm rotation direction with the load uncoupled before coupling a pump or compressor.",
  "Photograph the nameplate at commissioning, because it becomes illegible long before the motor "
  "fails.",
  "Count starts per hour on cyclic duty, since cumulative starting heat destroys more windings "
  "than running load does."],
 ["Find the synchronous speed of a six-pole motor on a 50 Hz supply.",
  "A four-pole 60 Hz motor runs at 1740 rev/min. Find the slip as a percentage.",
  "Find the rotor frequency for 5 % slip on a 50 Hz supply.",
  "State why a cage induction motor cannot run at synchronous speed.",
  "Find the full-load torque of a 4 kW motor running at 1455 rev/min.",
  "Find the output power of a motor developing 65 N\u00b7m at 960 rev/min.",
  "A motor has a full-load current of 24 A and starts at seven times that. Find the starting current.",
  "State the setting you would apply to the overload relay for the motor above, and why.",
  "State the approximate effect of star-delta starting on starting current and on starting torque.",
  "A nameplate reads 400 V, 11 kW, 0.86 power factor, efficiency 0.9. Find the full-load line "
  "current on a three-phase supply.",
  "Explain why a generator becomes mechanically harder to turn as electrical load is applied.",
  "A motor nameplate reads 1455 rev/min at 50 Hz. Determine the pole count and the full-load slip.",
  "Explain why exchanging two supply conductors reverses a three-phase motor.",
  "State two nameplate entries that must be checked before selecting the supply cable, and why."],
 [["1","1000 rev/min","n\u209b = 120f/p"],
  ["2","3.3 %","n\u209b = 1800; slip = 60/1800"],
  ["3","2.5 Hz","f\u1d63 = s f"],
  ["4","No relative motion means no induced current","Without slip no flux is cut, so no rotor "
   "current and no torque exist"],
  ["5","26.3 N\u00b7m","T = 9.55 P/n"],
  ["6","6.53 kW","P = 2\u03c0nT/60"],
  ["7","168 A","Starting current is a multiple of full-load current"],
  ["8","24 A","The relay guards against sustained overload; its time characteristic passes the "
   "starting surge"],
  ["9","Both fall to about one third","Reduced winding voltage reduces current, and torque falls "
   "with the square of voltage"],
  ["10","20.5 A","P_in = 11000/0.9 = 12222 W; I = 12222/(\u221a3 \u00d7 400 \u00d7 0.86)"],
  ["11","Load current produces an opposing field","By Lenz's law the reaction opposes rotation, "
   "so the prime mover must supply more mechanical power"],
  ["12","Four poles, 3 % slip","n\u209b = 1500, so slip = 45/1500"],
  ["13","It reverses the direction of field rotation","The phase sequence determines which way "
   "the rotating field sweeps"],
  ["14","Full-load current and rated voltage with its connection","Current sets the "
   "cross-section and the voltage with connection confirms the machine suits the supply"]],
 ["A three-phase supply in distributed windings produces a magnetic field that rotates at a speed "
  "fixed by frequency and pole count.",
  "Slip is essential: without relative motion between field and rotor there is no induced current "
  "and no torque.",
  "Mechanical power is the product of torque and speed, so low-speed machines are larger for the "
  "same rating.",
  "Starting current is five to eight times full load because the stationary rotor behaves as a "
  "shorted secondary.",
  "Reduced-voltage starting cuts current but cuts torque by the square of the voltage reduction.",
  "The nameplate states shaft output, not input, and its voltage entry must be read with the "
  "stated connection.",
  "Loading a generator produces an opposing field, so electrical output must be matched by "
  "mechanical input."],
 [["Synchronous speed","n\u209b = 120 f / p","Three-phase machine"],
  ["Fractional slip","s = (n\u209b \u2212 n\u1d63)/n\u209b","Induction machine"],
  ["Rotor speed","n\u1d63 = n\u209b(1 \u2212 s)","Induction machine"],
  ["Rotor frequency","f\u1d63 = s f","Induction machine"],
  ["Mechanical power","P = 2\u03c0 n T / 60","n in rev/min"],
  ["Torque from power","T = 9.55 P / n","n in rev/min, P in watts"],
  ["Three-phase power","P = \u221a3 V_L I_L cos\u03c6","Balanced load"],
  ["Generated frequency","f = p n / 120","Synchronous generator"]],
 [["Synchronous speed","The rotational speed of the magnetic field, set by frequency and poles"],
  ["Slip","The fractional difference between synchronous and rotor speed"],
  ["Breakdown torque","The maximum torque a machine can develop before stalling"],
  ["Direct on line","Starting by applying full supply voltage through a single contactor"],
  ["Star-delta","A starting method that reconnects the windings to reduce starting current"],
  ["Duty type","The nameplate classification of permitted running and starting pattern"],
  ["Single phasing","Operation with one supply conductor lost, producing severe imbalance"]],
 "Machines and transformers rely on magnetic coupling. The next chapter turns to semiconductors, "
 "where conduction is controlled within a solid material rather than by a field, beginning with "
 "the diode and the rectifier circuits built from it.",
)
