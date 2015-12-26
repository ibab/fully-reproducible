
# Fully reproducible research paper example

This is an example of a fully reproducible research paper using Github, Python, jinja2 and travis.
On each `git push`, travis checks out this repository and executes the `run.py` script.

The variables defined in that script are then made available to the jinja2 template `paper.tex` (which contains the LaTeX code for a research paper, with template fields for values that should be filled in from the script).
Travis fills in the template and compiles `paper.tex` into a PDF file, which it then uploads to the `gh-pages` branch of this repository.
This means that each previous stage of the analysis is represented as a git commit with a corresponding PDF file.

Once all researchers agree on a commit that should represent the final stage of their paper, they can use `git tag` to mark it as the official final version.
When the paper is in review, corrections can in turn be marked with `git tag`.
