# Introduction

The facets project contains two visualizations for understanding and analyzing machine learning datasets: Facets Overview and Facets Dive.

The visualizations are implemented as [Polymer](https://www.polymer-project.org) web components, backed by [Typescript](https://www.typescriptlang.org) code and can be easily embedded into Jupyter notebooks or webpages.

Live demos of the visualizations can be found on the [Facets project description page](https://pair-code.github.io/facets/).

## Facets Overview

![Overview visualization of UCI census data](/img/overview-census.png "Overview visualization of UCI census data -  Lichman, M. (2013). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml/datasets/Census+Income]. Irvine, CA: University of California, School of Information and Computer Science")

Overview gives a high-level view of one or more data sets. It produces a visual feature-by-feature statistical analysis, and can also be used to compare statistics across two or more data sets. The tool can process both numeric and string features, including multiple instances of a number or string per feature.

Overview can help uncover issues with datasets, including the following:

* Unexpected feature values
* Missing feature values for a large number of examples
* Training/serving skew
* Training/test/validation set skew

Key aspects of the visualization are outlier detection and distribution comparison across multiple datasets.
Interesting values (such as a high proportion of missing data, or very different distributions of a feature across multiple datasets) are highlighted in red.
Features can be sorted by values of interest such as the number of missing values or the skew between the different datasets.

The python code to generate the statistics for visualization can be installed through `pip install facets-overview`.

Details about Overview usage can be found in its [README](./facets_overview/README.md).

## Facets Dive

![Dive visualization of UCI census data](/img/dive-census.png "Dive visualization of UCI census data -  Lichman, M. (2013). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml/datasets/Census+Income]. Irvine, CA: University of California, School of Information and Computer Science")

Dive is a tool for interactively exploring up to tens of thousands of multidimensional data points, allowing users to seamlessly switch between a high-level overview and low-level details.
Each example is a represented as single item in the visualization and the points can be positioned by faceting/bucketing in multiple dimensions by their feature values. Combining smooth animation and zooming with faceting and filtering, Dive makes it easy to spot patterns and outliers in complex data sets.

Details about Dive usage can be found in its [README](./facets_dive/README.md).

# Setup

## Usage in Google Colabratory/Jupyter Notebooks

Using Facets in [Google Colabratory](https://colab.research.google.com) and [Jupyter](http://jupyter.org) notebooks can be seen
[in this notebook](https://colab.research.google.com/github/PAIR-code/facets/blob/master/colab_facets.ipynb). These notebooks work without the need to first download/install this repository.

Both Facets visualizations make use of HTML imports. So in order to use them, you must first load the appropriate polyfill, through `<script src="https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/1.3.3/webcomponents-lite.js"></script>`, as shown in the demo notebooks in this repo.

Note that for using Facets Overview in a Jupyter notebook, there are two considerations:
1. In the notebook, you will need to change the path that the Facets Overview python code is loaded from to the correct path given where your notebook kernel is run from.
2. You must also have the Protocol Buffers python runtime library installed: https://github.com/google/protobuf/tree/master/python. If you used pip or anaconda to install Jupyter, you can use the same tool to install the runtime library.

When visualizing a large amount of data in Dive in a Juypter notebook, as is done in the [Dive demo Jupyter notebook](./facets_dive/Dive_demo.ipynb), you will need to start the notebook server with an increased IOPub data rate.
This can be done with the command ```jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000```.

## Code Installation
```
git clone https://github.com/PAIR-code/facets
cd facets
```

## Building the Visualizations

If you make code changes to the visualization and would like to rebuild them, follow these directions:

1. Install bazel: https://bazel.build/
2. Build the visualizations: ```bazel build facets:facets_jupyter``` (run from the facets top-level directory)

## Using the rebuilt Visualizations in a Jupyter notebook

If you want to use the visualizations you built locally in a Jupyter notebook, follow these directions:

1. Move the resulting vulcanized html file from the build step into the facets-dist directory: ```cp -f bazel-bin/facets/facets-jupyter.html facets-dist/```
2. Install the visualizations into Jupyter as an nbextension.
  * If jupyter was installed with pip, you can use ```jupyter nbextension install facets-dist/ ``` if jupyter was installed system-wide or ```jupyter nbextension install facets-dist/ --user``` if installed per-user (run from the facets top-level directory). You do not need to run any follow-up ```jupyter nbextension enable``` command for this extension.
  * Alternatively, you can manually install the nbextension by finding your jupyter installation's ```share/jupyter/nbextensions``` folder and copying the facets-dist directory into it.
3. In the notebook cell's HTML link tag that loads the built facets html, load from ```/nbextensions/facets-dist/facets-jupyter.html```, which is the locally installed facets distribution. from the previous step.

## Known Issues

* The Facets visualizations currently work only in Chrome - [Issue 9](../../issues/9).

**Disclaimer: This is not an official Google product**
