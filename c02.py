# -*- coding: utf-8 -*-
from render import OH,MU,TAU,DEG,AP,TIMES

CH2=dict(n=2,title="Kirchhoff's laws",
 sub="Conservation of charge at a node, conservation of energy around a loop",
 why="Ohm's law describes one component. Kirchhoff's two laws describe how components "
     "constrain each other, and they are the only tools that will solve a network no amount of "
     "series-parallel reduction can simplify.",
 objs=["State both laws and identify the conservation principle behind each.",
   "Assign and keep consistent reference directions and loop senses.",
   "Write and solve node equations for a two-node network.",
   "Write and solve mesh equations for a two-loop network.",
   "Use a measured set of readings to detect an inconsistent or faulty circuit."],
 openfig=("c2_kcl","Kirchhoff's current law at a single node. The algebraic sum of the currents "
   "entering the node is zero; charge does not accumulate there.",44),
 secs=[
  dict(h2="The current law: charge cannot pile up",
   paras=["Kirchhoff's current law, KCL, states that the algebraic sum of currents entering any "
     "node is zero. Equivalently, the sum of currents arriving equals the sum leaving. The law "
     "follows directly from conservation of charge: a node is a point with no capacity to store "
     "charge, so whatever arrives must depart in the same instant.",
     "To apply KCL you must first commit to arrow directions. Any choice works provided you keep "
     "it, because the algebra will correct a wrong guess with a negative sign. The common failure "
     "is not a bad guess but an inconsistent one: changing a direction halfway through a solution "
     "guarantees a wrong answer."],
   eq=["\u03a3 I_in = \u03a3 I_out",
       "I\u2081 + I\u2082 \u2212 I\u2083 \u2212 I\u2084 = 0"],
   panel=("What counts as a node",
     ["A node is any stretch of conductor at one potential, however it is drawn on the page.",
      "Two junctions joined only by plain wire are the same node, so they share one equation.",
      "Counting nodes correctly is how you know in advance how many equations you need: one "
      "fewer than the node count."])),
  dict(h2="The voltage law: energy cannot be created in a loop",
   paras=["Kirchhoff's voltage law, KVL, states that the algebraic sum of potential differences "
     "around any closed loop is zero. Because voltage is energy per unit charge, a charge "
     "returned to its starting point must have gained and lost equal energy. Sources supply, "
     "resistances absorb, and the books must balance.",
     "In practice KVL means you can walk a loop on the drawing, adding a voltage rise when you "
     "pass from minus to plus through a source and subtracting a drop when you pass through a "
     "resistance in the direction of its current arrow. Return to the start and the total is zero."],
   eq=["\u03a3 V_rises = \u03a3 V_drops",
       "V_s \u2212 I R\u2081 \u2212 I R\u2082 = 0"],
   fig=("c2_kvl","Walking a loop with KVL. The supply voltage is distributed among the series "
     "elements, and the signed sum around the closed path is zero.",44)),
  dict(h2="Node-voltage analysis",
   paras=["Node analysis takes the node potentials as the unknowns. Choose a reference node, "
     "usually the one with the most connections, call it zero, then write KCL at each remaining "
     "node with every branch current expressed by Ohm's law as a potential difference divided by "
     "a resistance. The result is one equation per unknown node.",
     "Node analysis suits circuits with many parallel branches and few loops, which describes "
     "most distribution and sensor wiring. It is also the method that mirrors measurement, "
     "because a voltmeter referenced to one point reads node potentials directly."],
   numbered=["Identify and merge all nodes; count them.",
     "Choose the reference node and mark it 0 V.",
     "Label the remaining node potentials V_a, V_b and so on.",
     "At each labelled node write KCL with every current as (V_this \u2212 V_other) / R.",
     "Solve the simultaneous equations, then back-substitute for branch currents.",
     "Check by confirming KVL around any loop you did not use."]),
  dict(h2="Mesh-current analysis",
   paras=["Mesh analysis takes circulating loop currents as the unknowns. Assign a current to "
     "each independent loop, all in the same rotational sense, then write KVL around each loop. "
     "A resistance shared between two meshes carries the difference of the two mesh currents, "
     "which is where most sign errors occur.",
     "Mesh analysis suits circuits with few loops and many series elements. For a planar network "
     "the number of meshes equals the number of independent equations, so a two-loop circuit "
     "gives two equations in two unknowns regardless of how many components it contains."],
   eq=["Loop 1:  V_s = I\u2081(R\u2081+R\u2083) \u2212 I\u2082 R\u2083",
       "Loop 2:  0   = \u2212I\u2081 R\u2083 + I\u2082(R\u2082+R\u2083)"],
   fig=("c2_bridge","A bridge network. No amount of series or parallel reduction simplifies it, "
     "so node or mesh analysis is required.",46)),
  dict(h2="Choosing a method, and checking the answer",
   paras=["Count before you commit. If a circuit has fewer nodes than meshes, use node analysis; "
     "if fewer meshes than nodes, use mesh analysis. Either method gives the same answer, so the "
     "choice is only about arithmetic effort.",
     "Every solution should be checked against the law you did not use. If you solved by node "
     "equations, verify KVL around a loop. If you solved by mesh equations, verify KCL at a node. "
     "A solution that satisfies both laws and gives positive power absorbed by every resistance "
     "is almost certainly right."],
   table=(["Situation","Preferred method","Reason"],
     [["Many parallel branches","Node analysis","Fewer unknowns, matches voltmeter readings"],
      ["Few loops, long series strings","Mesh analysis","Fewer unknowns, avoids many node merges"],
      ["Bridge or ladder","Either, by count","Neither reduces by series-parallel alone"],
      ["One source, simple series-parallel","Reduction then Ohm's law","No simultaneous equations needed"]],None),
   panel=("Three checks that catch almost every error",
     ["Does every resistance absorb positive power? A negative value means a sign slip.",
      "Does the total source power equal the total dissipated power?",
      "Does the unused law hold? Node solutions must satisfy KVL and vice versa."])),
 ],
 examples=[
  dict(title="Current law at a supply node",
   given="Three branches leave a distribution node. Two carry 6.2 A and 3.4 A away from the "
     "node; the feed carries current toward it.",
   find="The feed current, and the third branch current if it measures 1.1 A away.",
   steps=[("Write KCL with inbound positive","I_feed \u2212 6.2 \u2212 3.4 \u2212 1.1 = 0"),
     ("Solve for the feed","I_feed = 10.7 A"),
     ("Confirm the balance","10.7 = 6.2 + 3.4 + 1.1 \u2713")],
   check="A clamp meter on the feed should read 10.7 A. A reading materially below that, with "
     "branch readings unchanged, indicates an unrecorded branch or a leakage path."),
  dict(title="Voltage law around a two-resistor loop",
   given="A 24 V source feeds R\u2081 = 180 "+OH+" in series with R\u2082 = 120 "+OH+".",
   find="The loop current and the voltage across each resistor.",
   steps=[("Apply KVL around the loop","24 \u2212 180 I \u2212 120 I = 0"),
     ("Collect terms","300 I = 24"),
     ("Loop current","I = 0.08 A = 80 mA"),
     ("Drops from Ohm's law","V\u2081 = 0.08 \u00d7 180 = 14.4 V ; V\u2082 = 0.08 \u00d7 120 = 9.6 V")],
   check="14.4 + 9.6 = 24.0 V, equal to the source, so KVL is satisfied around the loop."),
  dict(title="Two-node network by node analysis",
   given="A 12 V source feeds node A through 100 "+OH+". Node A connects to the reference "
     "through 200 "+OH+" and to node B through 50 "+OH+". Node B connects to the reference "
     "through 150 "+OH+".",
   find="The node potentials and the current in the 50 "+OH+" link.",
   steps=[("KCL at A","(12 \u2212 V_a)/100 = V_a/200 + (V_a \u2212 V_b)/50"),
     ("KCL at B","(V_a \u2212 V_b)/50 = V_b/150"),
     ("From B, express V_a","V_a = V_b (1 + 50/150) = 1.3333 V_b"),
     ("Substitute into A and solve","V_b \u2248 3.13 V, V_a \u2248 4.17 V"),
     ("Link current","I = (4.17 \u2212 3.13)/50 \u2248 20.8 mA")],
   check="Check KVL on the source branch: 12 \u2212 0.0783\u00d7100 \u2248 4.17 V, matching V_a, "
     "so the solution is consistent.")],
 lab=dict(title="verifying both of Kirchhoff's laws on a two-loop network",
  aim="Build a network that cannot be reduced by inspection, predict every branch current and "
      "node voltage from the two laws, then confirm the predictions by measurement within the "
      "tolerance of the components.",
  gear=["DC supply, 0\u201320 V, current limited to 0.5 A.",
    "Resistors: 100 "+OH+", 150 "+OH+", 220 "+OH+", 330 "+OH+", 470 "+OH+", all 0.5 W.",
    "Two multimeters, breadboard or terminal strip, and marked test leads.",
    "Squared paper for the circuit drawing and the prediction table."],
  steps=["Draw the two-loop network and label every node and branch before building it.",
    "Assign a reference node, a current arrow to every branch and a sense to each loop.",
    "Predict all branch currents and node voltages using node or mesh analysis. Record the "
    "predictions before any measurement.",
    "Build the circuit and set the supply to 12.0 V measured at its terminals.",
    "Measure every node voltage with the black lead held on the reference node throughout.",
    "Measure each branch current by opening that branch only, then restoring it before moving on.",
    "At each node, sum your measured currents and record the residual.",
    "Around each loop, sum your measured voltages and record the residual."],
  fig=("c2_bridge","The network for this activity. Node and branch labels must be written on your "
    "own drawing before the circuit is energised.",46),
  thdr=["Branch","Predicted I (mA)","Measured I (mA)","Node","Predicted V","Measured V"],
  trows=[["1","","","A","",""],["2","","","B","",""],["3","","","C","",""],
    ["4","","","D","",""],["5","","","\u2014","",""]],
  questions=["How close is each node residual to zero? Express the worst one as a percentage of "
    "the largest current at that node.",
   "How close is each loop residual to zero? Account for the difference using the resistor "
    "tolerance bands.",
   "Measure the resistors individually and recompute your predictions. Does the agreement improve?",
   "Which measurement disturbed the circuit most, the voltage readings or the current readings? "
    "Explain in terms of meter resistance.",
   "If one node residual were 15 % while all others were near zero, what single fault would you "
    "suspect and what would you measure next?"],
  safety=["Keep the supply at or below 20 V and the current limit at 0.5 A.",
    "De-energise before opening a branch to insert the ammeter.",
    "Check resistor power ratings against your predicted currents before energising.",
    "Never leave an ammeter connected across the supply."]),
 trouble=[["Node currents do not sum to zero","An unrecorded branch or a leakage path to earth",
   "Clamp or series-measure every conductor at that node","Trace the extra path; test insulation "
   "resistance de-energised"],
  ["Loop voltages do not sum to zero","A high-resistance joint acting as an unseen resistor",
   "Measure voltage across each joint under load","Re-terminate the joint and re-measure"],
  ["A branch current is negative in reality but positive in prediction","Reference arrow drawn "
   "opposite to the true flow","Compare the drawing with the physical wiring","Correct the "
   "drawing, not the measurement"],
  ["Node voltages all read low","Supply sagging under load, or source internal resistance",
   "Measure supply terminal voltage loaded and unloaded","Use a stiffer supply or account for "
   "internal resistance"],
  ["Readings change when the meter is moved","Meter loading on a high-resistance node",
   "Compare a high-impedance meter against the original","Use a higher input impedance meter and "
   "state it with the reading"],
  ["Two nodes read identical voltages unexpectedly","The two are actually one node, or a "
   "component is short circuited","Measure resistance between them de-energised","Correct the "
   "node count or replace the shorted part"]],
 tfig=("c2_kcl","A node under test. Every conductor at the node must be accounted for before the "
   "current law can be used as a fault indicator.",44),
 habits=["Write the node and branch labels on the drawing before energising; labels invented "
   "during fault-finding are rarely consistent.",
  "Hold the voltmeter reference lead in one place for a whole set of readings.",
  "Record the supply terminal voltage alongside every set, so sag is visible later.",
  "Treat a non-zero node residual as a real finding and chase it; it almost always means a path "
  "you have not drawn."],
 exercises=["Four conductors meet at a node. Three carry 2.1 A, 3.6 A and 0.8 A away. Find the "
  "fourth current and state its direction.",
  "A 36 V source drives a series loop of 220 "+OH+" and 380 "+OH+". Find the current and both drops.",
  "In a loop containing a 12 V and a 5 V source in opposition with a single 68 "+OH+" resistor, "
  "find the current.",
  "State how many independent node equations a circuit with six nodes requires.",
  "State how many independent mesh equations a planar circuit with four meshes requires.",
  "Two resistors, 150 "+OH+" and 450 "+OH+", are in parallel across 18 V. Verify KCL at the top node.",
  "A loop sums to \u22120.6 V instead of zero with 24 V applied. Express the discrepancy as a "
  "percentage and suggest a cause.",
  "Write, but do not solve, the node equations for a circuit with nodes A and B, a 20 V source "
  "feeding A through 120 "+OH+", a 240 "+OH+" from A to reference, a 60 "+OH+" from A to B and a "
  "180 "+OH+" from B to reference.",
  "Explain why a resistance shared by two meshes carries the difference of the mesh currents.",
  "A bridge has 1 k"+OH+" in three arms and 1.2 k"+OH+" in the fourth, fed from 10 V. Explain, "
  "without full calculation, why the detector branch carries current."],
 answers=[["1","6.5 A toward the node","Inbound must equal the 6.5 A total outbound"],
  ["2","60 mA; 13.2 V and 22.8 V","I = 36/600, then V = I R for each"],
  ["3","103 mA","Net driving voltage is 12 \u2212 5 = 7 V across 68 "+OH],
  ["4","Five","One fewer than the number of nodes"],
  ["5","Four","One per independent mesh in a planar network"],
  ["6","120 mA + 40 mA = 160 mA total","Branch currents 18/150 and 18/450 sum to the supply current"],
  ["7","2.5 %; a high-resistance joint","0.6/24; an unmodelled series resistance absorbs the balance"],
  ["8","(20\u2212V_a)/120 = V_a/240 + (V_a\u2212V_b)/60 and (V_a\u2212V_b)/60 = V_b/180",
   "KCL at each labelled node with Ohm's law substituted"],
  ["9","Both mesh currents traverse it, in opposite senses","Their superposition is the net "
   "branch current, hence the difference"],
  ["10","The arm ratios are unequal, so the bridge is unbalanced","1/1 \u2260 1/1.2, so the two "
   "divider midpoints sit at different potentials"]],
 summary=["KCL is conservation of charge at a node; KVL is conservation of energy around a loop.",
  "Both laws require committed reference directions, and a negative answer means the arrow was "
  "drawn the other way.",
  "Node analysis needs one equation fewer than the node count; mesh analysis needs one per mesh.",
  "Choose the method with fewer unknowns, then check the solution against the law you did not use.",
  "Bridge and ladder networks cannot be reduced by series-parallel alone, which is the practical "
  "reason these laws exist.",
  "A non-zero node or loop residual in measurement is a fault indicator, not experimental noise."],
 formulas=[["Current law","\u03a3 I_in = \u03a3 I_out","At any node, for any instant"],
  ["Voltage law","\u03a3 V = 0 around a loop","Any closed path, signs by traverse direction"],
  ["Node equation","\u03a3 (V_n \u2212 V_k)/R_nk = 0","KCL written with Ohm's law substituted"],
  ["Mesh equation","\u03a3 V_s = \u03a3 I R around loop","KVL with shared resistors carrying mesh differences"],
  ["Independent nodes","n \u2212 1","n is the merged node count"],
  ["Independent meshes","b \u2212 n + 1","b branches, n nodes, planar network"]],
 vocab=[["Node","A stretch of conductor at a single potential, however drawn"],
  ["Mesh","A loop that encloses no other loop in a planar drawing"],
  ["Reference direction","The arrow you commit to before solving, which fixes the sign convention"],
  ["Residual","The amount by which a measured sum fails to reach zero"],
  ["Bridge","A four-arm network whose detector branch current depends on the arm ratios"]],
 bridge="With both conservation laws available you can solve any resistive network. The next "
  "chapter applies them to the two arrangements that occur most often, series and parallel, and "
  "derives the divider rules that let you skip the simultaneous equations entirely.",
)
