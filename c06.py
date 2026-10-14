# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES
from mk import mkch,lab,ex

CH6=mkch(6,"Alternating current fundamentals",
 "Waveforms, frequency, phase and the meaning of a root-mean-square value",
 "Supply systems alternate, so every quantity you measure on them is an average of a changing "
 "value. Knowing exactly which average your meter reports, and what phase means, is the "
 "difference between a correct reading and a plausible wrong one.",
 ["Describe a sinusoid by amplitude, frequency, period and phase.",
  "Convert between peak, peak-to-peak, average and root-mean-square values.",
  "Explain why the root-mean-square value is the one that determines heating.",
  "Read period and amplitude from an oscilloscope display and compute frequency.",
  "Recognise when a meter's averaging method will give a misleading result."],
 ("c6_ac","A sinusoidal supply driving a resistive load. The instantaneous values change "
  "continuously, so a single figure must be defined before it can be quoted.",44),
 [dict(h2="Describing a sinusoid",
   paras=["A sinusoidal voltage is fully described by three numbers: its amplitude, its frequency "
    "and its phase relative to some reference. The period is the time for one complete cycle and "
    "is the reciprocal of the frequency. At 60 Hz the period is 16.67 ms; at 50 Hz it is 20 ms.",
    "Phase expresses where in its cycle a waveform sits compared with another of the same "
    "frequency. It is meaningless to speak of the phase of a single isolated waveform, just as it "
    "is meaningless to speak of a voltage at a single point: both need a reference."],
   eq=["v(t) = V_peak sin(2\u03c0 f t + \u03c6)",
       "T = 1 / f          \u03c9 = 2\u03c0 f"]),
  dict(h2="Peak, average and root-mean-square",
   paras=["The peak value is the largest instantaneous value. The peak-to-peak value is twice "
    "that for a symmetrical wave. The average over a full cycle of a symmetrical alternating wave "
    "is zero, which is why the rectified average is quoted instead. None of these is the value "
    "that determines heating.",
    "The root-mean-square value is defined as the equivalent direct voltage that would produce "
    "the same heating in a resistance. For a sinusoid it is the peak divided by the square root "
    "of two, about 0.707 of peak. Because heating depends on the square of the instantaneous "
    "value, this is the only average that predicts power correctly."],
   eq=["V_rms = V_peak / \u221a2 = 0.707 V_peak",
       "V_peak = 1.414 V_rms",
       "V_avg(rectified) = 0.637 V_peak"],
   fig=("c6_rms","Peak, peak-to-peak and root-mean-square values of a sinusoid. Only the "
     "root-mean-square value predicts heating in a resistance.",44),
   table=(["Quantity","For a sinusoid","At 120 V rms","At 230 V rms"],
     [["Root-mean-square","V_rms","120 V","230 V"],
      ["Peak","1.414 V_rms","170 V","325 V"],
      ["Peak to peak","2.828 V_rms","339 V","651 V"],
      ["Rectified average","0.900 V_rms","108 V","207 V"],
      ["Form factor","1.11","\u2014","\u2014"],
      ["Crest factor","1.414","\u2014","\u2014"]],None)),
  dict(h2="Why the root-mean-square value is the useful one",
   paras=["Instantaneous power in a resistance is the square of the instantaneous voltage divided "
    "by the resistance. Averaging that over a cycle requires the mean of the squared voltage, and "
    "taking the square root of that mean gives a voltage that can be used in the familiar DC "
    "power formulas. That is precisely the definition of root-mean-square.",
    "The practical consequence is that all the DC power relationships work unchanged on "
    "alternating quantities provided every value used is a root-mean-square value. Mixing a peak "
    "voltage with a root-mean-square current is one of the most common errors in AC calculation."],
   eq=["P = V_rms I_rms (resistive load)",
       "P = V_rms\u00b2 / R = I_rms\u00b2 R"],
   panel=("The rule that prevents most AC arithmetic errors",
     ["Convert everything to root-mean-square before any power calculation.",
      "Use peak values only for insulation stress and semiconductor voltage ratings.",
      "Never multiply a peak voltage by a root-mean-square current."])),
  dict(h2="What your meter actually measures",
   paras=["An averaging meter rectifies the waveform, measures the average and multiplies by 1.11 "
    "to display a root-mean-square value. This is correct only for an undistorted sinusoid. On a "
    "distorted waveform, such as the current drawn by electronic loads, the same meter can read "
    "substantially low.",
    "A true root-mean-square meter squares, averages and takes the root of the actual waveform, "
    "so it is correct regardless of shape, within its crest factor limit. On modern installations "
    "with electronic loads a true root-mean-square instrument is not a refinement but a "
    "requirement."],
   table=(["Meter type","Reads correctly on","Error on distorted current","When to use"],
     [["Averaging, rms calibrated","Clean sinusoids","Typically 10\u201340 % low","Simple linear loads"],
      ["True rms","Any waveform within crest factor","Small","Electronic loads, drives, lighting"],
      ["Peak reading","Peak value directly","Not applicable","Insulation and device ratings"],
      ["Clamp, averaging","Clean sinusoidal current","Can be large","Motor circuits only"]],None),
   fig=("c6_scope","Reading a waveform on an oscilloscope. Period is read horizontally and "
     "amplitude vertically, and the frequency follows from the period.",46)),
  dict(h2="Reading an oscilloscope",
   paras=["An oscilloscope displays instantaneous voltage against time, so it shows the shape "
    "that a meter reduces to a single number. Read the period by counting horizontal divisions "
    "for one complete cycle and multiplying by the time base setting, then invert for frequency. "
    "Read amplitude by counting vertical divisions and multiplying by the volts-per-division "
    "setting.",
    "The oscilloscope is the only instrument that reveals waveform distortion, clipping, notching "
    "and transients. When a meter reading is inconsistent with expectation, looking at the "
    "waveform usually explains it immediately."],
   numbered=["Set the coupling to DC unless you specifically want to remove the offset.",
     "Adjust the time base so two or three cycles fill the screen.",
     "Count divisions for one full cycle and multiply by the time base to get the period.",
     "Invert the period to obtain the frequency.",
     "Count peak-to-peak divisions and multiply by the volts per division.",
     "Divide the peak-to-peak value by 2.828 to obtain the root-mean-square value of a sinusoid."]),
 ],
 [ex("Peak and root-mean-square conversion",
   "An oscilloscope shows a sinusoid of 340 V peak to peak at a period of 16.67 ms.",
   "The peak value, the root-mean-square value and the frequency.",
   [("Peak from peak to peak","V_peak = 340/2 = 170 V"),
    ("Root-mean-square value","V_rms = 170/1.414 = 120.2 V"),
    ("Frequency from period","f = 1/0.01667 = 60 Hz")],
   "120 V at 60 Hz is a standard North American supply, which confirms the reading. Note that "
   "insulation must withstand 170 V peak, not 120 V."),
  ex("Power in a resistive AC load",
   "A 2.4 k"+OH+" heating element is supplied at 230 V rms.",
   "The current, the power and the peak voltage the element insulation sees.",
   [("Current from Ohm's law in rms terms","I = 230/2400 = 95.8 mA"),
    ("Power","P = V I = 230 \u00d7 0.0958 = 22.0 W"),
    ("Check by the squared form","P = 230\u00b2/2400 = 22.0 W \u2713"),
    ("Peak voltage","V_peak = 230 \u00d7 1.414 = 325 V")],
   "Both power routes agree because every value used was root-mean-square. The 325 V peak is the "
   "figure that matters for insulation rating."),
  ex("An averaging meter on a distorted current",
   "An electronic load draws a distorted current. A true rms clamp reads 6.4 A; an averaging "
   "clamp reads 4.9 A on the same conductor.",
   "The error of the averaging meter and the consequence for a 230 V supply calculation.",
   [("Absolute difference","6.4 \u2212 4.9 = 1.5 A"),
    ("Error relative to the true value","1.5/6.4 \u00d7 100 = 23 % low"),
    ("Apparent power from the true reading","S = 230 \u00d7 6.4 = 1472 VA"),
    ("Apparent power from the averaging reading","S = 230 \u00d7 4.9 = 1127 VA")],
   "The averaging meter understates the loading by about 345 VA, which could lead to an "
   "undersized conductor or an overloaded circuit being declared acceptable.")],
 lab("measuring peak and root-mean-square values of an alternating supply",
  "Compare oscilloscope-derived peak values with meter-displayed root-mean-square values on both "
  "a clean sinusoid and a deliberately distorted waveform, and quantify the difference between "
  "averaging and true rms instruments.",
  ["Signal generator capable of sine, square and triangle output at 50\u20131000 Hz.",
   "Oscilloscope with calibrated probes.",
   "One averaging multimeter and one true rms multimeter.",
   "Load resistor, 1 k"+OH+" 1 W, and a breadboard.",
   "Optionally a low-voltage transformer output for a mains-frequency sinusoid."],
  ["Set the generator to a 1 V rms sinusoid at 100 Hz into the 1 k"+OH+" load.",
   "Measure the peak-to-peak voltage on the oscilloscope and compute the root-mean-square value.",
   "Record both meter readings and compare all three figures.",
   "Measure the period on the oscilloscope and compute the frequency; compare with the generator "
   "setting.",
   "Switch the generator to a square wave of the same peak amplitude and repeat all readings.",
   "Switch to a triangle wave and repeat again.",
   "Tabulate the ratio of each meter reading to the oscilloscope-derived true value for each shape.",
   "Return the generator to a low amplitude before disconnecting."],
  ("c6_scope","The measurement setup. The oscilloscope and both meters observe the same waveform "
   "across the same load.",46),
  ["Waveform","Scope V p-p","True rms computed","Averaging meter","True rms meter"],
  [["Sine 100 Hz","","","",""],["Square 100 Hz","","","",""],["Triangle 100 Hz","","","",""],
   ["Sine 1 kHz","","","",""],["Square 1 kHz","","","",""],["Triangle 1 kHz","","","",""]],
  ["For which waveform did the averaging meter agree best with the computed value? Explain why.",
   "For a square wave the true root-mean-square value equals the peak. Did your true rms meter "
   "confirm this?",
   "Compute the form factor of each waveform from your data and compare with the theoretical "
   "values of 1.11 for sine and 1.00 for square.",
   "At 1 kHz, did either meter's accuracy change? Check both meters' stated bandwidth.",
   "A distorted load current reads 23 % low on an averaging clamp. Describe one installation "
   "decision this error could invalidate."],
  ["Keep all signal levels below 10 V; this activity requires no hazardous voltages.",
   "If a mains-derived transformer output is used, treat the primary side as live and do not "
   "probe it.",
   "Check the oscilloscope probe attenuation setting before trusting an amplitude reading.",
   "Confirm both meters are set to AC volts, not DC, before recording."]),
 [["Meter reads low on an electronic load","Averaging meter used on a distorted current",
   "Compare against a true rms instrument on the same conductor","Use a true rms meter and "
   "re-record the loading"],
  ["Oscilloscope amplitude is ten times wrong","Probe attenuation setting does not match the "
   "instrument setting","Check the probe switch against the channel menu","Set both to the same "
   "attenuation and re-measure"],
  ["Waveform shows flattened peaks","Supply clipping, or the instrument input is overdriven",
   "Reduce the vertical sensitivity and re-observe","Investigate the supply; reduce the probe "
   "loading"],
  ["Frequency reads half or double the expected value","Triggering on the wrong edge or counting "
   "half a cycle","Count a full cycle between identical points on the trace","Re-measure the "
   "period between two matching zero crossings"],
  ["AC voltage reading drifts while the load is steady","Meter on the wrong range, or supply "
   "voltage genuinely fluctuating","Log readings over a minute and compare with another meter",
   "Identify whether the instrument or the supply is varying"],
  ["Calculated power far exceeds the measured value","Peak and root-mean-square values mixed in "
   "the calculation","Recheck every value used for which average it represents","Convert all "
   "quantities to root-mean-square and recalculate"]],
 ("c6_rms","Distinguishing the averages. Peak matters for insulation, root-mean-square matters "
  "for heating, and the rectified average matters only to the meter's internal circuit.",44),
 ["Write which average a number is whenever you record it; \u201c170 V\u201d is ambiguous and "
  "\u201c170 V peak\u201d is a measurement.",
  "Use a true rms instrument on any circuit containing electronic loads, drives or modern lighting.",
  "Check probe attenuation before believing an oscilloscope amplitude.",
  "Look at the waveform whenever a meter reading contradicts your prediction; the shape usually "
  "explains it."],
 ["A sinusoid has a peak of 170 V. Find its root-mean-square and peak-to-peak values.",
  "A 230 V rms supply feeds a 46 "+OH+" element. Find the current and the power.",
  "Find the period of a 50 Hz supply and of a 400 Hz aircraft supply.",
  "An oscilloscope shows 8 divisions peak to peak at 50 V per division. Find the root-mean-square "
  "value for a sinusoid.",
  "A waveform occupies 5 divisions per cycle at 2 ms per division. Find the frequency.",
  "Explain why the average of a symmetrical sinusoid over a full cycle is zero.",
  "A square wave has a peak of 10 V. State its root-mean-square value and explain the difference "
  "from a sinusoid.",
  "An averaging meter reads 4.2 A where the true value is 5.5 A. Find the percentage error.",
  "Find the peak voltage that a 480 V rms system's insulation must withstand.",
  "Explain why mixing a peak voltage with a root-mean-square current gives a power figure that is "
  "too high, and by what factor for a sinusoid."],
 [["1","120.2 V rms; 340 V peak to peak","Divide by 1.414; double the peak"],
  ["2","5.0 A; 1150 W","I = V/R, then P = V I, all in rms terms"],
  ["3","20 ms; 2.5 ms","T = 1/f"],
  ["4","141.4 V rms","400 V peak to peak, so 200 V peak, divided by 1.414"],
  ["5","100 Hz","Period is 10 ms, so f = 1/0.01"],
  ["6","Equal positive and negative halves","They cancel exactly over a complete cycle"],
  ["7","10 V rms","The magnitude is constant, so the mean of the square equals the square of the peak"],
  ["8","23.6 % low","1.3/5.5 expressed as a percentage"],
  ["9","679 V peak","480 \u00d7 1.414"],
  ["10","Too high by a factor of 1.414","The peak exceeds the root-mean-square value by \u221a2"]],
 ["A sinusoid needs amplitude, frequency and phase to be fully described, and phase is always "
  "relative to a reference.",
  "The root-mean-square value is the equivalent direct value for heating, and equals the peak "
  "divided by \u221a2 for a sinusoid.",
  "All the DC power relationships hold on AC provided every quantity used is root-mean-square.",
  "Peak values govern insulation stress and semiconductor ratings; root-mean-square values govern "
  "heating and conductor sizing.",
  "Averaging meters are calibrated for clean sinusoids and read low on distorted waveforms.",
  "An oscilloscope is the only instrument that shows waveform shape, which is often the "
  "explanation for a surprising meter reading."],
 [["Instantaneous value","v = V_p sin(\u03c9t + \u03c6)","Sinusoidal quantity at time t"],
  ["Period and frequency","T = 1/f","Any periodic waveform"],
  ["Angular frequency","\u03c9 = 2\u03c0f","Radians per second"],
  ["Root-mean-square","V_rms = V_p/\u221a2","Sinusoids only"],
  ["Rectified average","V_avg = 0.637 V_p","Sinusoids only"],
  ["Resistive AC power","P = V_rms I_rms","Purely resistive load"]],
 [["Root-mean-square","The equivalent direct value that produces the same heating"],
  ["Crest factor","The ratio of peak to root-mean-square value, 1.414 for a sinusoid"],
  ["Form factor","The ratio of root-mean-square to rectified average, 1.11 for a sinusoid"],
  ["True rms meter","An instrument that computes the root-mean-square of the actual waveform"],
  ["Phase","The displacement of one waveform relative to another of the same frequency"]],
 "You can now describe and measure an alternating quantity. The next chapter adds reactive "
 "elements to alternating circuits, where current no longer peaks with voltage and the concept "
 "of impedance replaces simple resistance.",
)
