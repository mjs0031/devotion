""" Python Package Support """
# Not Applicable

""" Django Package Support """
from django.contrib import admin

"""        Internal Package Support          """
""" -- IMPORTED AT APPROPRIATE SUBSECTION -- """

"""
 
 File       :: devotion/admin.py
 
 Author(s)  :: Matthew J Swann
 Version    :: 1.0
 Last Mod   :: 2014-08-11
 Mod by     :: Matthew J Swann
 
 This code imports each database table from each internal support
 package and then registers these to the admin site.
 
"""

"""
 {
   DEVOTIONAL
 }
"""

from devotional.models import (
            Devotional               
                )

admin.site.register(Devotional) #, DevotionalAdmin)