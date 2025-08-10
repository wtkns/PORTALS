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

    def HandleButtonPress(self, panelName, buttonFunc):
        """
        Handle a button press event.
        """
        debug(f"CONTROLPANEL Button pressed: {panelName}, {buttonFunc}")

        if buttonFunc == "loadScore":
            self.HandleLoadButton()
        elif buttonFunc == "next":
            self.HandleNextSectionButton()
        elif buttonFunc == "previous":
            self.HandlePreviousSectionButton()

        op.LOG.Log(f"HandleButtonPress: {buttonFunc}")

    def HandleLoadButton(self):
        """
        Handle the load button click event.
        """
        # scoreFilePath = self.scoreFileBrowser.par.Value0.val
        # self.ScorePath = scoreFilePath
        # op.LOG.Log(f"Load Score button clicked: {self.ScorePath}")
        debug(f"Load Score button clicked")
        # op.STATE.SetState("STARTUP")

    def HandleNextSectionButton(self):
        """
        if next section is available, increment current section
        """
        op.LOG.Log(f"HandleNextSectionButton called")
        debug(f"HandleNextSectionButton called")
        # if op.SCORE.CurrentSection < len(op.SCORE.SectionList) - 1:
        # 	op.SCORE.CurrentSection += 1
        # 	op.SCORE.SetCurrentSectionDisplay(op.SCORE.CurrentSection)
        # 	op.LOG.Log(f"Current section incremented to {op.SCORE.CurrentSection}")

    def HandlePreviousSectionButton(self):
        """
        if previous section is available, decrement current section
        """
        op.LOG.Log(f"HandlePreviousSectionButton called")
        debug(f"HandlePreviousSectionButton called")

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

    def HandleStartupButton(self):
        """
        Handle the startup button click event.
        """
        op.LOG.Log(f"Startup button clicked")
        op.STATE.SetState("STARTUP")
