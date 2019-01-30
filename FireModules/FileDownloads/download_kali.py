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

class download_kali( FireModule ):

	def __init__(self):
		self.commentsStr = "FileDownloads/download_kali"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "FileDownloads/download_kali"
		return;

	def Description( self ):
		self.Description = "Downloads Kali distro to local directory"
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

		self.filepath = self.mDirectoryPath + "/" + 'kali.iso'
		print self.commentsStr + ": Downloading Kali to: " + self.filepath
		with open(self.filepath, 'wb') as out_file:
    		with contextlib.closing(urllib.request.urlopen('http://cdimage.kali.org/kali-2017.2/kali-linux-2017.2-amd64.iso')) as fp:
        		block_size = 1024 * 8
        		while True:
            		block = fp.read(block_size)
            		if not block:
                		break
            		out_file.write(block)
		return

