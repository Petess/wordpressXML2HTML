# wordpressXML2HTML
Simple script that just gets the text from a wordpress xml export file and exports the text of the post entries to HTML

Requires python3 

Usage for the script is:

usage: wordpressXML2HTML.py [-h] -f FILE -o OUTPUT [-n NUMBER] [-sd STARTDATE]
                            [-ed ENDDATE]

With this script the output can then be used by pandoc to get the entries from a blog into word or pdf format. 

The library that this depends on, xmlr, has been deprecated. The library can still be directly installed by downloading the source and using pip install on the directory. 

Once the output has been obtained the html can be converted to docx format with the pandoc command - pandoc -s .\somename.html -o somename.docx

 ToDo
======

 Rewrite using xmltodict
