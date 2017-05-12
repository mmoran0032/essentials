PYTHON INSTALLATION
===================

To get your ``python3`` environment up an running, follow the steps below.
Previously, you just installed things as needed, but since you've figured out
exactly what you need, and since those requirements aren't going to change any
time soon, just run this as a batch operation and get it over with.

Of course, you will end up adding to this as you go, but that's fine.


Miniconda
---------

Use the **miniconda** distribution of Anaconda, downlaoded from `their
website <http://conda.pydata.org/miniconda.html>`__, and run the bash script. I
place the directory within ``/opt/miniconda3`` to keep my home directory
uncluttered. Obviously use the Python 3.X version of miniconda.

*Almost* everything you need can be installed with conda, so run the below to
grab everything and get going::

    conda install beautifulsoup4 cython flake8 flask \
                  h5py html5lib jupyter lxml \
                  matplotlib mpmath numpy \
                  pandas patsy psutil psycopg2 requests \
                  scikit-learn scikit-image scipy \
                  seaborn setuptools sqlalchemy statsmodels sympy

That's it! It's a mix of scientific, machine learning, and helper packages that
you've been using frequently, and some you haven't been using frequently. Go
through the list again every time you reinstall, as there are probably some
packages that you could take out of the mix.

You can also check which packages are installed with ``conda list``. This does
include packages that you didn't explicitly call for, so will be longer than
the above.

Some packages require you to install them with ``conda install -c [URL]
package``, listed below:

-  **OpenCV**: ``https://conda.binstar.org/menpo opencv3``

-  **pymc3**: ``conda-forge pymc3``

-  **sqlalchemy-utils**: ``conda-forge sqlalchemy-utils``


Additional Installs
-------------------

There are a few packages that aren't included in Anaconda, so you'll have to
download and install them with ``python3 setup.py install --user``. When
checking your installed packages, these will still show up, but as a pip-
installed package.

-  **autopep8** (``git@github.com:hhatto/autopep8.git``), a utility that
   automatically converts code to be compliant with PEP8 guidelines. Every so
   often I want to use this, since it is a quick swipe across everything. For
   the most part, my code follows PEP8 pretty closely.
-  **progressbar** (``git@github.com:coagulant/progressbar-python3.git``), a
   wrapper for loops that displays the progress of that loop in the terminal.
   Nice for when I write longer, non-interactive analysis scripts.
