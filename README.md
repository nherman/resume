# Resume Templating

###usage:

Install reqs:
`pip install -r requirements.py`
`brew cask install mactex` (for PDFs) 


To generate PDFs:
`make`

To generate .md files:
`python build.py`

All output can be found in /versions/

###Requirements
 * jinja2
 * pdflatex

###Notes:
 * For privately distributed PDFs, consider manually inserting contact info in .md files before running make.