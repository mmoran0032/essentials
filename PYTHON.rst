PYTHON INSTALLATION
===================

To get your ``python3`` environment up an running, follow the steps below.
Previously, you just installed things as needed, but since you've figured out
exactly what you need, and since those requirements aren't going to change any
time soon, just run this as a batch operation and get it over with.

Of course, you will end up adding to this as you go, but that's fine.


Miniconda
---------

Use the **miniconda** distribution of Anaconda, downloaded from `their
website <http://conda.pydata.org/miniconda.html>`__, and run the bash script. I
place the directory within ``/opt/miniconda3`` to keep my home directory
uncluttered. Obviously use the Python 3.X version of miniconda.

*Almost* everything you need can be installed with conda, so run the below to
grab everything and get going::

    conda install beautifulsoup4 cython flake8 flask
                  h5py html5lib jupyter lxml
                  matplotlib mpmath numpy
                  pandas patsy psutil psycopg2 requests
                  scikit-learn scikit-image scipy
                  seaborn setuptools sqlalchemy statsmodels sympy

That's it! It's a mix of scientific, machine learning, and helper packages that
you've been using frequently, and some you haven't been using frequently. Go
through the list again every time you reinstall, as there are probably some
packages that you could take out of the mix.

You can also check which packages are installed with ``conda list``. This does
include packages that you didn't explicitly call for, so will be longer than
the above.

Some packages require you to install them with ``conda install -c conda-forge
package``, listed below:

=                   =
Package             Description
=                   =
geopandas           Working with geospatial data
geoplot             Plotting geospatial data
lime                Locally-Interpretable Model Evaluation
pymc3               Bayesian models
sqlalchemy-utils    Additional database help
=                   =


Additional Installs
-------------------

There are a few packages that aren't included in Anaconda, so you'll have to
download and install them with ``python3 setup.py install --user``. When
checking your installed packages, these will still show up, but as a pip-
installed package.

-   **autopep8** (``git@github.com:hhatto/autopep8.git``), a utility that
    automatically converts code to be compliant with PEP8 guidelines. Every so
    often I want to use this, since it is a quick swipe across everything. For
    the most part, my code follows PEP8 pretty closely.
-   **progressbar** (``git@github.com:coagulant/progressbar-python3.git``), a
    wrapper for loops that displays the progress of that loop in the terminal.
    Nice for when I write longer, non-interactive analysis scripts.


Environment Setup
-----------------

Environments are used used to isolate Python versions and packages, and
managed by Anaconda. Here is a quick way to get those environments to work
automatically when changing to the directory in question:

#.  Create an ``environment.yml`` file that contains the name of the
    environment you want to create and any dependencies you want. Example::

        name: ENVNAME
        dependencies:
        - python=3
        - numpy

#.  Create the environment with ``conda env create``, which uses the file
    we just created to set up the environment.

#.  Create a ``.envrc`` file that contains the single line, where ``ENVNAME``
    needs to be replaced with the same name you used in the ``environment.yml``
    file::

        source activate ENVNAME

#.  Make sure that ``direnv`` is installed, and if not, install it. You will
    also need to allow ``direnv`` to run in this directory by running::

        direnv allow

#.  Do any source control work that you need to do.

When you change into the directory, the ``.envrc`` file combined with
``direnv`` will automatically source your created virtual environment, so
you don't have to automatically do it. Additionally, it will unsource it
when you change out of that directory.

Information provided by `TD Hopper
<http://tdhopper.com/blog/2015/Nov/24/my-python-environment-workflow-with-conda/>`__
and adapted to use ``direnv`` instead of ``autoenv``.
