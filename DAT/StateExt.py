from TDStoreTools import StorageManager
import TDFunctions as TDF

class StateExt:
	"""
	StateExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

		# properties
		TDF.createProperty(self, 'State', value='uninit', dependable=True,
						   readOnly=False)

	def handleSetStateInit(self):
		op.LOG.Log('STATE: initState()')
		# Initialize the state of the component
		self.State = 'INIT'
		op.CONTROLPANEL.OpenScoreBrowser()
		op.LOG.Log('STATE: Component initialized to INIT state')


	def handleSetState(self, state):
		op.LOG.Log(f'STATE: handleSetState(\'{state}\')')
		# Initialize the state of the component
		if state == 'INIT': 
			self.handleSetStateInit()

	
	def Set(self, state):
		debug(f'STATE: Set(\'{state}\')')
		debug(f'STATE: current state: \'{self.State}\')')
		self.handleSetState(state)
		debug(f'STATE: new state: \'{self.State}\')')
