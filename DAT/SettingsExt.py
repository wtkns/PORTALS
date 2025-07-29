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
        TDF.createProperty(self, 'AudioDevice', value="",
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'MidiDevice', value="",
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'MidiChannel', value="",
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'MidiMap', value={},
                           dependable=True, readOnly=False) 

    def ConfigSettings(self):
        op.LOG.Log("SETTINGS: ConfigSettings()")
        node = var('NODE')

        if node == 'DEVJW':
            op.LOG.Log(f'SETTINGS: Hello james, running {node}.')
            # do james things here

        elif node == 'DEVJWL':
            op.LOG.Log(f'SETTINGS: Hello james, running {node} on your laptop.')
            # do dylan things here

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

    def ReadConfigDict(self, config_dict):
        op.LOG.Log(f'SETTINGS: ReadConfigDict({config_dict})')
        self.AudioDevice = config_dict.get('audio_device', '')
        self.MidiDevice = config_dict.get('midi_device', '')
        self.MidiChannel = config_dict.get('midi_channel', '')
        self.MidiMap = config_dict.get('midi_map', {})
    
    def GetConfigDict(self): 
        op.LOG.Log(f'SETTINGS: GetConfigDict()')
        return {
            'asset_path': self.AssetPath,
            'video_path': self.VideoPath,
            'audio_device': self.AudioDevice,
            'midi_device': self.MidiDevice,
            'midi_channel': self.MidiChannel,
            'midi_map': self.MidiMap
        }
