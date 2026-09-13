Please now i would like to have another version,
I just need to create the slides, no script notes for now.
- I prefer the dark theme, so please use the style, layout, colors, fonts from presentation_academic
- I would like to have as footer, instead of Master's defence or Master Thesis, the name of the part that was in the heading, with that color and style, for example in presentation_academic : MATHEMATICAL FRAMEWORK, CHANNEL FRAMEWORK, PHYSICAL MODELLING etc.; so we can save a little more space on the top and have more space in the slides.
- after the title, draw a small colored line, as you did in presentation_3, but set the parameter like color, lenght in percentage, thickness, at the top of the page so i can tweak them by myself later.
- For what concerns the slides, build the presentation as follows:
    - slide 1 and 2 from presentation_academic
    - slide 3 from presentation_3 but please, I would like to have an animation, so multiple slides where i can see the classical quantum information moving because we chose different measurment basis
    - slide 3 from presentation_academic
    - slide 4 from presentation_academic
    - a new slide, with the formulas from slide 6 from presentation_3, but where i will show parallely on 2 lines the formulas and the circuit. This slide is used just to say that I study both the quantum circuit and the numerical precise simulation for that, and all the steps in the pipeline can be swapped at any time. So to explain parallely:
        - the initialization and the numerical evolutions, and the circuit initialization and time evolution
        - the PCA, and the VQSE
        - the partial trace, and a non measuring of the circuit,
        - use, if you find useful these plots, and leave a todo if i need to plot something:
            - the initialization quantum circuit: /home/ronin/Dev/thesis/TeXtured/figures/asi_report/circuit_notrotter.png
            - the circuit for the VQSE (i do not it to be readable, since the formulas are more important, but maybe it is nice): /home/ronin/Dev/thesis/TeXtured/figures/misc/lhea_pennylane.png
            - the output of QFI (i do not need it to be readable, can be just shown as an output), TQFI etc : /home/ronin/Dev/thesis/TeXtured/figures/asi_report/simulation.png
    - both slides 7 from presentation_3 and slide 5 from presentation can go one after another, the goal is to explain that a thermal state, being able to control only the temperature, can be useful if we want a high localized peak when we know where is the domain of measurement, or a smooth curve if we do not acutally know where h_x is.
    - a blank spade detector slude (slide 8 of presentation_3)
    - slide 6 from presentation academic, but in the direct imaging part, insert side by side the plots: 
        - /home/ronin/Dev/thesis/TeXtured/figures/scripts_for_figures/rayleigh_resolved.png
        - /home/ronin/Dev/thesis/TeXtured/figures/scripts_for_figures/rayleigh_unresolved.png
    - slide 7 from presentaiton_academic but the numer 52500 smaller, and insert side by side the plots:
        - /home/ronin/Dev/thesis/TeXtured/figures/asi_report/sample_1_exoplanet_2026.png
        - /home/ronin/Dev/thesis/TeXtured/figures/asi_report/average_sample_exoplanet_2026.png  
    - slide 8 from presentation_academic,  
    - all the slides from slide 10 from presentation_3 


I want to change a little the flow:
- slide 4 has to introduce a little that i will use mixed states and a good way to treat them is to compute the truncated density matrix, so:
  - change the title,
  - insert TQFI somewhere
  - maybe remove the square of the PCA, but add a point that says that it resembles it

- add a new slide 5 that says our aim: We want to study QFI, TQFI. both simulating numerically and creating the quantum circuits. Apply those methods to:
    - a quantum magnetometer 
    - a exoplanet problem 
- after this, insert the old slide 6, remove the subtitle, the takeway. remove the formulas and insert them in the notes, little, just as a reference. make the boxes larger, in "preparation/encoding" leave only "preparation", and make the plot a little bigger, so we can see them, and make an actual viisble separation between numerical simulaiton and quantum circuit
- after this slide insert old slide 5 of the magnetometer
- then old slide 7 and old slide 8, old slide 9 and so on.
  

