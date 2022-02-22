Normal text

.. code-block:: Python

    import random

More normal text


.. code-block:: python

    import random


.. code-block:: console

        # console - ❌
        python -m pip install -r requirements.txt

.. code-block:: bash

        # bash - ✅
        python -m pip install -r requirements.txt


.. code-block:: console

        # console - ✅
        $ python -m pip install -r requirements.txt
        Requirement already satisfied: Pygments>=2.9.0 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from -r requirements.txt (line 2)) (2.11.2)
        Requirement already satisfied: Sphinx>=4.0.2 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from -r requirements.txt (line 3)) (4.4.0)
        ...

.. code-block:: bash

        # bash - ❌
        python -m pip install -r requirements.txt
        Requirement already satisfied: Pygments>=2.9.0 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from -r requirements.txt (line 2)) (2.11.2)
        Requirement already satisfied: Sphinx>=4.0.2 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from -r requirements.txt (line 3)) (4.4.0)
        ...
