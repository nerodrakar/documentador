---
layout: default
title: histogram_chart
grand_parent: Framework
parent: Common Library functions
nav_order: 4
has_toc: false
---

<h3>histogram_chart</h3>

<br>

<p align = "justify">
    This function shows a Boxplot and Histogram in a single chart.


</p>

```python
histogram_chart(**kwargs)
```

Input variables
{: .label .label-yellow }

<table style = "width:100%">
    <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Type</th>
      </tr>
    </thead>
    <tr>
        <td><code>plot_setup</code></td>
        <td>Setup chart Dictionary with the following keys:</td>
        <td>Dictionary</td>
    <tr>
        <td><code>name</code></td>
        <td>Path + name figure (key required in plot_setup)</td>
        <td>String</td>
    <tr>
        <td><code>width</code></td>
        <td>figure width in SI units (key required in plot_setup)</td>
        <td>Float</td>
    <tr>
        <td><code>height</code></td>
        <td>figure height in SI units (key required in plot_setup)</td>
        <td>Float</td>
    <tr>
        <td><code>extension</code></td>
        <td>File extension (key required in plot_setup)</td>
        <td>String</td>
    <tr>
        <td><code>bins</code></td>
        <td>Range representing the width of a single bar (key required in plot_setup)</td>
        <td>Integer</td>
    </tr>
</table>

Output variables
{: .label .label-yellow }

<table style = "width:100%">
    <thead>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Type</th>
      </tr>
    </thead>
    <tr>
        <td><code>None</code></td>
        <td>The function displays the plot on the screen and saves it to the local folder of the <code>.ipynb</td>
        <td>None</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>histogram_chart</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

