# ScoreExt.py
# extension that provides methods for loading the score

from TDStoreTools import StorageManager
import TDFunctions as TDF
import yaml

class Score:
    def __init__(self, yaml_path):
        with open(yaml_path, 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            if not data:
                raise ValueError("YAML file is empty or invalid")
            self.Config = data.get('config', {})
            self.Sections = data.get('sections', [])




class ScoreExt:
    """
    ScoreExt description
    SCORE is a singleton object instantiated in STATE (op.STATE.Score)
    that holds the current loaded score.
    """
    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp

    def LoadScore(self, scorePath):
        """
        Load a .YAML score from path.
        """
        if not scorePath.endswith('.yaml'):
            op.LOG.Log('Score path must end with .yaml')
            ui.messageBox('error','Score path must end with .yaml')
            return 0

        return Score(scorePath)