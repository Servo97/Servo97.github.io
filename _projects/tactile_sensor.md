---
layout: page
title: Tactile Sensor
description: A low-cost magnetometer-based tactile sensor for soft robots
img: assets/img/projects/tactile/black-finger_3mag.jpg
importance: 1
category: MSR
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/tactile/black-pcb.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/tactile/black-finger_3mag.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/tactile/black-setup.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<h3>(In Progress)</h3>

Soft robots for manipulation can afford a wide range of actions purely on the back of compliance. However, for delicate everyday tasks, especially in the areas of robotic indoor assistance, human feeding, medicine delivery, and wound care, relying on compliance might not be enough. We need tactile feedback at a high frequency with high sensitivity to detect these contacts and act on them. 

Although there are established tactile sensors like <a href="https://www.gelsight.com/">GelSight</a>, and <a href="https://syntouchinc.com/">BioTac</a>, they either require a lot of compute, or are quite expensive, which defeats the low-cost objective of using soft robots for manipulation. 

Recent works like <a href="https://reskin.dev/">ReSkin</a> and <a href="https://arxiv.org/pdf/2203.15941.pdf">Biomimetic Tactile Sensor</a> have shown great potential of low-cost tactile sensing. Inspired from these works, our project uses soft silicone elastomers to make an omni-directional tactile sensor with an array of magnets embedded around 4 magnetometers as shown above.

<h4>Challenge:</h4> Hand soldering 0201 level SMD components, Designing resin printed molds for curing soft elastomers to embed 2mmx2mmx2mm magnetic cubes, and characterizing the sensor against ground truth forces from an industry grade force-torque sensor. 

<h4>Motivation:</h4> The main motivation for these sensors is for use with multi-finger soft hands that can't hold hefty sensors and need a wide range of sensing to accomplish dexterous manipulation tasks. 

Sensor characterization experiments involve using a UR5 Robot to apply forces around the surface of the tactile sensor, collect magnetometer sensor readings, and store the corresponding ground truth force values from a NordBo robotics force-torque sensor. 