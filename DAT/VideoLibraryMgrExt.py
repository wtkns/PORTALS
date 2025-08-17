# VideoLibraryExt.py

from TDStoreTools import StorageManager
import TDFunctions as TDF
import random
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from dataclasses import dataclass, field
        
class VideoLibrary:
    """Manages a collection of Video objects from a folder."""
    def __init__(self, sectionList):
        self.SectionList = sectionList
    
    def LoadSection(section)
        debug(f"Loading section: {section}")
    

class VideoLibraryMgrExt:
    """
    op.VIDEOLIBRARYMGR is a manager for handling Video Library loading
    VideoLibrary is an object instantiated in STATE (op.STATE.VideoLibrary)
    """
    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp

    def LoadVideoLibrary(self, section_list):
        """
        interface that generates a video Library
        from a list of section names and folders.
        """
        # error checking
        #    return 0

        return VideoLibrary(section_list)