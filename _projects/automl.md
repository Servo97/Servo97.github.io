---
layout: page
title: HyperWorks AutoML
description: A custom autoML tool for material scientists 
img: assets/img/projects/automl/black-automl.png
importance: 4
category: HyperWorks Imaging
---

<div class="row">
    <div class="col-sm mt-12 mt-md-0">
        {% include figure.html path="assets/img/projects/automl/automl.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

This project was developed for automating data analysis pipelines in material science labs. We primarily targeted battery manufacturers, solar cell manufacturers, and research labs in large universities. The web-app was a no-code tool for auomatic feature engineering, model training, and ensemble learning to give the most generalizable model that satisfied task requirements. A custom backend was provided for battery cycle-life prediction where domain experts could choose a subset of important features for testing battery cycle-life hypotheses.

<h4>Challenge:</h4> Developing a Full Stack Web App from scratch with no prior background. 

<h4>Motivation:</h4> Material science researchers did not necessarily have exposure to data analytics and ML methodologies. Moreover, existing autoML tools back then, needed setting up of programming environments and required familiarity of a wide range of ML tools. This app provided a no-code solution to researchers to quickly test chemical compositions and physical parameters for their processes with a user friendly UI. 

<h4>Tech Stack:</h4> 
<ul>
    <li>Backend server: Django</li>
    <li>Server Load Balancing + Reverse Proxy: Nginx, Docker</li>
    <li>Databases: MongoDB</li>
    <li>App Development: Angular 8, Highcharts</li>
</ul>

I gained a lot of insights in software development by learning and implementing frontend, backend, and CI-CD pipelines from scratch. My expertise in ML eased the actual machine learning aspects of the project, however, syncing them with a website, plotting interactive graphs, and ensuring all the async elements work with each other was a very enriching experience.