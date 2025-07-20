from TDStoreTools import StorageManager
import TDFunctions as TDF

import logging
import os
from datetime import datetime


class LogExt:
    """
    LogExt description
    """

    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp

    def _get_logfile_path(self):
        # Create a log file name with today's date
        log_dir = os.path.join(project.folder, "LOG")
        os.makedirs(log_dir, exist_ok=True)
        log_filename = datetime.now().strftime("%Y-%m-%d") + ".log"
        return os.path.join(log_dir, log_filename)

    def Log(self, message):
        logfile = self._get_logfile_path()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(logfile, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def CreateLogFile(self):
        logfile = self._get_logfile_path()
        
        if not os.path.exists(logfile):
            with open(logfile, "w") as f:
                f.write(f"Log file created on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
