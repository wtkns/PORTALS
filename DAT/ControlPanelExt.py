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

    def HandleLoadButton(self):
        """
        Handle the load button click event.
        """
        debug(op.CONTROLPANEL.ScoreFileBrowser)
        
        # op.LOG.log("Load button clicked.")
        # op.LOG.log(op.CONTROLPANEL.ScoreFileBrowser)

        # if button == 'load':
        #     scoreName = self.scoreBrowser.getSelectedScoreName()
        #     if scoreName:
        #         self.LoadScore(scoreName)
        #     else:
        #         debug("No score selected to load.")
        # else:
        #     debug(f"Unhandled button: {button}")
            
        
    # def loadScore(self, scorePath):
    #     """
    #     Load a score by name.
    #     """
    #     if not scoreName:
    #         return

    #     # Load the score from the storage
    #     score = StorageManager.load(scoreName)
    #     if score:
    #         self.scoreBrowser.setScore(score)
    #         debug(f"Loaded score: {scoreName}")
    #     else:
    #         debug(f"Score not found: {scoreName}")