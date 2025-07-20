"""
Extension classes enhance TouchDesigner components with python. An
extension is accessed via ext.ExtensionClassName from any operator
within the extended component. If the extension is promoted via its
Promote Extension parameter, all its attributes with capitalized names
can be accessed externally, e.g. op('yourComp').PromotedFunction().

Help: search "Extensions" in wiki
"""

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
        dep_path = f'{project.folder}/DEP/PYTHON'
        norm_dep_path = os.path.normpath(dep_path)
        op.LOG.Log(f'adding {norm_dep_path} to sys path')

        if norm_dep_path not in sys.path:
            op.LOG.Log(f'adding {norm_dep_path} to sys path')
            sys.path.insert(0, norm_dep_path)

    def Startup(self):
        self.addDependenciesToPath()
        op.LOG.Log('startupExt.Startup()')
