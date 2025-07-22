

from TDStoreTools import StorageManager
import TDFunctions as TDF


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

        