# ScoreExt.py
# extension that provides methods for loading the score

from TDStoreTools import StorageManager
import TDFunctions as TDF
import yaml
import os

class Score:
    def __init__(self, yaml_path):
        with open(yaml_path, 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            if not data:
                raise ValueError("YAML file is empty or invalid")
            self.Config = data.get('config', {})
            self.Path = self.Config.get('root_path', yaml_path)
            self.Sections = data.get('sections', [])
            self.MidiMap = data.get('midi_map', {})

    def GetPath(self):
        """
        Get the root path of the score.
        """
        return self.Path

    def GetSection(self, index):
        """
        Get a section by index.
        """
        if 0 <= index < len(self.Sections):
            return self.Sections[index]
        return None

    def GetSectionName(self, index):
        """
        Get a section by index.
        """
        section = self.GetSection(index)
        if section:
            return section.get('name', None)
        return None

    def GetSectionVideoFolder(self, index):
        """
        Get the file path of a section by index.
        """
        section = self.GetSection(index)
        if section:
            full_path = os.path.join(self.Path, section.get('video_folder', ''))
            return full_path
        return None

class ScoreMgrExt:
    """
    SCOREMGR is a manager for handling score loading and playback.
    Score is an object instantiated in STATE (op.STATE.Score)
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