# VideoLibraryExt.py

from TDStoreTools import StorageManager
import TDFunctions as TDF
import random
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from dataclasses import dataclass, field


class Video:
    def __init__(self, videoPath):

        f = "" # fileFrom(videoPath)

        video = {
            "path": videoPath,
            "playcount": 0,
            "length": 0, #getLength(f),
            "resolution": self.GetResolution(f),
            "tags": []
        }
    
    def GetLength(self, file):
        # get length of video from file
        videoLength = 0
        return videoLength

    def GetResolution(self, file):
        # get resolution of video from file
        xResolution = 1920 
        yResolution = 1080
        return [xResolution, yResolution]
        
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
        debug(f"Loading section: {section}")
    
    def getRandomVideo(section):
        debug(f"return random video path from {section}")

    def getUnplayedVideo(section):
        debug(f"return random video path from {section}")

    def getRandomTaggedVideo(section):
        debug(f"return random video path from {section}")

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
        debug(f"generating video file list for section {folderPath}")
        videoList = []
        files = os.listdir(folderPath)
        for file in files:
            debug(f"file name: {file}")
            videoList.append({"path": file, "playedcount": 0, "tags": ["tag1","tag2"]})

        return videoList
