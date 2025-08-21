# VideoLibraryExt.py

from TDStoreTools import StorageManager
import TDFunctions as TDF
import random
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from dataclasses import dataclass, field


class Video:
    def __init__(self, videoPath):

        f = "" # STUB:  fileFrom(videoPath)

        video = {
            "path": videoPath,
            "playcount": 0,
            "length": self.GetLength(f),
            "resolution": self.GetResolution(f),
            "tags": self.GetTags(f)
        }
    
    def GetLength(self, file):
        #STUB:  get length of video from file
        videoLength = 0
        return videoLength

    def GetResolution(self, file):
        #STUB:  get resolution of video from file
        xResolution = 1920 
        yResolution = 1080
        return [xResolution, yResolution]
    
    def GetTags(self, file):
        #STUB:  get tags from somewhere metadata? another YAML file?
        return ["abstract", "crystal"]
        
class VideoLibrary:
    """Manages a collection of Video objects from a folder."""
    def __init__(self, sectionList):
        self.Library = []
        debug("creating video library")

        for section in sectionList:
            sectionName = section[0]
            sectionVideoPath = section[1]
            videoList = op.VIDEOLIBRARYMGR.GetVideoList(sectionVideoPath)

            self.Library.append([sectionName, videoList])

    def LoadSection(section):
        debug(f"STUB: Loading section: {section}")
    
    def getRandomVideo(section):
        debug(f"STUB: return random video path from {section}")

    def getUnplayedVideo(section):
        debug(f"STUB: return random video path from {section}")

    def getRandomTaggedVideo(section):
        debug(f"STUB: return random video path from {section}")

class VideoLibraryMgrExt:
    """
    op.VIDEOLIBRARYMGR is a manager for handling Video Library loading
    VideoLibrary is an object instantiated in STATE (op.STATE.VideoLibrary)
    """
    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp

    def LoadVideoLibrary(self, sectionList):
        """
        interface that generates a video Library
        from a list of section names and folders.
        """
        debug(f"loading video library {sectionList}")
        return VideoLibrary(sectionList)

    def GetVideoList(self, folderPath):
        op.LOG.Log(f"generating video file list for section {folderPath}")
        videoList = []
        files = os.listdir(folderPath)
        for file in files:
            path = os.path.join(folderPath, file)
            videoList.append({"path": path, "playedcount": 0, "tags": ["tag1","tag2"]})
        return videoList
