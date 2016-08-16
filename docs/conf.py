master_doc = 'index'

project = u'SAREhub'
copyright = u'2016, SARE SA'
author = u'SARE SA'

# The suffix of source filenames.
from recommonmark.parser import CommonMarkParser

# The suffix of source filenames.
source_suffix = ['.rst', '.md']

source_parsers = {
   '.md': CommonMarkParser,
}