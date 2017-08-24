Julia
=====

Julia, a high-level, high-performance computing language, is a newer language
that I may add into my repertoire for programming and data science. Since it is
still young, any initial work with it would be to learn the language and get
used to how it runs. The code has been shown to be comparable in speed to
compiled C/Fortran routines while maintaining the ease of development of
Python.


Install
-------

Install by downloading the Linux binary from
`JuliaLang.org <https://julialang.org/downloads/>`__, unpack it, and move the
directory into ``/opt``. The ``.bashrc`` file is already set up to access this
location for Julia.

Once you've installed it, there are a few required packages that you'll need to
install. Installation of these is done from the Julia REPL by running
``Pkg.add("PackageName")``. The packages I've installed are:

-   *Plots* and *PyPlot* for plotting
-   *GLM* for generalized linear models
-   *ScikitLearn* for machine learning similar to the Python interface
-   *MixedModels* for mixed-effect models
