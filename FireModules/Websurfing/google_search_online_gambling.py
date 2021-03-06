#!/usr/bin/python
#
# Filename:  
#
# Version: 1.0.0
#
# Author:  Emmanuel Ferran (FullMidnight) based off the work by Joe Gervais (TryCatchHCF)
#
# Summary:
#
#	Part of the DumpsterFire Toolset. See documentation at https://github.com/TryCatchHCF/DumpsterFire
#
#
# Description:
#
#
# Example:
#
#

import urllib, time, random

from FireModules.fire_module_base_class import *

class google_search_online_gambling( FireModule ):

	def __init__(self):
		self.commentsStr = "Websurfing/google_search_online_gambling"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Websurfing/google_search_online_gambling"
		return;

	def Description( self ):
		self.Description = "Performs Google search on online gambling sites"
		return self.Description

	def Configure( self ):
		return

	def GetParameters( self ):
		return ""

	def SetParameters( self, parametersStr ):
		print (parametersStr)
		return

	def ActivateLogging( self, logFlag ):
		print (self.commentsStr + ": Setting Logging flag!")
		print (logFlag)
		return

	def Ignite( self ):

		print (self.commentsStr + ": Opening URL session for Google search on online gambling")
		self.webSession = urllib.request.urlopen( 'https://www.google.com/search?q=online+gambling+sites&oq=online+gambling+sites' )
		trash = self.webSession.read()

		return

