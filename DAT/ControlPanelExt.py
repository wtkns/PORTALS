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
        self.scoreBrowser = op('score_browser')


    def OpenScoreBrowser(self):
        self.scoreBrowser.openViewer()
        debug("open score browse")
