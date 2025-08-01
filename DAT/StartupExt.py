# StartupExt.py
# Provides methods to initialize system.

from TDStoreTools import StorageManager
import TDFunctions as TDF
import os
import sys


class StartupExt:
    """
    Extension class for project startup initialization.

    Public Methods:
        - Startup():
            Called on project start (e.g., by op.STARTUP.execute1.onStart).
            Responsibilities:
                1. Reset the timeline.
                2. Set up the log file.
                3. Initialize project settings.
                4. Add dependencies path to sys.path.
                5. Set the initial state to 'INIT'.

    Private Methods:
        - getDependenciesPath():
            Returns the path to the dependencies folder.
        - addDependenciesToPath(dep_path):
            Adds the dependencies path to sys.path if not already present.

    Attributes:
        - ownerComp: The component to which this extension is attached.

    Notes:
        - Consider improving dependency and error handling in future revisions.
    """

    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp

    def getDependenciesPath(self):
        return f"{op.SETTINGS.ProjectPath}/DEP/PYTHON"

    def addDependenciesToPath(self, dep_path):
        norm_dep_path = os.path.normpath(dep_path)
        if norm_dep_path not in sys.path:
            sys.path.insert(0, norm_dep_path)
            op.LOG.Log(f"ADDING: {norm_dep_path} to sys.path")
        else:
            op.LOG.Log(f"EXISTS: {norm_dep_path} in sys.path")

    def Startup(self):
        me.time.play = 0 # Stop the timeline
        me.time.frame = 0 # Reset the timeline frame to 0
        op.LOG.CreateLogFile()
        op.LOG.Log("++++ STARTUP.Startup() called ++++")
        op.SETTINGS.InitializeSettings()
        self.addDependenciesToPath(self.getDependenciesPath())
        op.STATE.SetState("INIT")
        op.LOG.Log("++++ STARTUP: Startup Completed ++++")
