import wpparser
import datetime
import argparse


def getLines( InFileName, outfileName, maxLines, startdate = None, enddate = None):

    f = open(outfileName,'w', encoding='utf8')
    f.write("<HTML><BODY>\n")

    count = 0
    if maxLines == None:
        maxLines=-1
    
    print( maxLines )

    DateStart = None
    DateEnd = None
    if ( startdate != None ):
        DateStart = datetime.datetime.strptime( startdate , "%Y-%m-%d" )
    if ( enddate != None ):
        DateEnd = datetime.datetime.strptime( enddate, "%Y-%m-%d" )

    data = wpparser.parse(InFileName)

    print( "There are ", len( data["posts"] ) , " posts" )

    for elpost in data["posts"]:
        if maxLines == -1 or count < int(maxLines) :
            if ( elpost['title'] != None ):
                thetitle = "<h2>" + elpost['title'] + "</h2>"

                
                # date time things here 
                if ( 1 ):
                    f.write( thetitle + "\n" )
                    f.write( '<b>' + elpost['post_date'] + '</b>' )   
                    moo = elpost['content']
                    moo = moo.replace( "\n","<BR>" )
                    f.write( "<p>" + moo + "</p>")
        
        # print( elpost['title'])
        count = count + 1 
        None


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