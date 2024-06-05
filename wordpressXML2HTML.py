from xmlr import xmliter
import datetime
import argparse

# This script is deprecated. Please use wordpressXML2HTML_2.py 
# 

def getLines( InFileName, outfileName, maxLines, startdate = None, enddate = None):

    f = open(outfileName,'w', encoding='utf8')
    f.write("<HTML><BODY>\n")

    count = 0
    if maxLines == None:
        maxLines=-1

    DateStart = None
    DateEnd = None
    if ( startdate != None ):
        DateStart = datetime.datetime.strptime( startdate , "%Y-%m-%d" )
    if ( enddate != None ):
        DateEnd = datetime.datetime.strptime( enddate, "%Y-%m-%d" )

    for d in xmliter(InFileName, 'item'):
        if maxLines == -1 or count < maxLines : 
            if ( d['{http://wordpress.org/export/1.2/}post_type'] == 'post' ):
                if ( d['title'] != None ):
                    title = "<H2>" + d['title'] + "</h2>"
                    if ( d['pubDate'] != None ):
                         
                        date_time_obj = datetime.datetime.strptime(d['pubDate'],"%a, %d %b %Y %H:%M:%S %z")
                        date_time_obj = date_time_obj.replace(tzinfo=None)
                        if ( ( DateStart != None ) and ( DateStart < date_time_obj ) ) or (DateStart == None):                      
                            if ( ( DateStart != None ) and ( DateEnd > date_time_obj ) ) or (DateEnd == None):
                                f.write(title + "\n")
                                dateStr = '<b>'+ date_time_obj.date().strftime("%Y-%m-%d") + '</b>' 
                                f.write( dateStr + "\n" )
                                itemString = "<p>" + d['{http://purl.org/rss/1.0/modules/content/}encoded'].replace('\n\n','</p><p>\n') + '</p>'
                                f.write( itemString +"\n" )
                                count = count + 1

    f.write('\n</BODY></HTML>')
    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file', help='Name of the xml file exported from wordpress', required=True)
    parser.add_argument('-o','--output',help='Name of the file to output to', required=True)
    parser.add_argument('-n','--number',help='Number of entries to convert')
    parser.add_argument('-sd','--startdate',help='Date from which to start processing entries  (in YYYY-MM-DD format)')
    parser.add_argument('-ed','--enddate',help='Date to stop processing entries at (in YYYY-MM-DD format)')
    
    args = parser.parse_args()   
        
    getLines( args.file, args.output, args.number ,args.startdate, args.enddate )