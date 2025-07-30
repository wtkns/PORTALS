# ControlPanelExt.py

from TDStoreTools import StorageManager
import TDFunctions as TDF


class ControlPanelExt:
	"""
	ControlPanelExt description
	"""

	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.scoreFileBrowser = op("score_file_browser")
		self.sectionDisplay = op("section_display")
		self.controlPanel = op("control_panel_container")

	def OpenControlPanel(self):
		op.LOG.Log(f"Opening Control Panel")
		self.controlPanel.openViewer()

	def HandleLoadButton(self):
		"""
		Handle the load button click event.
		"""
		scorePath = self.scoreFileBrowser.par.Value0.val
		op.LOG.Log(f"Load Score button clicked: {scorePath}")
		op.SCORE.LoadScore(scorePath)

	def HandleNextSectionButton(self):
		"""
		if next section is available, increment current section
		"""
		op.LOG.Log(f"HandleNextSectionButton called")
		if op.SCORE.CurrentSection < len(op.SCORE.SectionList) - 1:
			op.SCORE.CurrentSection += 1
			op.SCORE.SetCurrentSectionDisplay(op.SCORE.CurrentSection)
			op.LOG.Log(f"Current section incremented to {op.SCORE.CurrentSection}")

	def HandlePreviousSectionButton(self):
		"""
		if previous section is available, decrement current section
		"""
		op.LOG.Log(f"HandlePreviousSectionButton called")

	def SetCurrentSectionDisplay(self, sectionNumber):
		"""
		Set the current section display.
		"""
		self.sectionDisplay.par.Value0 = sectionNumber
		op.LOG.Log(f"Set current section display to {sectionNumber}")

	def SetScoreLengthDisplay(self, scoreLength):
		"""
		Set the score length display.
		"""
		self.sectionDisplay.par.Value1 = scoreLength
		op.LOG.Log(f"Set score length display to {scoreLength}")

