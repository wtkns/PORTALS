from TDStoreTools import StorageManager
import TDFunctions as TDF


class SettingsExt:

    def __init__(self, ownerComp):
        self.ownerComp = ownerComp
        self.nodeSettings = op('node_settings')

        TDF.createProperty(self, 'AssetPath', value="",
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'VideoPath', value="",
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'PatternFile', value="",
                           dependable=True, readOnly=False)

    def ConfigSettings(self):
        op.LOG.Log('SettingsExt.ConfigSettings()')
        debug("Settings: running Config")
        node = var('NODE')

        if node == 'DEVJW':
            op.LOG.Log(f'Hello james, running {node}.')
            # do james things here

        elif node == 'DEVDY':
            op.LOG.Log(f'Hello Dylan, running {node}.')
            # do dylan things here
            
        elif node == 'PROD':
            op.LOG.Log(f'Hello sexy, running {node}.')
            # do live show prod things here

        else:
            node = 'DEV'
            op.LOG.Log(
                f'running {node}, unknown workstation. Config NODE in portals.bat')

        self.AssetPath = self.nodeSettings[node, 'asset_path'].val
        op.LOG.Log(f'Settings: AssetPath {self.AssetPath}')
        
        self.VideoPath = self.nodeSettings[node, 'video_path'].val
        op.LOG.Log(f'Settings: VideoPath {self.VideoPath}')

        self.PatternFile = self.nodeSettings[node, 'pattern_file'].val
        op.LOG.Log(f'Settings: PatternFile {self.PatternFile}')
        