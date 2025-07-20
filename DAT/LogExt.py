from TDStoreTools import StorageManager
import TDFunctions as TDF

import logging


class LogExt:
	"""
	LogExt description
	"""

	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

	def Log(self, v):
		debug(f'log message: {v}')

	def CreateLogFile(self):
		debug("file created")