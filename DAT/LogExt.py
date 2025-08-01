# LogExt.py
# Provides methods to create, write, and manage log files.

from TDStoreTools import StorageManager
import TDFunctions as TDF

import logging
import os
from datetime import datetime


class LogExt:
    """
    Simple logging extension for the project.

    Public methods:
        - CreateLogFile: Creates a log file with today's date.
        - Log: Writes a message to the log file with a timestamp.
        - DumpLog: Reads and returns the content of the log file.
        - ClearLog: Clears the content of the log file.
    Private methods:
        - get_logfile_path: Returns the path to the log file based on today's date.
    Public Attributes:
        - LogFile: The path to the log file.
    """

    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp
        TDF.createProperty(self, "LogFile", value="", dependable=True, readOnly=False)

    def get_logfile_path(self):
        # Create a log file name with today's date
        log_dir = os.path.join(project.folder, "LOG")
        os.makedirs(log_dir, exist_ok=True)
        log_filename = datetime.now().strftime("%Y-%m-%d") + ".log"
        return os.path.join(log_dir, log_filename)

    def CreateLogFile(self):
        self.LogFile = self.get_logfile_path()
        if not os.path.exists(self.LogFile):
            with open(self.LogFile, "w") as f:
                f.write(
                    f"Log file created on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                )

    def Log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.LogFile, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def DumpLog(self):
        if not os.path.exists(self.LogFile):
            debug("ERROR: Log file does not exist.")
            return

        with open(self.LogFile, "r") as f:
            log_content = f.read()
            op.LOG.Log(f"Log content:\n{log_content}")
            return log_content

    def ClearLog(self):
        if os.path.exists(self.LogFile):
            with open(self.LogFile, "w") as f:
                f.write(
                    f"Log cleared on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                )
            op.LOG.Log("Log file cleared.")
        else:
            debug("Log file does not exist, nothing to clear.")
