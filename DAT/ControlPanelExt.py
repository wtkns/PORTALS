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

        TDF.createProperty(
            self, "ScorePath", value="NULL", dependable=True, readOnly=False
        )

    def OpenControlPanel(self):
        op.LOG.Log(f"Opening Control Panel")
        self.controlPanel.openViewer()

    def HandleButtonPress(self, controller, panelName, buttonFunc):
        """
        Handle a button press event.
        """
        try:
            obj = self
            getattr(obj, buttonFunc)()
        except Exception as e:
            debug(f"Error in HandleButtonPress, (function may not exist): {e}")
            return False

    def loadScore(self):
        """
        Load the score from the file browser.
        """

        op.LOG.Log("ControlPanelExt: Load score button pressed")
        try:
            op.STATE.SetState("QUEUED")
            op.LOG.Log("ControlPanelExt: Load score completed")
        except Exception as e:
            debug(f"Error loading score: {e}")
            return


    def initScore(self):
        """
        Initialize the score.
        """
        debug("Initializing score")

    def resetScore(self):
        """
        Initialize the score.
        """
        debug("Resetting score")

    def playScore(self):
        """
        Play the score.
        """
        debug("Playing score")
    
    def pauseScore(self):
        """
        Pause the score.
        """
        debug("Pausing score")

    def nextSection(self):
        """
        Skip to the next section of the score.
        """
        debug("Next section")

    def previousSection(self):
        """
        Skip to the previous section of the score.
        """
        debug("previous section")


    def SetCurrentSectionDisplay(self, sectionNumber):
        """
        Set the current section display.
        """
        # self.sectionDisplay.par.Value0 = sectionNumber
        op.LOG.Log(f"Set current section display to {sectionNumber}")

    def SetScoreLengthDisplay(self, scoreLength):
        """
        Set the score length display.
        """
        # self.sectionDisplay.par.Value1 = scoreLength
        op.LOG.Log(f"Set score length display to {scoreLength}")
