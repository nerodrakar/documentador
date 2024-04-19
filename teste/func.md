---
layout: default
title: func
grand_parent: Framework
parent: Common Library functions
nav_order: 1
has_toc: false
---

<h3>func</h3>

<br>

<p align = "justify">
    See documentation in: https://wmpjrufg.github.io/EASYPLOTPY/001-6.html
</p>

```python
func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.2f}%\n({:d})".format(pct, absolute)
        
    # Plot
    w, h = convert_si_to_inches_in_chart_size(w, h)
    fig, ax = plt.subplots(1, 1, figsize = (w, h), subplot_kw = dict(aspect = 'equal'))
    wEDGES, textensions, autotextensions = ax.pie(VALUES, autopct = lambda pct: func(pct, VALUES), textensionprops = dict(color = Textension_color), colors = colors)
    ax.legend(wEDGES, ELEMENTS, loc_legend = 'center left', bbox_to_anchor = (1, 0.5), fontsize = legend_size)
    plt.setp(autotextensions, size = Textension_FONT_size, weight = 'bold')
    
    # Save figure
    save_chart_in_folder(name, extension, dots_per_inch)


def radar_chart(**kwargs)
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
        <td><code>pct</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.2f}%\n({:d})".format(pct</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>absolute)
        
    # Plot
    w</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>h = convert_si_to_inches_in_chart_size(w</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>h)
    fig</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>ax = plt.subplots(1</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>1</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>figsize = (w</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>h)</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>subplot_kw = dict(aspect = 'equal'))
    wEDGES</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>textensions</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>autotextensions = ax.pie(VALUES</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>autopct = lambda pct: func(pct</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>VALUES)</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>textensionprops = dict(color = Textension_color)</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>colors = colors)
    ax.legend(wEDGES</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>ELEMENTS</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>loc_legend = 'center left'</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>bbox_to_anchor = (1</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>0.5)</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>fontsize = legend_size)
    plt.setp(autotextensions</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>size = Textension_FONT_size</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>weight = 'bold')
    
    # Save figure
    save_chart_in_folder(name</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>extension</code></td>
        <td>Description not available.</td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>dots_per_inch)


def radar_chart(**kwargs</code></td>
        <td>Description not available.</td>
        <td>None</td>
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
        <td>This function does not return any value.</td>
        <td>None</td>
    </tr>
</table>

Example 1
{: .label .label-blue }

<p align = "justify">
    <i>
        Use the <code>func</code> function to perform a task.
    </i>
</p>

```python
# Example code goes here
```

```bash
# Example output goes here
```

