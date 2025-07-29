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
        self.scoreFileBrowser = op('score_file_browser')
        self.scoreBrowserContainer = op('score_browser_container')


    def OpenScoreBrowser(self):
        self.scoreBrowserContainer.openViewer()
        debug("open score browse")

    def HandleLoadButton(self):
        """
        Handle the load button click event.
        """
        op.SCORE.LoadScore(self.scoreFileBrowser.par.Value0.val)
