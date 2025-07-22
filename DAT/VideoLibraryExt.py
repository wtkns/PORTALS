

from TDStoreTools import StorageManager
import TDFunctions as TDF
import random
from moviepy.video.io.VideoFileClip import VideoFileClip

class VideoLibraryExt:
    """
    VideoLibraryExt description
    """

    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp
        self.FileList = op('file_list')
        
        # properties
        TDF.createProperty(self, 'FileCount', value=self.FileList.numRows, dependable=True,
                           readOnly=False)
        

    def GetRandomVideo(self):
        if self.FileList.numRows > 0:
            random_index = random.randint(0, self.FileList.numRows - 1)
            return self.FileList.row(random_index)
        return None
    
    def GetVideoFromId(self, row_id):
        if self.FileList.numRows > 0:
            return self.FileList.row(row_id)
        return None
    
    def GetVideoDuration(self, video_path): 
        # print(op.VIDEOLIBRARY.GetVideoDuration(str(op.VIDEOLIBRARY.GetRandomVideo()[1])))
        try:
            clip = VideoFileClip(video_path)
            duration = clip.duration
            return duration
        except Exception as e:
            print(f"Error getting duration for {video_path}: {e}")
            return None
        