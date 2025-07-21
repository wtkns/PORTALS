

from TDStoreTools import StorageManager
import TDFunctions as TDF


class VideoLibraryExt:
    """
    VideoLibraryExt description
    """

    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp

        # properties
        TDF.createProperty(self, 'FileCount', value=0, dependable=True,
                           readOnly=False)
        self.FileCount = len(self.FileList)-1

    def myFunction(self, v):
        debug(v)

    def PromotedFunction(self, v):
        debug(v)
