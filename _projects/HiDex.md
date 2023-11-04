---
layout: page
title: HiDex 
description: A novel MCTS-based algorithm to generate contact-rich manipulation plans using RRT within seconds.
img: assets/img/projects/hidex/HiDex.gif
importance: 1
category: PhD
---

<div class="row">
    <div class="col-sm mt-6 mt-md-0">
        {% include figure.html path="assets/img/projects/hidex/transparent-overview.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-6 mt-md-0">
        {% include figure.html path="assets/img/projects/hidex/transparent-level1.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

We present a hierarchical framework for planning rigid-body motions and contacts for dexterous robotic manipulation. 
Our framework has three levels: 
1. planning object motions; 
2. planning robot contacts; 
3. path evaluation and control optimization that passes the rewards to the upper levels. 
We apply our framework to 7 hand configurations and 15 scenarios. We demonstrate 8 of the plans on robots. 
Our framework offers two main advantages. 
First, it allows efficient global reasoning over high-dimensional complex space. 
Our planners solve a diverse set of manipulation tasks that require dexterity both intrinsic (using the fingers) and extrinsic (also using the environment) mostly in seconds.  
Second, our framework incorporates expert knowledge and allows for customizable setups in task mechanics and models. It requires only minor modifications to accommodate different scenarios and robots. Hence, it could provide a flexible and generalizable solution for many manipulation tasks. 

<a href="https://xianyicheng.github.io/HiDex-Website">The project website with all demo videos can be found here!</a>

<div class="row">
    <div class="">
        {% include figure.html path="assets/img/projects/hidex/HiDex.gif" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>