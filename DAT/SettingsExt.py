from TDStoreTools import StorageManager
import TDFunctions as TDF


class SettingsExt:

    def __init__(self, ownerComp):
        self.ownerComp = ownerComp

        # refer to the node_settings table op
        self.nodeSettings = op('node_settings')

        TDF.createProperty(self, 'AssetPath', value="",
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'VideoPath', value="",
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'PatternFile', value="",
                           dependable=True, readOnly=False)

    def ConfigSettings(self):
        debug("Settings: running Config")
        node = var('NODE')

        if node == 'DEVJW':
            op.LOG.Log(f'SETTINGS: Hello james, running {node}.')
            # do james things here

        elif node == 'DEVDY':
            op.LOG.Log(f'SETTINGS: Hello Dylan, running {node}.')
            # do dylan things here

        elif node == 'PROD':
            op.LOG.Log(f'SETTINGS: Hello sexy, running {node}.')
            # do live show prod things here

        else:
            node = 'DEV'
            op.LOG.Log(
                f'SETTINGS: running {node}, unknown workstation. Config NODE in portals.bat')

        # look for the paths in the node settings table
        self.AssetPath = self.nodeSettings[node, 'asset_path'].val          
        self.VideoPath = self.nodeSettings[node, 'video_path'].val

        op.LOG.Log(f'SETTINGS: AssetPath {self.AssetPath}')
        op.LOG.Log(f'SETTINGS: VideoPath {self.VideoPath}')
