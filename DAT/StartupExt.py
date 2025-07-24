from TDStoreTools import StorageManager
import TDFunctions as TDF

import os
import sys


class StartupExt:
    """
    StartupExt description
    """

    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp

    def addDependenciesToPath(self):
        op.LOG.Log('STARTUP: addDependenciesToPath()')
        dep_path = f'{project.folder}/DEP/PYTHON'
        norm_dep_path = os.path.normpath(dep_path)

        if norm_dep_path not in sys.path:
            op.LOG.Log(f'ADDING: {norm_dep_path} to sys.path')
            sys.path.insert(0, norm_dep_path)
        else:
            op.LOG.Log(f'EXISTS: {norm_dep_path} in sys.path')

    def Startup(self):
        op.LOG.CreateLogFile()
        op.LOG.Log('STARTUP: Startup initiated')
        
        self.addDependenciesToPath()
        op.SETTINGS.ConfigSettings()

        op.LOG.Log('STARTUP: Startup Completed')
        op.LOG.Log('+++++++++++++++++++++++++++++++++++++++++++++++')
        op.STATE.Set('INIT')
        
