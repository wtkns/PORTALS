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

    def Startup(self):
        """Main startup routine called on project start."""
        try:
            op.LOG.CreateLogFile()
        except Exception as e:
            debug("FAILED TO CREATE LOG FILE")

        try:
            op.LOG.Log("++++ STARTUP.Startup() called ++++")
            op.STATE.SetState("INIT")
            op.LOG.Log("++++ STARTUP: Startup Completed ++++")
        except Exception as e:
            op.STATE.SetState("ERROR")
            op.LOG.Log(f"STARTUP ERROR: {e}")
