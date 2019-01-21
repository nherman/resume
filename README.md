# Resume Templating

### Requirements
 * jinja2
 * pdflatex

##### Install reqs:
`pip install -r requirements.py`  
`brew cask install mactex`


### usage:

##### To generate PDFs:
`make`

##### To generate .md files:
`python build.py`

All output can be found in /versions/

### Notes:
 * For privately distributed PDFs, consider manually inserting contact info in .md files before running make.
