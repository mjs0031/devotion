""" Python Package Support """
import csv

""" Django Package Support """
# Not applicable

""" Internal Package Support """
from devotional.models import Devotional

"""

 Testing/Low_Level/event_import.py
 Author:      Matthew J Swann
 Version:     1.0
 Last Update: 2013-01-02
 Update By:   Matthew J Swann
 
 
 Importing CSV to Devotional Table.

 """
 
class Import_Script(object): 
    
    def __init__(self, scriptName=None):
        
        if(scriptName.endswith(".csv") == False):
            raise IOError("Invalid script name")
        
        #if ( scriptName == None ):
        #    raise IOError("No script")
        
        csv_reader = csv.reader( open(scriptName) ) 
             
        for row in csv_reader:
            
            if str.strip(row[0]) == 'title':
                continue
            
            the_title = str.strip(row[0])
            the_month = str.strip(row[1])
            the_day   = str.strip(row[2])
            the_body  = str.strip(row[3])

            Devotional.objects.create(
                    title = the_title,
                    month = the_month,
                    day   = the_day,
                    body  = the_body                            
                            )
