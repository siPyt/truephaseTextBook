# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH12=mkch(12,"Diodes and rectification",
 "One-way conduction, and converting alternating supply to direct",
 "Almost every piece of modern equipment contains a rectifier, because electronics needs direct "
 "supply while distribution provides alternating. The diode is the component that makes the "
 "conversion possible, and understanding its forward drop, its reverse limit and its heat "
 "explains most rectifier failures.",
 ["Describe forward and reverse behaviour of a junction diode and its forward voltage drop.",
  "Identify half-wave, full-wave centre-tapped and bridge rectifier circuits from a schematic.",
  "Compute mean and root-mean-square output values for rectifier circuits.",
  "Select a diode on the basis of forward current and peak reverse voltage.",
  "Explain how a reservoir capacitor reduces ripple and what it does to peak current.",
  "Apply Zener diodes for reference and simple regulation, and compute the series resistor."],
 ("c12_half","A half-wave rectifier. The diode conducts on one polarity only, so the load "
  "receives current during alternate half-cycles.",46),
 [dict(h2="The junction diode",
   paras=["A diode conducts readily in one direction and blocks in the other. In the forward "
    "direction, conduction begins once the applied voltage exceeds the junction's threshold, "
    "about 0.7 volts for silicon and about 0.3 volts for germanium or a Schottky type. Beyond "
    "that point the forward drop changes only slightly as current rises, so it is usually treated "
    "as a constant.",
    "In the reverse direction only a negligible leakage current flows, until the reverse voltage "
    "reaches the breakdown value. For an ordinary rectifier diode, breakdown is destructive, so "
    "the peak reverse voltage the circuit will impose must be known and the diode rated above it "
    "with a margin."],
   eq=["Forward drop, silicon:  V_F \u2248 0.7 V",
       "Power dissipated in the diode:  P = V_F I_F",
       "Reverse condition:  V_R must stay below the rated peak reverse voltage"],
   panel=("The forward drop is a heat problem, not just a voltage loss",
     ["A diode carrying 8 A at 0.8 V dissipates 6.4 W as heat.",
      "That heat must leave through the package and its mounting.",
      "A rectifier without adequate heatsinking fails thermally, not electrically.",
      "Schottky types drop less and run cooler, at the cost of higher leakage."])),
  dict(h2="Half-wave rectification",
   paras=["A single diode in series with the load passes current on one polarity only. The load "
    "therefore receives half-cycles separated by gaps, which gives a low mean output and a large "
    "ripple content. The diode must withstand the full peak supply voltage in reverse during the "
    "blocked half-cycles.",
    "Half-wave rectification is cheap and occasionally adequate, but it wastes half of each "
    "cycle, it draws current from the supply in one direction only, and it needs a much larger "
    "reservoir capacitor for the same ripple. It is used mainly in very low-power circuits."],
   eq=["V_mean = 0.318 V_pk      V_rms = 0.5 V_pk",
       "Ripple frequency = supply frequency",
       "Peak reverse voltage across the diode = V_pk"]),
  dict(h2="Full-wave and bridge rectification",
   paras=["A full-wave rectifier uses both half-cycles. With a centre-tapped secondary and two "
    "diodes, each diode handles one half-cycle; with four diodes in a bridge, no centre tap is "
    "needed and the whole secondary winding is used on every half-cycle.",
    "The bridge is almost always preferred. It makes better use of the transformer, and although "
    "two diodes conduct in series so the total forward drop doubles, the output is higher than "
    "the centre-tapped arrangement gives from the same winding. The ripple frequency is twice the "
    "supply frequency, which makes smoothing easier."],
   eq=["V_mean = 0.637 V_pk      V_rms = 0.707 V_pk",
       "Ripple frequency = 2 \u00d7 supply frequency",
       "Bridge output \u2248 V_pk \u2212 2 V_F      Centre-tap output \u2248 V_pk \u2212 V_F"],
   table=(["Property","Half wave","Centre-tapped full wave","Bridge"],
     [["Diodes required","1","2","4"],
      ["Mean output","0.318 V_pk","0.637 V_pk","0.637 V_pk"],
      ["Ripple frequency","Supply frequency","Twice supply","Twice supply"],
      ["Forward drops in path","One","One","Two"],
      ["Transformer utilisation","Poor","Half winding per half-cycle","Full winding"],
      ["Peak reverse voltage","V_pk","2 V_pk per diode","V_pk"]],None),
   fig=("c12_bridge","A bridge rectifier. Two diodes conduct on each half-cycle, so current "
     "through the load is always in the same direction.",46)),
  dict(h2="Smoothing and the reservoir capacitor",
   paras=["Rectified output is unidirectional but far from steady. A capacitor across the load "
    "charges to near the peak and then supplies the load during the intervals when the rectifier "
    "output falls below the capacitor voltage, so the output becomes a nearly steady voltage with "
    "a small sawtooth ripple superimposed.",
    "The price of smoothing is current. The capacitor recharges only during a short period near "
    "each peak, so the peak repetitive current through the diodes and the transformer is many "
    "times the mean load current. Larger capacitors give less ripple but shorter, higher charging "
    "pulses, which is why oversizing a reservoir capacitor can destroy the rectifier it was "
    "meant to protect."],
   eq=["Ripple voltage \u2248 I_load / (f_ripple C)",
       "Larger C or higher f_ripple gives less ripple",
       "Peak diode current \u226b mean load current"],
   panel=("Why a bigger capacitor is not always better",
     ["Smoothing works by recharging the capacitor in a brief pulse near each peak.",
      "Doubling the capacitance roughly halves the ripple but shortens the charging window.",
      "Peak repetitive diode current and transformer heating both rise.",
      "Check the diode's repetitive peak current rating, not only its mean rating."])),
  dict(h2="Zener diodes and simple regulation",
   paras=["A Zener diode is designed to break down at a specified reverse voltage without damage, "
    "and to hold that voltage nearly constant over a wide current range. Operated in reverse with "
    "a series resistor to limit the current, it provides a stable reference or a simple regulated "
    "supply for a light load.",
    "The series resistor must be chosen so that enough current flows to keep the Zener in "
    "breakdown at the minimum input voltage and maximum load current, while the Zener's "
    "dissipation stays within rating at the maximum input voltage and minimum load current. Those "
    "two conditions bracket the acceptable resistor values."],
   eq=["R = (V_in \u2212 V_Z) / (I_Z + I_load)",
       "P_Z = V_Z I_Z      P_R = (V_in \u2212 V_Z) I_total",
       "Worst case for the Zener: maximum V_in with no load"],
   fig=("c12_zener","A Zener diode as a shunt regulator. The series resistor sets the total "
     "current and the Zener absorbs whatever the load does not take.",46),
   bh="Selecting a Zener regulator",
   bullets=["Operate the Zener in reverse; it is not a forward conduction device.",
     "Always include the series resistor, or the Zener will be destroyed.",
     "Check dissipation at maximum input with the load disconnected.",
     "Keep the Zener current above a few milliamperes for a stable voltage.",
     "Use a Zener as a reference for larger loads, not as the regulator itself."]),
  dict(h2="Light-emitting diodes and other variants",
   paras=["A light-emitting diode is a forward-conducting junction that emits light, with a "
    "forward drop between about 1.8 and 3.4 volts depending on colour. Like any diode it has no "
    "internal current limiting, so a series resistor or a constant-current supply is mandatory; "
    "connecting one directly across a supply destroys it immediately.",
    "Other variants adapt the same junction to specific tasks. Schottky diodes switch fast and "
    "drop less. Photodiodes convert light to current. Varactors present a voltage-dependent "
    "capacitance. Each appears in the symbol set with a distinguishing mark on the standard diode "
    "outline."],
   table=(["Device","Operated","Characteristic exploited","Typical use"],
     [["Rectifier diode","Forward","One-way conduction","Mains rectification"],
      ["Schottky","Forward","Low drop, fast recovery","Switching supplies"],
      ["Zener","Reverse breakdown","Constant breakdown voltage","Reference and regulation"],
      ["Light-emitting","Forward","Light emission","Indication and illumination"],
      ["Photodiode","Reverse","Light-dependent current","Sensing and detection"],
      ["Varactor","Reverse","Voltage-dependent capacitance","Tuning circuits"]],None)),
 ],
 [ex("Half-wave and bridge outputs from the same supply",
   "A transformer secondary gives 24 V root mean square.",
   "The peak value, and the mean output as a half-wave rectifier and as a bridge, allowing for "
   "silicon forward drops.",
   [("Peak voltage","V_pk = 24 \u00d7 1.414 = 33.9 V"),
    ("Half-wave mean, ideal","0.318 \u00d7 33.9 = 10.8 V"),
    ("Bridge mean, ideal","0.637 \u00d7 33.9 = 21.6 V"),
    ("Bridge smoothed output","33.9 \u2212 1.4 = 32.5 V across the capacitor"),
    ("Peak reverse voltage, bridge","About 33.9 V per diode")],
   "The bridge gives twice the mean output of the half-wave circuit from the same winding. Note "
   "that the smoothed output approaches the peak, not the mean, which is why a 24 V winding "
   "produces about 32 V of direct supply."),
  ex("Diode selection for a rectifier",
   "A bridge rectifier supplies 5 A at 30 V direct from a 24 V root-mean-square winding.",
   "The minimum diode ratings and the heat each diode must dissipate.",
   [("Peak reverse voltage present","V_pk = 33.9 V"),
    ("Rating with margin","Select at least 100 V peak reverse voltage"),
    ("Mean current per diode","Each conducts half the time, so about 2.5 A mean"),
    ("Current rating with margin","Select at least 6 A continuous"),
    ("Dissipation per diode","P = 0.8 \u00d7 2.5 = 2 W"),
    ("Total bridge dissipation","About 8 W, requiring a heatsink")],
   "Eight watts in a small bridge package needs real heatsinking. Rating a rectifier only on "
   "voltage and mean current, without checking the thermal path, is the usual reason bridges fail "
   "in service."),
  ex("Reservoir capacitor for a specified ripple",
   "A bridge rectifier on a 50 Hz supply must hold ripple below 1 V peak to peak while supplying "
   "0.8 A.",
   "The minimum reservoir capacitance.",
   [("Ripple frequency","Bridge on 50 Hz gives 100 Hz"),
    ("Rearrange the ripple relation","C = I / (f_ripple V_ripple)"),
    ("Substitute","C = 0.8/(100 \u00d7 1)"),
    ("Result","C = 8000 \u00b5F"),
    ("Practical choice","Fit 10 000 \u00b5F rated above 50 V")],
   "Note how large smoothing capacitors must be for appreciable load current at mains frequency. "
   "A half-wave circuit would need twice this value for the same ripple, because its ripple "
   "frequency is half as high."),
  ex("Series resistor for a Zener regulator",
   "A 5.6 V Zener is to supply a load of up to 20 mA from an input that varies between 12 V and "
   "15 V. A minimum Zener current of 5 mA is required.",
   "The series resistor, and the Zener dissipation in the worst case.",
   [("Worst case for resistor sizing","Minimum input, maximum load"),
    ("Current required","I = 20 + 5 = 25 mA"),
    ("Resistor value","R = (12 \u2212 5.6)/0.025 = 256 \u03a9, so use 240 \u03a9"),
    ("Worst case for the Zener","Maximum input, no load"),
    ("Total current then","I = (15 \u2212 5.6)/240 = 39 mA, all through the Zener"),
    ("Zener dissipation","P = 5.6 \u00d7 0.039 = 0.22 W, so use a 0.5 W device")],
   "The two worst cases are different conditions and both must be checked. The Zener is most "
   "stressed when the load is disconnected, which is exactly the condition a casual bench test "
   "might overlook."),
  ex("Series resistor for a light-emitting diode",
   "A red light-emitting diode with a 2.0 V forward drop is to operate at 15 mA from a 24 V "
   "supply.",
   "The series resistor and its dissipation.",
   [("Voltage across the resistor","24 \u2212 2.0 = 22 V"),
    ("Resistor value","R = 22/0.015 = 1467 \u03a9, so use 1.5 k\u03a9"),
    ("Resulting current","I = 22/1500 = 14.7 mA"),
    ("Resistor dissipation","P = 22 \u00d7 0.0147 = 0.32 W, so use a 0.5 W part")],
   "Most of the supply voltage is dropped across the resistor, which is why the resistor "
   "dissipates far more than the diode. Running indicators from a high supply voltage this way "
   "is wasteful but simple.")],
 lab("diode characteristic, rectifier waveforms and a Zener regulator",
  "Measure the forward characteristic of a silicon diode, display and measure half-wave and "
  "bridge rectifier waveforms with and without smoothing, then test the line and load regulation "
  "of a Zener shunt regulator.",
  ["Silicon diodes, 1 A, four required for the bridge.",
   "Schottky diode and a 5.6 V Zener diode, 0.5 W.",
   "Transformer, 230 V to 24 V, supplied through an isolating transformer.",
   "Resistors: 100 \u03a9, 240 \u03a9, 1.5 k\u03a9 and a 0 to 1 k\u03a9 decade box.",
   "Electrolytic capacitors, 100 \u00b5F and 1000 \u00b5F, rated above 50 V.",
   "Oscilloscope with a differential or isolated input, and two multimeters.",
   "Variable direct supply, 0 to 20 V, current limited."],
  ["With the variable direct supply and a 100 \u03a9 series resistor, raise the voltage across the "
   "silicon diode in small steps and record forward voltage against forward current up to 100 mA.",
   "Repeat for the Schottky diode and note the difference in threshold.",
   "Reverse the silicon diode, apply 10 V, and record the leakage current.",
   "Plot the forward characteristic and identify the threshold voltage from your data.",
   "Build the half-wave rectifier from the transformer secondary into a 1 k\u03a9 load.",
   "Display the load waveform and measure its peak and mean values. Record the ripple frequency.",
   "Add the 100 \u00b5F capacitor across the load and record the new mean output and the ripple.",
   "Replace the single diode with the four-diode bridge and repeat both measurements.",
   "Change the capacitor to 1000 \u00b5F and record the ripple again.",
   "Reduce the load resistance in steps and record how ripple varies with load current.",
   "Build the Zener regulator with the 240 \u03a9 series resistor from the variable direct supply.",
   "Hold the load constant and vary the input from 8 V to 18 V, recording the output each time.",
   "Hold the input at 15 V and vary the load from open circuit to 25 mA, recording the output."],
  ("c12_bridge","The bridge rectifier under test. The oscilloscope is connected across the load "
   "through an isolated input, and the capacitor is switched in and out.",46),
  ["Configuration","Mean output (V)","Ripple (V pk-pk)","Ripple frequency (Hz)","Comment"],
  [["Half wave, no capacitor","","","",""],["Half wave, 100 \u00b5F","","","",""],
   ["Bridge, no capacitor","","","",""],["Bridge, 100 \u00b5F","","","",""],
   ["Bridge, 1000 \u00b5F","","","",""],["Bridge, 1000 \u00b5F, heavy load","","","",""],
   ["Zener output, 8 V input","","","",""],["Zener output, 18 V input","","","",""]],
  ["From your forward characteristic, at what voltage did appreciable conduction begin? Compare "
   "silicon with the Schottky device.",
   "Why was the bridge ripple frequency twice that of the half-wave circuit, and why does that "
   "make smoothing easier?",
   "Compare your smoothed bridge output with the peak of the secondary waveform. Why is it close "
   "to the peak rather than to the unsmoothed mean?",
   "How did ripple change when you increased the capacitance tenfold? Compare the measured change "
   "with the prediction from the ripple relation.",
   "How did ripple change as the load current rose, and why?",
   "Over your input range from 8 V to 18 V, how much did the Zener output vary? Express that as a "
   "percentage.",
   "What happened to the Zener output when the input fell to 8 V, and can you explain it using the "
   "minimum Zener current?",
   "Compute the Zener dissipation at 18 V input with no load and compare it with the device rating."],
  ["Supply the bench through an isolating transformer and a residual current device.",
   "Do not connect an earthed oscilloscope ground to any point of a mains-referenced rectifier; "
   "use an isolated or differential input.",
   "Observe electrolytic capacitor polarity. A reversed electrolytic can rupture.",
   "A smoothing capacitor holds dangerous charge after the supply is removed. Discharge it "
   "through a resistor and prove it dead before touching the circuit.",
   "Check resistor and Zener dissipation before applying power, not after.",
   "Diodes and heatsinks become hot. Allow them to cool before handling."]),
 [["Rectifier diodes fail repeatedly in service","Peak reverse voltage rating too low, or supply "
   "transients exceeding it","Compute the peak reverse voltage present and compare with the "
   "rating","Fit diodes rated well above the peak, and add transient suppression"],
  ["Bridge rectifier runs very hot and eventually fails","Inadequate heatsinking for the forward "
   "drop at the operating current","Compute V_F I_F per diode and measure the package temperature",
   "Fit an adequate heatsink, improve airflow, or use Schottky devices"],
  ["Output voltage sags badly under load","Reservoir capacitance too small, or the transformer is "
   "undersized","Measure the ripple and the output at load against the no-load figure",
   "Increase the capacitance and verify the transformer volt-ampere rating"],
  ["Smoothing capacitor fails after a capacitance upgrade","Peak repetitive diode and capacitor "
   "current rose with the larger capacitor","Measure the charging pulse current with a current "
   "probe","Return to a suitable capacitance or fit components rated for the ripple current"],
  ["Zener regulator output falls below its rated voltage","Input too low or load too high, so "
   "Zener current fell below the breakdown minimum","Measure the current through the series "
   "resistor at the worst case","Reduce the series resistor or raise the input voltage"],
  ["Zener diode overheats with the load disconnected","All the series current diverted through "
   "the Zener at maximum input","Compute V_Z I_Z at maximum input with no load","Select a "
   "higher-wattage Zener or a larger series resistor"],
  ["Light-emitting diode fails instantly on connection","Connected without a series current-"
   "limiting resistor, or reverse connected","Check for a series resistor and confirm polarity",
   "Fit the correct series resistor and observe polarity"]],
 ("c12_zener","Testing the Zener regulator. Line regulation is checked by varying the input; "
  "load regulation by varying the load while the input is held constant.",46),
 ["Compute diode dissipation and provide for the heat before selecting a rectifier package.",
  "Rate the peak reverse voltage with generous margin, because supply transients are not optional "
  "events.",
  "Discharge smoothing capacitors through a resistor and prove dead before working on any "
  "rectifier.",
  "Check the Zener worst case with the load disconnected, which is the condition that destroys it.",
  "Never connect a light-emitting diode without a current-limiting resistor or a constant-current "
  "supply."],
 ["A transformer secondary gives 18 V root mean square. Find the peak value.",
  "Find the ideal mean output of a half-wave rectifier from that secondary.",
  "Find the ideal mean output of a bridge rectifier from the same secondary.",
  "State the ripple frequency of a bridge rectifier on a 60 Hz supply.",
  "Explain why a smoothed bridge output approaches the peak rather than the mean value.",
  "A diode carries 4 A with a 0.75 V forward drop. Find the power it dissipates.",
  "State the number of diodes in a bridge and how many conduct at any instant.",
  "Find the reservoir capacitance for 2 V ripple at 1 A from a bridge on a 50 Hz supply.",
  "Explain why increasing a reservoir capacitor can shorten the life of the rectifier diodes.",
  "A 9.1 V Zener feeds a 25 mA load from 18 V, with 6 mA minimum Zener current. Find the series "
  "resistor.",
  "Find the Zener dissipation above at 18 V with the load disconnected.",
  "State the operating region of a Zener diode and why a series resistor is mandatory.",
  "A 3.0 V light-emitting diode is to run at 20 mA from 12 V. Find the series resistor.",
  "State one advantage and one disadvantage of a Schottky diode compared with a silicon "
  "rectifier diode."],
 [["1","25.5 V","V_pk = 1.414 V_rms"],
  ["2","8.1 V","0.318 V_pk"],
  ["3","16.2 V","0.637 V_pk"],
  ["4","120 Hz","A bridge gives twice the supply frequency"],
  ["5","The capacitor charges to near the peak","It then holds that level between peaks, so the "
   "output follows the peak rather than the average of the unsmoothed waveform"],
  ["6","3 W","P = V_F I_F"],
  ["7","Four diodes; two conduct at a time","Each half-cycle uses a diagonally opposite pair"],
  ["8","5000 \u00b5F","C = I/(f_ripple V_ripple) with f_ripple = 100 Hz"],
  ["9","Peak repetitive current rises","The capacitor recharges in a shorter, higher pulse, "
   "heating the diodes and the transformer"],
  ["10","287 \u03a9, so use 270 \u03a9","R = (18 \u2212 9.1)/0.031"],
  ["11","About 0.3 W","All 33 mA flows through the Zener at 9.1 V"],
  ["12","Reverse breakdown; the resistor limits current","Without it the current is unlimited and "
   "the device is destroyed"],
  ["13","450 \u03a9","R = (12 \u2212 3.0)/0.020"],
  ["14","Lower forward drop; higher reverse leakage","Less heat in conduction but poorer blocking "
   "performance"]],
 ["A diode conducts above its forward threshold and blocks until its reverse breakdown voltage is "
  "reached, where an ordinary rectifier fails.",
  "The forward drop multiplied by the current is heat, and thermal design determines rectifier "
  "reliability.",
  "Half-wave rectification uses one half-cycle; full-wave and bridge circuits use both and double "
  "the mean output.",
  "A bridge needs no centre tap, uses the whole winding, and gives twice the supply ripple "
  "frequency.",
  "A reservoir capacitor raises the output to near the peak and reduces ripple, but raises peak "
  "repetitive diode current.",
  "A Zener diode operated in reverse breakdown with a series resistor provides a reference or "
  "simple regulation, with its worst case at maximum input and no load.",
  "Every light-emitting diode requires external current limiting."],
 [["Silicon forward drop","V_F \u2248 0.7 V","Conducting junction diode"],
  ["Diode dissipation","P = V_F I_F","Forward conduction"],
  ["Half-wave mean","V_mean = 0.318 V_pk","Resistive load, no smoothing"],
  ["Full-wave mean","V_mean = 0.637 V_pk","Resistive load, no smoothing"],
  ["Smoothed output","V \u2248 V_pk \u2212 n V_F","With reservoir capacitor, n diodes in path"],
  ["Ripple voltage","V_ripple \u2248 I/(f_ripple C)","Capacitor-smoothed rectifier"],
  ["Zener series resistor","R = (V_in \u2212 V_Z)/(I_Z + I_load)","Shunt regulator"],
  ["Indicator resistor","R = (V_supply \u2212 V_F)/I_F","Light-emitting diode circuit"]],
 [["Forward drop","The nearly constant voltage across a conducting diode"],
  ["Peak reverse voltage","The highest reverse voltage a diode must withstand without breakdown"],
  ["Ripple","The alternating component remaining on a rectified and smoothed output"],
  ["Reservoir capacitor","The capacitor that holds the output near the peak between rectifier "
   "pulses"],
  ["Zener voltage","The specified reverse breakdown voltage a Zener diode maintains"],
  ["Line regulation","The change in output caused by a change in input voltage"],
  ["Load regulation","The change in output caused by a change in load current"]],
 "A diode conducts or blocks according to the polarity applied to it, with no third terminal to "
 "intervene. Adding that control terminal gives the transistor, which can switch and amplify, "
 "and which the next chapter examines.",
)
