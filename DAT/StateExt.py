# StateExt.py
# State tracking extension for the system.

from TDStoreTools import StorageManager
import TDFunctions as TDF


class StateExt:
    """
    handles the state of the system.
    Valid states are: INIT, STARTUP, READY, RUNNING, PAUSED, STOPPED.
    Each state represents a different phase of the system's operation.
        NULL: System is not initialized
        INIT: Initialized system, ready to LOAD SCORE.
        STARTUP: Score is loaded, ready to load videos, set up video bus, MIDI, and output.
        READY: Everything is loaded successfully. System is ready to run.
        RUNNING: System is actively processing.
        PAUSED: System is paused, can resume or stop.
        STOPPED: System is stopped or in an Error State, must be reset.
    Handles the state transitions and logs the state changes.
    """

    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp
        self.validStates = ["INIT", "STARTUP", "READY", "RUNNING", "PAUSED", "STOPPED"]

        # properties
        TDF.createProperty(self, "State", value="NULL", dependable=True, readOnly=False)
        TDF.createProperty(self, "Score", value="NULL", dependable=True, readOnly=False) # holds the current loaded score SINGLETON OBJECT

    def validState(self, state):
        """
        Check if the state is valid.
        """
        return state in self.validStates

    def GetState(self):
        """
        returns the current state of the system.
        """
        return self.State

    def SetState(self, new_state):
        """
        Interface to set the current state of the system.
        """
        if self.validState(new_state):
            self.handleSetState(new_state)
        else:
            op.LOG.Log(
                f"StateExt: Invalid state {new_state}. Valid states are: {self.validStates}"
            )

    def handleSetState(self, new_state):
        # Initialize the state of the component
        match new_state:
            case "INIT":
                # Initialized system, ready to LOAD SCORE
                self.State = "INIT"
                op.CONTROLPANEL.OpenControlPanel()
                op.LOG.Log("StateExt: Initialized to INIT")

            case "STARTUP":
                # Score is loaded, ready to load videos, set up video bus, and output
                self.State = "STARTUP"
                op.LOG.Log("StateExt: Initialized to STARTUP")

            case "READY":
                self.State = "READY"
                op.LOG.Log("StateExt: Initialized to READY")

            case "RUNNING":
                self.State = "RUNNING"
                op.LOG.Log("StateExt: Initialized to RUNNING")

            case "PAUSED":
                self.State = "PAUSED"
                op.LOG.Log("StateExt: Initialized to PAUSED")

            case "STOPPED":
                self.State = "STOPPED"
                op.LOG.Log("StateExt: Initialized to STOPPED")

            case _:
                op.LOG.Log(f"StateExt: Unrecognized state {new_state}")
