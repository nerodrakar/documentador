---
layout: default
title: line_chart
grand_parent: Framework
parent: Common Library functions
nav_order: 1
has_toc: false
---

<h3>line_chart</h3>

<br>

<p align = "justify">
    This function shows a Multiple lines in single chart.

    Args:
        plot_setup (dict): Setup chart dictionary with the following keys:
            name (str): Path + name figure
            width (float): figure width in SI units
            height (float): figure height in SI units
            extension (str): File extension
            dots_per_inch (int): The resolution in dots per inch
            marker (list): List of markers
            marker size (list): List of marker sizes
            line width (list): List of line widths
            line style (list): List of line styles
            y axis label (str): y axis label
            x axis label (str): x axis label
            labels size (int): Labels size
            labels color (str): Labels color
            x axis size (int): x axis size
            y axis size (int): y axis size
            axises color (str): Axises color
            x limit (list): x axis limits
            y limit (list): y axis limits
            chart color (list): List of chart colors
            on grid? (bool): Grid on or off
            y log (bool): y log scale
            x log (bool): x log scale
            legend (list): List of legends
            legend location (str): Legend location
            size legend (int): Legend size

    Return:
        None
</p>

```python
line_chart(**kwargs)
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
        <td><code>**kwargs</code></td>
        <td>Description of the argument</td>
        <td>Type of the argument</td>
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
        <td>Description of the return value</td>
        <td>Type of the return value</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>line_chart</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

