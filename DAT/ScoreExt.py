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
		TDF.createProperty(self, 'SectionList', value=[],
					dependable=True, readOnly=False)		

	def LoadScore(self, scorePath):
		"""
		Load a .YAML score from path.
		"""
		if not scorePath.endswith('.yaml'):
			op.LOG.Log('Score path must end with .yaml')
			ui.messageBox('error','Score path must end with .yaml')
			return

		with open(scorePath) as f:
			data = yaml.load(f, Loader=yaml.FullLoader)
			if not data:
				op.LOG.Log('Score file is empty or invalid')
				ui.messageBox('error','Score file is empty or invalid')
				return

			self.ScorePath = scorePath
			op.SETTINGS.ReadConfigDict(data['config'])
			self.readScore(data['sections'])

		# debug(f'Score: {scorePath}')

	def readScore(self, sections):
		"""
		Read the score sections.
		"""
		for section in sections:
			if 'name' not in section:
				op.LOG.Log('Section must have a name')
				ui.messageBox('error','Section must have a name')
				continue

			if 'video_folder' not in section:
				op.LOG.Log('Section must have a video folder')
				ui.messageBox('error','Section must have a video folder')
				continue

			self.addSection(section)

	def addSection(self, sectionDict):
		"""
		Add a section to the score.
		"""
		self.SectionList.append(sectionDict)
		op.LOG.Log(f'Section added: {sectionDict}')
