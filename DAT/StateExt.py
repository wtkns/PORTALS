# StateExt.py
# State tracking extension for the system.

from TDStoreTools import StorageManager
import TDFunctions as TDF
from enum import Enum


class SystemState(Enum):
    """
    Each state represents a different phase of the system's operation.
    """

    NULL = "NULL"  # System is not initialized
    INIT = "INIT"  # Initialized system, ready to LOAD SCORE.
    QUEUED = (
        "QUEUED"  # Score is loaded, MIDI, Video Library, and Output Window are ready.
    )
    RUNNING = "RUNNING"  # System is actively processing.
    PAUSED = "PAUSED"  # System is paused, can resume or stop.
    STOPPED = "STOPPED"  # System Stopped.
    ERROR = "ERROR"  # System is in an Error State


class StateExt:
    """
    handles the state of the system.
    Valid states are: INIT, STARTUP, READY, RUNNING, PAUSED, STOPPED.
    Handles the state transitions and logs the state changes.
    """

    def __init__(self, ownerComp):
        self.ownerComp = ownerComp  # The component to which this extension is attached

        self.state_handlers = {
            SystemState.INIT: self._handle_startup,
            SystemState.QUEUED: self._handle_load,
            SystemState.RUNNING: self._handle_play,
            SystemState.PAUSED: self._handle_pause,
            SystemState.STOPPED: self._handle_stop,
            SystemState.ERROR: self._handle_halt,
        }

        # properties
        TDF.createProperty(self, "SessionState", value="NULL", dependable=True, readOnly=False)
        TDF.createProperty(self, "SessionScore", value="NULL", dependable=True, readOnly=False)
        TDF.createProperty(
            self, "SessionVideoLibrary", value="[]", dependable=True, readOnly=False
        )

        TDF.createProperty(
            self, "SessionCurrentSection", value="0", dependable=True, readOnly=False
        )

    def validState(self, state):
        """
        Check if the state is valid.
        """
        return state in self.validStates

    def GetState(self):
        """
        returns the current state of the system.
        """
        return self.SessionState

    def SetState(self, new_state):
        """
        Interface to set the current state of the system.
        """
        try:
            state_enum = SystemState(new_state)
        except ValueError:
            badStateMessage = f"StateExt: Invalid state {new_state}. Valid states are: {[s.value for s in SystemState]}"
            op.LOG.Log(badStateMessage)
            debug(badStateMessage)
            return

        handler = self.state_handlers.get(state_enum)
        if handler:
            handler()
        else:
            op.LOG.Log(f"StateExt: No handler for state {new_state}")

    def _handle_startup(self):
        """
        Initial startup routine,
        stops and resets timeline,
        opens control panel.
        called by STARTUP.Startup() and
        STATE.Reset
        """
        me.time.play = 0
        me.time.frame = 0
        try:
            op.SETTINGS.InitializeSettings()
        except Exception as e:
            op.LOG.Log(f"++++ initialization error: {e} ++++")
        op.CONTROLPANEL.OpenControlPanel()
        self.SessionState = SystemState.INIT.value
        op.LOG.Log("SessionState: Initialized to INIT")

    def _handle_load(self):
        """
        Routine that
        1. loads the score,
        2. opens the first section
        3. prepares the video library
        4. initalizes the MIDI listener
        5. opens the output window
        """

        # get the score file path from the CONTROLPANEL
        # scoreFileBrowserOp = op.scoreFileBrowser

        # get the score object from SCOREMGR.LoadScore
        try:
            filePath = op.scoreFileBrowser.par.Value0.eval()
            self.SessionScore = op.SCOREMGR.LoadScore(filePath)

        except Exception as e:
            debug(f"Error loading score from file browser: {e}")
            return

        op.LOG.Log(f"Loaded {filePath} score from file browser")

        # get structured list of section names and paths for all videos for all sections
        # like: [["test-intro", "test-intro-path"], ["test-section A", "test-section A path"]]
        scoreLibraryList = self.SessionScore.GetLibraryList()

        debug(f"ScoreLibraryList: {scoreLibraryList}")

        # generate video Library
        try:
            self.SessionVideoLibrary = op.VIDEOLIBRARYMGR.LoadVideoLibrary(scoreLibraryList)

        except Exception as e:
            debug(f"Error loading video library: {e}")
            return

        op.LOG.Log(f"Loaded {self.SessionVideoLibrary.Library} from score")
        op.LOG.Log(f"Loaded {self.SessionVideoLibrary.Library} from score")
 
        # set section display
        op.CONTROLPANEL.SetCurrentSectionDisplay(self.SessionScore.GetCurrentSectionIndex())
        op.CONTROLPANEL.SetScoreLengthDisplay(self.SessionScore.GetLastSectionIndex())

        # # Open Output window
        # # op.WINDOW.OpenWindow(2)
        # op.LOG.Log(
        #     f"OPENING WINDOW: monitor number {self.SessionScore.Monitor}, size: {self.SessionScore.Resolution[0]} X {self.SessionScore.Resolution[1]}"
        # )

        self.SessionState = SystemState.QUEUED.value
        op.LOG.Log("SessionState: transitioned to QUEUED")

    def _handle_play(self):
        self.SessionState = SystemState.RUNNING.value
        op.LOG.Log("SessionState: transitioned to READY")

    def _handle_pause(self):
        self.SessionState = SystemState.PAUSED.value
        op.LOG.Log("SessionState: transitioned to RUNNING")

    def _handle_stop(self):
        self.SessionState = SystemState.QUEUED.value
        op.LOG.Log("SessionState: transitioned to QUEUED")

    def _handle_halt(self):
        self.SessionState = SystemState.ERROR.value
        op.LOG.Log("SessionState: Initialized to STOPPED")
