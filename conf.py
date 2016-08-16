Contents:

.. toctree::
  :maxdepth: 2
  :glob:

  *

# The suffix of source filenames.
from recommonmark.parser import CommonMarkParser

# The suffix of source filenames.
source_suffix = ['.rst', '.md']

source_parsers = {
   ’.md’: CommonMarkParser,
}