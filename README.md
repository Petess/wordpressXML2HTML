# wordpressXML2HTML
A script that just gets the text from a wordpress xml export file and exports the text of the post entries to HTML

Requires python3 and the wpparser library. 

This can be installed by running pip install -r requirements.txt 

Usage for the script is:

usage: wordpressXML2HTML_2.py [-h] -f FILE -o OUTPUT [-n NUMBER] [-sd STARTDATE]
                            [-ed ENDDATE]

With this script the output can then be used by pandoc to get the entries from a blog into word or pdf format. 

Once the output has been obtained the html can be converted to docx format with the pandoc command - pandoc -s .\somename.html -o somename.docx

 Note
======
 The first version of this wordpressXML2HTML depends on the xmlr library. xmlr has been deprecated. The library can still be directly installed by downloading the xmlr source and using pip install on the directory. 

 There is a similar program written in Go available at from [goWordPressXML2HTML](https://github.com/Petess/goWordPressXML2HTML)
