from TDStoreTools import StorageManager
import TDFunctions as TDF
import yaml

class ScoreExt:
	"""
	ScoreExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		TDF.createProperty(self, 'ScorePath', value="",
					dependable=True, readOnly=False)
		TDF.createProperty(self, 'ScoreName', value="",
					dependable=True, readOnly=False)

	def LoadScore(self, scorePath):
		"""
		Load a .YAML score from path.
		"""
		if not scorePath.endswith('.yaml'):
			op.LOG.Log('Score path must end with .yaml')
			ui.messageBox('error','Score path must end with .yaml')
			return

		self.ScorePath = scorePath

		with open(scorePath) as f:
			data = yaml.load(f, Loader=yaml.FullLoader)
			if not data:
				op.LOG.Log('Score file is empty or invalid')
				ui.messageBox('error','Score file is empty or invalid')
				return

			op.SETTINGS.ReadConfigDict(data)

			print(data)

		debug(f'Score: {scorePath}')
