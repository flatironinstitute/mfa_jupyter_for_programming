# mfa_jupyter_for_programming

Support material for an introduction to using Jupyter to teach computer programming.

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/flatironinstitute/mfa_jupyter_for_programming/master)

This repository contains Jupyter notebooks and other material
intended to help teach "how to use Jupyter for teaching programming".

For sharing information with the class
<a href="https://cl1p.net/">cl1p.net</a> provides a useful temporary
clipboard service.

# Course Goals

- To walk through some example notebooks which teach programming concepts by demonstrating them in action.
- To explain advantages, disadvantages, and technical characteristics of the Jupyter infrastructure which relate to educational uses.
- To discuss different ways of deploying Jupyter and Jupyter notebooks.

The material assumes the student is familiar with some sort of traditional programming
language (Basic, Python, C, Javascript, or similar).

# Suggested software

In order to actively run the material in the notebooks discussed in the course
you should either

- Install Jupyter/Python/git locally and "clone" this repository as described below, or

- Run using Binder "in the cloud".  For best results you will need to authenticate 
as a Google user to use our Binder.  You can also use the public Binder,
but you may have performance problems (linked above in the binder image).

# Installing locally

To install locally it is best to use the Anaconda distribution.
The conda installations and some of the other installation steps can take
a few minutes to execute.  Below is the procedure I recommend:

- Get the <a href="https://www.anaconda.com/distribution/">Python 3 Anaconda distribution</a> for your platform.
Install using "single user mode".  If the install asks to change your "path" allow the change.

- Open a "terminal window" so you can use command lines.  On MS/Windows open the "anaconda prompt"
you can find using the start menu.
On Apple/Mac use Applications/Utilities/Terminal.

- In the terminal install git using the conda command line: `conda install git`

- (optional) make a directory for storing install files and change to that location.

- Use git to clone this repository to your machine: `git clone https://github.com/flatironinstitute/mfa_jupyter_for_programming.git`

- Go into the repository: `cd mfa_jupyter_for_programming`

- Install the requirements for the repository: `conda env update -f environment.yml`

- Run the Jupyter notebook server: `jupyter notebook`

- When you are done you can stop the Jupyter server by sending 2 control-C's to the terminal.

# What did I just install?

- Anaconda is a professional programming environment with associated tools widely used in academia and industry.

- `git` is the dominant method for managing software repositories.

- The environment update added a bunch of other functionality used in the course.

