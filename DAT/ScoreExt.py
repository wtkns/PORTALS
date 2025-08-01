# ScoreExt.py
# extension that provides methods for loading the score

from TDStoreTools import StorageManager
import TDFunctions as TDF
import yaml

# class Score:
#     def __init__(self, ownerComp):
#         self.Path = ""
#         self.Name = ""
#         self.Sections = [] 
#         self.CurrentSection = 0
#         self.VideoLibrary = {}


class ScoreExt:
    """
    ScoreExt description
    SCORE is a singleton object instantiated in STATE (op.STATE.Score)
    that holds the current loaded score.
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
        TDF.createProperty(self, 'CurrentSection', value=0,
                    dependable=True, readOnly=False)
        TDF.createProperty(self, 'VideoLibrary', value={},
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

            self.ResetScore()
            self.ScorePath = scorePath
            op.SETTINGS.ReadConfigDict(data['config'])
            self.readScore(data['sections'])
            # op.VIDEOLIBRARY.
            op.CONTROLPANEL.SetCurrentSectionDisplay(0)
            op.CONTROLPANEL.SetScoreLengthDisplay(len(data['sections']))
        return self



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
        op.LOG.Log(f'Sections loaded successfully, section count: {len(self.SectionList)}')

    def addSection(self, sectionDict):
        """
        Add a section to the score.
        """
        self.SectionList.append(sectionDict)
        op.LOG.Log(f'Section added: {sectionDict}')
    
    def GetCurrentSection(self):
        """
        Get the current section.
        """
        if self.CurrentSection < len(self.SectionList):
            return self.SectionList[self.CurrentSection]
        else:
            op.LOG.Log('Current section index out of range')
            return None

    def ResetScore(self):
        """
        Reset the score to its initial state.
        """
        self.ScorePath = ""
        self.ScoreName = ""
        self.SectionList = []
        self.CurrentSection = 0
        op.LOG.Log('Score reset to initial state')

    def NextSection(self):
        op.CONTROLPANEL.HandleNextSectionButton()
        op.LOG.Log('NextSection called')

    def PreviousSection(self):
        op.CONTROLPANEL.HandlePreviousSectionButton()
        op.LOG.Log('PreviousSection called')

