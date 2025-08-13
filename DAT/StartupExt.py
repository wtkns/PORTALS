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
        # Subpath for dependencies
        self.DEPENDENCIES_SUBPATH = "/DEP/PYTHON"

    def get_dependencies_path(self):
        """Return the absolute path to the dependencies folder."""
        return os.path.join(op.SETTINGS.ProjectPath, self.DEPENDENCIES_SUBPATH)

    def add_dependencies_to_path(self, dep_path):
        """Add the dependencies path to sys.path if not already present."""
        norm_dep_path = os.path.normpath(dep_path)
        if norm_dep_path not in sys.path:
            sys.path.insert(0, norm_dep_path)
            op.LOG.Log(f"ADDING: {norm_dep_path} to sys.path")
        else:
            op.LOG.Log(f"EXISTS: {norm_dep_path} in sys.path")

    def reset_timeline(self):
        """Reset the timeline to frame 0 and stop playback."""
        me.time.play = 0
        me.time.frame = 0

    def initialize_settings(self):
        """Initialize project settings."""
        op.SETTINGS.InitializeSettings()

    def Startup(self):
        """Main startup routine called on project start."""
        try:
            self.reset_timeline()
            op.LOG.CreateLogFile()
            op.LOG.Log("++++ STARTUP.Startup() called ++++")
            self.initialize_settings()
            self.add_dependencies_to_path(self.get_dependencies_path())
            op.STATE.SetState("INIT")
            op.LOG.Log("++++ STARTUP: Startup Completed ++++")
        except Exception as e:
            op.LOG.Log(f"STARTUP ERROR: {e}")
