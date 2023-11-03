---
layout: page
title: Delta Arrays
description: An array of 64 soft delta robots in an 8x8 grid formation
img: assets/img/projects/delta_array/upside_down_deltas.png
importance: 2
category: MSR
---


<div class="row">
    <div class="col-sm mt-6 mt-md-0">
        {% include figure.html path="assets/img/projects/delta_array/upside_down_deltas.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-6 mt-md-0">
        {% include figure.html path="assets/img/projects/delta_array/fingertip.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

The term dexterous manipulation often invokes the image of a five-fingered hand delicately holding an object as a human would. However, robots are not restricted to human morphology. Imagine instead a surface covered in fingers. Each finger can move its fingertip in a small 3D workspace above its fixed base and interact with parts of objects that enter its workspace. The fingers can work together to shift, tilt, lift, block, and even pinch objects. The large number of fingers provides additional redundancy, with larger objects being manipulated by tens of fingers at a time. The distributed nature of the fingers also means that multiple objects can be easily manipulated in parallel in different regions of the surface. This type of system would thus represent a distributed dexterous manipulation paradigm.

Our delta array setup consists of 64 linearly-actuated delta robots with 3D-printed compliant linkages. Through the design of the individual delta robots, the modular array structure, and distributed communication and control, we study a wide range of in-plane and out-of-plane manipulations, as well as prehensile manipulations among subsets of neighboring delta robots. The fingertips on the deltas previously did not have any tactile sensing, however, they were made with TPU to add compliance in grasps with a rigid core replicating the flesh and bone structure in human fingertips.

We also demonstrate dexterous manipulation capabilities of the delta array using model free RL while leveraging the compliance to not break the end-effectors. Our evaluations show that the resulting 192 DoF compliant robot is capable of performing various coordinated distributed manipulations of a variety of objects, including translation, alignment, prehensile squeezing, lifting, and grasping.

<a href="https://iamlab-cmu.github.io/delta-arrays/">Resources for fabrication and assembly are open-sourced here.</a>

<div class="row">
    <div class="col-sm mt-6 mt-md-0">
        {% include figure.html path="assets/img/projects/delta_array/block_lift.gif" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-6 mt-md-0">
        {% include figure.html path="assets/img/projects/delta_array/block_tilt.gif" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>