# SettingsExt.py

from TDStoreTools import StorageManager
import TDFunctions as TDF
from datetime import datetime


class SettingsExt:

    def __init__(self, ownerComp):
        self.ownerComp = ownerComp

        TDF.createProperty(self, 'ProjectPath', value=project.folder,
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'Node', value=var('NODE'),
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'AssetPath', value="",
                           dependable=True, readOnly=False)

    def InitializeSettings(self):
        nodeSettings = op('node_settings')
        op.LOG.Log("SETTINGS: InitializeSettings()")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if self.Node == 'DEVJW':
            op.LOG.Log(f'Session [{timestamp}]: Hello james, running {self.Node}.')
            # do james things here
        elif self.Node == 'DEVJWL':
            op.LOG.Log(f'Session [{timestamp}]: Hello james, running {self.Node} on your laptop.')
            # do laptop things here
        else:
            op.LOG.Log(f'Session [{timestamp}]: running {self.Node}, unknown workstation. Config NODE in portals.bat')
            return
        self.AssetPath = nodeSettings[self.Node, 'asset_path'].val

    
    def GetConfigDict(self): 
        op.LOG.Log(f'SETTINGS: GetConfigDict()')
        return {
            'node': self.Node,
            'project_path': self.ProjectPath,
            'asset_path': self.AssetPath
        }
