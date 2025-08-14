# SettingsExt.py

from TDStoreTools import StorageManager
import TDFunctions as TDF
from datetime import datetime
import os
import sys


class SettingsExt:

    def __init__(self, ownerComp):
        self.ownerComp = ownerComp

        TDF.createProperty(
            self, "ProjectPath", value=project.folder, dependable=True, readOnly=False
        )
        TDF.createProperty(
            self, "Node", value=var("NODE"), dependable=True, readOnly=False
        )
        TDF.createProperty(self, "AssetPath", value="", dependable=True, readOnly=False)
        # Subpath for dependencies
        self.DEPENDENCIES_SUBPATH = "/DEP/PYTHON"

    def InitializeSettings(self):
        nodeSettings = op("node_settings")
        op.LOG.Log("SETTINGS: InitializeSettings()")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if self.Node == "DEVJW":
            op.LOG.Log(f"Session [{timestamp}]: Hello james, running {self.Node}.")
            # do james things here
        elif self.Node == "DEVJWL":
            op.LOG.Log(
                f"Session [{timestamp}]: Hello james, running {self.Node} on your laptop."
            )
            # do laptop things here
        else:
            op.LOG.Log(
                f"Session [{timestamp}]: running {self.Node}, unknown workstation. Config NODE in portals.bat"
            )
            return
        self.AssetPath = nodeSettings[self.Node, "asset_path"].val
        self.add_dependencies_to_path(self.get_dependencies_path())

    def get_dependencies_path(self):
        """Return the absolute path to the dependencies folder."""
        return os.path.join(self.ProjectPath, self.DEPENDENCIES_SUBPATH)

    def add_dependencies_to_path(self, dep_path):
        """Add the dependencies path to sys.path if not already present."""
        norm_dep_path = os.path.normpath(dep_path)
        if norm_dep_path not in sys.path:
            sys.path.insert(0, norm_dep_path)
            op.LOG.Log(f"ADDING: {norm_dep_path} to sys.path")
        else:
            op.LOG.Log(f"EXISTS: {norm_dep_path} in sys.path")

    def GetConfigDict(self):
        op.LOG.Log(f"SETTINGS: GetConfigDict()")
        return {
            "node": self.Node,
            "project_path": self.ProjectPath,
            "asset_path": self.AssetPath,
        }
