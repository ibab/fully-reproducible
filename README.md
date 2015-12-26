
# Fully reproducible research paper example

This is an example of a fully reproducible research paper using Github, Python, jinja2 and travis.
On each `git push`, travis checks out this repository and executes the `run.py` script.

The variables defined in that script are then made available to the jinja2 template `paper.tex` (which contains the LaTeX code for a research paper, with template fields for values that should be filled in from the script).
Travis fills in the template and compiles `paper.tex` into a PDF file, which it then uploads to the `gh-pages` branch of this repository. (See https://ibab.github.io/fully-reproducible for the rendered web page)
This means that each stage of the analysis is represented as a git commit with a corresponding PDF file.

Once all researchers agree on a commit that should represent the final stage of their paper, they can use `git tag` to mark it as the official final version.
When the paper is in review, corrections can in turn be marked with `git tag`.

All of this makes it very easy for researchers to collaborate.
For example, they can make use of Github's pull request feature to enable other researchers in their group to have a look at what has been changed and what the result in the paper is before they accept the change.
This not only makes it more likely that mistakes are spotted early on, but also increases the effectiveness of the group ("Why don't you make use of X?").

It also makes it possible for outsiders (machine learning experts, software engineers, laymen, …)  to easily discover and contribute to research projects.
Ideally, a fully reproducible research paper should be public from day 1!

The idea outlined here is a very basic approach that can already be realized if the computational effort needed for the analysis is not too large (can run on a single travis node).
With some work, it should be possible to automatically launch a cluster of nodes on a cloud provides like AWS instead.
This should allow for arbitrarily difficult computations and should also make it easier for outsiders to verify the analysis by launching their own nodes.

