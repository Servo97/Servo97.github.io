---
layout: page
title: Beer Can Detection
description: Detection of beer can placement in S.E. Asian grocery stores for an Ad Agency
img: assets/img/projects/beer/black-beer1.png
importance: 4
category: HyperWorks Imaging
---

<div class="row">
    <div class="col-sm mt-6 mt-md-0">
        {% include figure.html path="assets/img/projects/beer/beer1.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-6 mt-md-0">
        {% include figure.html path="assets/img/projects/beer/beer_0.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

The problem statement for this project was given by an Ad Agency operating primarily in South East Asian countries like Thailand, Cambodia, Vietnam, and Laos. I trained a YOLO-v5 model with a self-supervised learning loop to detect all can-shaped objects with few ground truth annotations (<20). I further web-scraped images of beer cans from the internet and trained a ResNet-50 only to get a 65% accuracy in classification across 19 beer brands (classes). In order to improve this score, I used the latest (in 2020) StyleGanv2 model to generate data conditioned on the web-scraped data, as some flavor of artificial data augmentation. It helped increase the classification accuracy from 65% to 85%. 

<h4>Challenge:</h4> The Ad Agency contract workers were the hoi polloi in their respective countries. Hence, most of the images they received were taken with low-quality smartphone cameras, with no consideration for reflection or external illumination. There were 2 main challenges due to this:

1. Detecting objects behind bright ambient illumination was hard due to occlusions. 
2. Classification of detected images was hard due to external reflections in the environment adding noise to the image patches.

<h4>Motivation:</h4> Different brands pay varying amount of money to show their products on the shelves in grocery stores. Ad agencies track their stocks across vendors and ensure that the payment is justified. 