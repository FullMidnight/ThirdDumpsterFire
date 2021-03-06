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

import os, sys, urllib

from FireModules.fire_module_base_class import *

class download_tor_browser_linux( FireModule ):

	def __init__(self):
		self.commentsStr = "FileDownloads/download_tor_browser_linux"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "FileDownloads/download_tor_browser_linux"
		return;

	def Description( self ):
		self.Description = "Download Tor Browser for Linux"
		return self.Description

	def Configure( self ):
		self.mDirectoryPath = raw_input( "Enter Directory Path to download files into: " )
		return

	def GetParameters( self ):
		return self.mDirectoryPath

	def SetParameters( self, parametersStr ):
		self.mDirectoryPath = parametersStr
		return

	def ActivateLogging( self, logFlag ):
		print (self.commentsStr + ": Setting Logging flag!")
		print (logFlag)
		return

	def Ignite( self ):

		self.filepath = self.mDirectoryPath + "/" + 'tor-browser.zip'
		print (self.commentsStr + ": Downloading Tor Browser to: " + self.filepath)
		with open(self.filepath, 'wb') as out_file:
    		with contextlib.closing(urllib.request.urlopen('https://www.torproject.org/dist/torbrowser/7.0.6/tor-browser-linux64-7.0.6_en-US.tar.xz')) as fp:
        		block_size = 1024 * 8
        		while True:
            		block = fp.read(block_size)
            		if not block:
                		break
            		out_file.write(block)
		return

