

from TDStoreTools import StorageManager
import TDFunctions as TDF
import random
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from dataclasses import dataclass, field

@dataclass
class Video:
    """Represents a single video file with its metadata."""
    path: str
    tag: str # The subfolder name
    duration: float
    played_count: int = 0

    def __repr__(self):
        return f"Video(path='{os.path.basename(self.path)}', tag='{self.tag}', duration={self.duration:.2f}s)"

    def played(self):
        """Increments the play count for this video."""
        self.played_count += 1
        
class Playlist:
    """Manages a collection of Video objects from a folder."""
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        self.videos: list[Video] = []
        self.current_index: int = -1
    
    def populate_videos(self):
        """Scans the folder and populates the video list."""
        print(f"Scanning '{self.folder_path}' for videos...")
        for subdir, _, files in os.walk(self.folder_path):
            for file in files:
                # Simple check for common video extensions
                if file.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):
                    full_path = os.path.join(subdir, file)
                    tag = os.path.basename(subdir)
                    try:
                        # Get duration without loading the whole video into memory
                        with VideoFileClip(full_path) as clip:
                            duration = clip.duration
                        
                        video_obj = Video(path=full_path, tag=tag, duration=duration)
                        self.videos.append(video_obj)
                    except Exception as e:
                        print(f"Could not process {full_path}: {e}")
        
        random.shuffle(self.videos) # Start with a random order
        print(f"Found {len(self.videos)} videos.")
    
    def get_next_video(self) -> Video | None:
        """Gets the next video in the shuffled list, looping back to the start."""
        if not self.videos:
            return None
        
        self.current_index = (self.current_index + 1) % len(self.videos)
        video = self.videos[self.current_index]
        video.played()
        return video

    def get_random_unplayed_video(self) -> Video | None:
        """Gets a random video that has not been played in this session."""
        unplayed = [v for v in self.videos if v.played_count == 0]

        if not unplayed:
            print("All videos have been played! Resetting play counts.")
            # Optional: Reset all counts if you run out of unplayed videos
            for v in self.videos:
                v.played_count = 0
            unplayed = self.videos

        if not unplayed: # Still no videos
            return None

        video = random.choice(unplayed)
        video.played()
        return video
        

class VideoLibraryExt:
    """
    VideoLibraryExt description
    # e.g op.VIDEOLIBRARY.GetRandomVideo()
    """

    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp
        self.FileList = op('file_list')
        self.Root = op.SETTINGS.VideoPath
        
        # properties
        TDF.createProperty(self, 'FileCount', value=self.FileList.numRows, dependable=True,
                           readOnly=False)

        TDF.createProperty(self, 'VideoPlaylist', value=Playlist(folder_path=self.Root), dependable=True,
                           readOnly=False)

        my_playlist = self.VideoPlaylist
        # my_playlist.populate_videos()
        
    def GetRandomVideo(self):
        # op.VIDEOLIBRARY.GetRandomVideo()
        my_playlist = self.VideoPlaylist
        video = my_playlist.get_random_unplayed_video()
        return video

    def GetNextVideo(self):
        # op.VIDEOLIBRARY.GetNextVideo()
        my_playlist = self.VideoPlaylist
        video = my_playlist.get_next_video()
        return video

