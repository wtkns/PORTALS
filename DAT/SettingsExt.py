# SettingsExt.py

from TDStoreTools import StorageManager
import TDFunctions as TDF


class SettingsExt:

    def __init__(self, ownerComp):
        self.ownerComp = ownerComp

        TDF.createProperty(self, 'ProjectPath', value=project.folder,
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'Node', value=var('NODE'),
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'AssetPath', value="",
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'AudioDevice', value="",
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'MidiDevice', value="",
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'MidiChannel', value="",
                           dependable=True, readOnly=False)
        TDF.createProperty(self, 'MidiMap', value={},
                           dependable=True, readOnly=False) 

    def InitializeSettings(self):
        nodeSettings = op('node_settings')
        op.LOG.Log("SETTINGS: InitializeSettings()")
        if self.Node == 'DEVJW':
            op.LOG.Log(f'SETTINGS: Hello james, running {self.Node}.')
            # do james things here
        elif self.Node == 'DEVJWL':
            op.LOG.Log(f'SETTINGS: Hello james, running {self.Node} on your laptop.')
            # do laptop things here
        else:
            op.LOG.Log(f'SETTINGS: running {self.Node}, unknown workstation. Config NODE in portals.bat')
            return
        self.AssetPath = nodeSettings[self.Node, 'asset_path'].val

    def SetConfigFromScore(self, config_dict):
        self.AudioDevice = config_dict.get('audio_device', '')
        self.MidiDevice = config_dict.get('midi_device', '')
        self.MidiChannel = config_dict.get('midi_channel', '')
        self.MidiMap = config_dict.get('midi_map', {})
        op.LOG.Log(f'SETTINGS: Config Imported {self.GetConfigDict()}')
    
    def GetConfigDict(self): 
        op.LOG.Log(f'SETTINGS: GetConfigDict()')
        return {
            'node': self.Node,
            'project_path': self.ProjectPath,
            'asset_path': self.AssetPath,
            'audio_device': self.AudioDevice,
            'midi_device': self.MidiDevice,
            'midi_channel': self.MidiChannel,
            'midi_map': self.MidiMap
        }
