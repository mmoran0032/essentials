Environment Setup
=================

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
#.  Create a ``.envrc`` file that contains the single line::

        source activate ENVNAME

    ``ENVNAME`` needs to be replaced with the same name you used in the
    ``environment.yml`` file.
#.  Make sure that ``direnv`` is installed, and if not, install it.
#.  Do any source control work that you need to do.

When you change into the directory, the ``.envrc`` file combined with
``direnv`` will automatically source your created virtual environment, so
you don't have to automatically do it. Additionally, it will unsource it
when you change out of that directory.

*Information provided by
`TD Hopper <http://tdhopper.com/blog/2015/Nov/24/my-python-environment-workflow-with-conda/>`_ and adapted to use ``direnv`` instead of ``autoenv``.*

