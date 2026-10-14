# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH8=mkch(8,"Resonance and filters",
 "The frequency where reactances cancel, and the circuits built from that effect",
 "At one particular frequency an inductive and a capacitive reactance are equal and cancel. That "
 "single fact produces the sharpest voltage rises you will ever measure in a passive circuit, "
 "and it is the basis of every tuned circuit and passive filter.",
 ["Compute the resonant frequency of a series or parallel combination.",
  "Describe what happens to impedance, current and element voltages at series resonance.",
  "Compute the quality factor and the bandwidth of a resonant circuit.",
  "Identify low-pass, high-pass, band-pass and band-stop arrangements from a schematic.",
  "Compute the cut-off frequency of a single-stage resistive-capacitive filter."],
 ("c8_series_res","A series resonant circuit. At resonance the inductive and capacitive "
  "reactances cancel, leaving only the resistance to limit the current.",46),
 [dict(h2="The resonant frequency",
   paras=["Inductive reactance rises with frequency while capacitive reactance falls, so there is "
    "exactly one frequency at which the two are equal. Setting them equal and solving gives the "
    "resonant frequency, which depends only on the inductance and the capacitance, not on the "
    "resistance present.",
    "That independence from resistance is worth noting: resistance determines how sharp the "
    "resonance is and how large the element voltages become, but it does not move the resonant "
    "frequency itself."],
   eq=["At resonance:  X_L = X_C",
       "2\u03c0 f L = 1/(2\u03c0 f C)",
       "f\u2080 = 1 / (2\u03c0 \u221a(L C))"]),
  dict(h2="Series resonance: minimum impedance, maximum current",
   paras=["In a series circuit the two reactances cancel at resonance, so the impedance falls to "
    "the resistance alone. This is the minimum impedance the circuit can present, so the current "
    "reaches its maximum and the voltage and current come into phase.",
    "The element voltages at resonance can greatly exceed the supply voltage. Each reactance "
    "carries the resonant current and its full reactance, which may be many times the resistance. "
    "The two large voltages are in opposition and cancel as far as the supply is concerned, but "
    "each is individually real and will stress insulation and instruments."],
   eq=["Z = R      I = V / R      \u03c6 = 0",
       "V_L = I X_L = Q V      V_C = I X_C = Q V"],
   panel=("Series resonance produces genuine voltage magnification",
     ["A circuit with Q = 20 supplied at 24 V develops 480 V across each reactive element.",
      "The two cancel at the supply terminals, so a supply-side meter shows nothing unusual.",
      "Measure across the individual elements before assuming a circuit is low voltage."])),
  dict(h2="Quality factor and bandwidth",
   paras=["The quality factor expresses how sharp a resonance is: it is the ratio of reactance at "
    "resonance to the series resistance. A high quality factor means a narrow response and large "
    "voltage magnification; a low one means a broad response and little magnification.",
    "The bandwidth is the span of frequencies over which the response stays within the half-power "
    "points, and it equals the resonant frequency divided by the quality factor. A tuned circuit "
    "must therefore trade selectivity against bandwidth, which is the central compromise in "
    "filter design."],
   eq=["Q = X_L / R = (1/R)\u221a(L/C)",
       "BW = f\u2080 / Q",
       "Half-power points at 0.707 of maximum"],
   fig=("c8_parallel_res","A parallel resonant circuit. At resonance it presents maximum "
     "impedance, so it blocks rather than passes the resonant frequency.",46)),
  dict(h2="Parallel resonance: maximum impedance",
   paras=["A parallel inductor and capacitor behave in the opposite way. At resonance the two "
    "branch currents are equal and opposite, so they circulate between the elements and the "
    "supply sees almost no current. The impedance is therefore at a maximum.",
    "This is why a parallel tuned circuit is used to reject a frequency rather than to pass it, "
    "and why the circulating current inside a parallel resonant loop can be far larger than the "
    "current drawn from the supply. In power systems an accidental parallel resonance between "
    "correction capacitors and system inductance can amplify a harmonic severely."],
   table=(["Property","Series resonance","Parallel resonance"],
     [["Impedance at f\u2080","Minimum, equal to R","Maximum"],
      ["Current from supply","Maximum","Minimum"],
      ["Magnified quantity","Element voltages","Circulating branch currents"],
      ["Typical use","Accept a frequency","Reject a frequency"],
      ["Phase at f\u2080","Zero","Zero"]],None)),
  dict(h2="Passive filters",
   paras=["A filter is a circuit whose response depends deliberately on frequency. A single "
    "resistor and capacitor make a low-pass filter if the output is taken across the capacitor, "
    "and a high-pass filter if it is taken across the resistor. The cut-off frequency is where "
    "the reactance equals the resistance, at which point the output has fallen to 0.707 of the "
    "input and the power to half.",
    "Combining a low-pass and a high-pass stage produces a band-pass response; a series or "
    "parallel resonant circuit does the same job more sharply. Band-stop or notch responses are "
    "built the same way with the elements interchanged."],
   eq=["f_c = 1 / (2\u03c0 R C)",
       "At f_c the output is 0.707 of input, that is \u22123 dB"],
   fig=("c8_filters","Low-pass and high-pass arrangements from the same two components. The "
     "output terminals determine which response you get.",46),
   bh="Identifying a filter from the schematic",
   bullets=["Output across the capacitor in a series resistor-capacitor pair: low pass.",
     "Output across the resistor in the same pair: high pass.",
     "Series resonant branch feeding the output: band pass.",
     "Parallel resonant branch across the output: band stop, or notch.",
     "Inductor in the series path with a capacitor to the reference: low pass with a steeper slope."]),
 ],
 [ex("Resonant frequency and quality factor",
   "A series circuit has L = 100 mH, C = 100 nF and R = 50 "+OH+".",
   "The resonant frequency, the reactance at resonance, the quality factor and the bandwidth.",
   [("Resonant frequency","f\u2080 = 1/(2\u03c0\u221a(0.1 \u00d7 100\u00d710\u207b\u2079)) = 1592 Hz"),
    ("Reactance at resonance","X_L = 2\u03c0 \u00d7 1592 \u00d7 0.1 = 1000 "+OH),
    ("Check the capacitive reactance","X_C = 1/(2\u03c0 \u00d7 1592 \u00d7 100\u00d710\u207b\u2079) = 1000 "+OH+" \u2713"),
    ("Quality factor","Q = 1000/50 = 20"),
    ("Bandwidth","BW = 1592/20 = 79.6 Hz")],
   "Both reactances come to 1000 "+OH+" at the computed frequency, which confirms the resonant "
   "frequency. A quality factor of 20 is a sharp resonance."),
  ex("Voltage magnification at series resonance",
   "The circuit above is supplied at 10 V at its resonant frequency.",
   "The current and the voltage across the inductor and the capacitor.",
   [("Impedance at resonance","Z = R = 50 "+OH),
    ("Current","I = 10/50 = 0.2 A"),
    ("Inductor voltage","V_L = 0.2 \u00d7 1000 = 200 V"),
    ("Capacitor voltage","V_C = 0.2 \u00d7 1000 = 200 V"),
    ("Supply-side sum","200 \u2212 200 = 0, leaving 10 V across R")],
   "The 200 V across each element is twenty times the supply, equal to Q \u00d7 V. A meter at the "
   "supply terminals would show only 10 V, which is why this hazard is easy to miss."),
  ex("Cut-off frequency of a resistive-capacitive filter",
   "A filter uses R = 1.6 k"+OH+" and C = 100 nF, with the output taken across the capacitor.",
   "The filter type, the cut-off frequency and the output at one tenth and ten times that "
   "frequency.",
   [("Filter type","Output across the capacitor, so low pass"),
    ("Cut-off frequency","f_c = 1/(2\u03c0 \u00d7 1600 \u00d7 100\u00d710\u207b\u2079) = 995 Hz"),
    ("At 99.5 Hz, a decade below","X_C \u226b R, so output \u2248 input, near 0 dB"),
    ("At 9.95 kHz, a decade above","X_C \u226a R, so output \u2248 input/10, near \u221220 dB"),
    ("At the cut-off itself","Output = 0.707 of input, that is \u22123 dB")],
   "A single stage rolls off at 20 dB per decade, so the response a decade above cut-off is one "
   "tenth of the input. Taking the output across the resistor instead would give a high-pass "
   "response with the same cut-off frequency.")],
 lab("locating resonance and plotting a filter response",
  "Find the resonant frequency of a series combination by measurement, observe the voltage "
  "magnification across the reactive elements, then plot the response of a single-stage filter "
  "and locate its cut-off frequency from the data.",
  ["Signal generator, sine output, 100 Hz to 100 kHz, with a stated output amplitude.",
   "Inductor, 100 mH, with its resistance measured.",
   "Capacitors, 100 nF and 10 nF, film type.",
   "Resistors, 50 "+OH+", 1.6 k"+OH+", 0.25 W.",
   "Oscilloscope and a true rms multimeter."],
  ["Measure and record the inductor's resistance and the actual component values.",
   "Compute the expected resonant frequency before building the circuit.",
   "Build the series combination of L, C and the 50 "+OH+" resistor across the generator.",
   "Set the generator to 2 V rms and keep that amplitude constant throughout the sweep.",
   "Sweep the frequency and find the frequency at which the voltage across the resistor is "
   "maximum. That is resonance.",
   "At resonance, measure the voltage across the inductor and across the capacitor separately.",
   "Find the two frequencies at which the resistor voltage falls to 0.707 of its peak, and "
   "compute the bandwidth.",
   "Rebuild as a low-pass filter with the 1.6 k"+OH+" resistor and the 100 nF capacitor.",
   "Measure the output across the capacitor at frequencies from 100 Hz to 20 kHz and tabulate.",
   "Identify from your data the frequency at which the output is 0.707 of the input."],
  ("c8_series_res","The resonance test circuit. The resistor voltage is proportional to the "
   "current, so its maximum locates resonance.",46),
  ["Frequency (Hz)","V across R","V across L","V across C","Comment"],
  [["500","","","",""],["1000","","","",""],["1592 (predicted f\u2080)","","","",""],
   ["2000","","","",""],["4000","","","",""],["8000","","","",""]],
  ["How close was the measured resonant frequency to your prediction? Account for the difference "
   "using the measured component values.",
   "What was the ratio of the inductor voltage at resonance to the supply voltage? Compare it "
   "with your computed quality factor.",
   "Compute the bandwidth from your half-power frequencies and compare with f\u2080 divided by Q.",
   "Replace the 100 nF with 10 nF on paper and predict the new resonant frequency. By what factor "
   "should it change?",
   "From your filter data, at what rate does the output fall above cut-off? Express it in decibels "
   "per decade."],
  ["Keep the generator output at or below 5 V rms.",
   "Element voltages at resonance can be many times the supply voltage. Set the oscilloscope "
   "range accordingly before probing the inductor or capacitor.",
   "Check resistor dissipation at the resonant current before sweeping.",
   "Reduce the generator amplitude to minimum before changing any connection."]),
 [["Measured resonant frequency differs from prediction","Component tolerance, especially the "
   "inductor","Measure L and C and recompute","Use measured values; inductors are often 10\u201320 % out"],
  ["Resonance peak is broad and shallow","Low quality factor from high series resistance",
   "Compute Q from the measured reactance and resistance","Reduce the series resistance or use a "
   "lower-loss inductor"],
  ["Instrument damaged while probing a resonant circuit","Element voltage magnification exceeded "
   "the instrument range","Compute Q V before probing the reactive elements","Set the range for "
   "Q times the supply voltage, not the supply voltage"],
  ["Correction capacitors overheat on a distorted supply","Parallel resonance between the "
   "capacitors and system inductance near a harmonic","Measure the capacitor current and its "
   "waveform","Fit detuning reactors to shift the resonance away from a harmonic"],
  ["Filter passes more high frequency than expected","Stray capacitance bypassing the series "
   "element, or the output taken at the wrong node","Check the output node against the drawing "
   "and shorten leads","Correct the connection; reduce lead length and loop area"],
  ["Notch filter does not reject the target frequency","Resonant frequency has drifted with "
   "temperature or component ageing","Sweep and locate the actual notch frequency","Retune, or "
   "specify components with tighter temperature coefficients"]],
 ("c8_filters","Measuring a filter response. The output is recorded against frequency at constant "
  "input amplitude, and the cut-off is read at the 0.707 point.",46),
 ["Compute Q V before probing a resonant circuit; the element voltages, not the supply voltage, "
  "set the instrument range you need.",
  "Use measured inductance and capacitance for any resonance prediction, because tolerances are wide.",
  "Hold the input amplitude constant across a frequency sweep, or the response curve is meaningless.",
  "Treat an unexplained capacitor failure in a corrected installation as a possible harmonic "
  "resonance."],
 ["Find the resonant frequency of 50 mH with 200 nF.",
  "Find the resonant frequency of 10 mH with 1 \u00b5F.",
  "A series circuit resonates at 2 kHz with X_L = 800 "+OH+" and R = 40 "+OH+". Find Q and the bandwidth.",
  "The circuit above is supplied at 12 V at resonance. Find the inductor voltage.",
  "State what happens to the impedance, current and phase angle of a series circuit at resonance.",
  "State what happens to the impedance and supply current of a parallel resonant circuit at resonance.",
  "Find the cut-off frequency of a 10 k"+OH+" resistor with a 10 nF capacitor.",
  "A filter takes its output across the resistor of a series resistor-capacitor pair. State the "
  "filter type.",
  "Explain why resonance frequency is independent of the series resistance.",
  "A correction capacitor bank resonates with system inductance at 250 Hz on a 50 Hz system. "
  "State which harmonic that is and why it matters."],
 [["1","1592 Hz","f\u2080 = 1/(2\u03c0\u221a(LC))"],
  ["2","1592 Hz","The LC product is identical to question 1"],
  ["3","Q = 20; BW = 100 Hz","Q = X_L/R, then BW = f\u2080/Q"],
  ["4","240 V","V_L = Q V = 20 \u00d7 12"],
  ["5","Impedance minimum, current maximum, phase zero","The reactances cancel, leaving R alone"],
  ["6","Impedance maximum, supply current minimum","Branch currents are equal and opposite and "
   "circulate internally"],
  ["7","1592 Hz","f_c = 1/(2\u03c0RC)"],
  ["8","High pass","The resistor voltage rises as capacitive reactance falls with frequency"],
  ["9","Resonance requires only X_L = X_C","Neither reactance depends on R, so R affects sharpness "
   "but not the frequency"],
  ["10","The fifth harmonic; amplification","Harmonic current from electronic loads is amplified "
   "by the resonance, overheating the capacitors"]],
 ["Resonance occurs at the single frequency where inductive and capacitive reactances are equal, "
  "and depends only on L and C.",
  "Series resonance gives minimum impedance and maximum current; parallel resonance gives maximum "
  "impedance and minimum supply current.",
  "The quality factor sets both the sharpness and the voltage magnification, and bandwidth is "
  "f\u2080 divided by Q.",
  "Element voltages at series resonance can be many times the supply voltage and are a genuine "
  "hazard.",
  "A single resistor-capacitor stage gives a low-pass or high-pass response depending on which "
  "element the output is taken across, with cut-off at 1/(2\u03c0RC).",
  "Accidental resonance between correction capacitors and system inductance amplifies harmonics "
  "and destroys capacitors."],
 [["Resonant frequency","f\u2080 = 1/(2\u03c0\u221a(LC))","Series or parallel LC"],
  ["Resonance condition","X_L = X_C","Defines f\u2080"],
  ["Quality factor","Q = X_L/R","Series resonant circuit"],
  ["Bandwidth","BW = f\u2080/Q","Between half-power points"],
  ["Voltage magnification","V_L = V_C = Q V","At series resonance"],
  ["Filter cut-off","f_c = 1/(2\u03c0RC)","Single-stage RC filter"]],
 [["Resonance","The condition where inductive and capacitive reactances cancel"],
  ["Quality factor","The ratio of reactance to resistance at resonance, setting sharpness"],
  ["Bandwidth","The frequency span between the half-power points"],
  ["Cut-off frequency","Where a filter's output has fallen to 0.707 of its input"],
  ["Detuning reactor","An inductor added to shift a capacitor bank's resonance away from a harmonic"]],
 "Resonance and filtering depend on inductance, which is produced by magnetic fields. The next "
 "chapter examines magnetism directly: how fields are produced, how they produce force and "
 "voltage, and how magnetic circuits are analysed.",
)
