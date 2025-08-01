# ExtensionName.py
# Provides short description of the extension's purpose.

from TDStoreTools import StorageManager
import TDFunctions as TDF


class ExtensionName:
    """
    Extension class description.

    Public Methods:
        - PublicMethodName():
            short description. if it is a complex method, describe its responsibilities. 
            Responsibilities:
                1. responsibility one
                2. responsibility two
            Args:
                - arg1: description of arg1
                - arg2: description of arg2
            Returns:
                - return_value: description of return value

    Private Methods:
        - privateMethodName():
            short description. if it is a complex method, describe its responsibilities. 
            Responsibilities:
                1. responsibility one
                2. responsibility two
            Args:
                - arg1: description of arg1
                - arg2: description of arg2
            Returns:
                - return_value: description of return value

    Public Attributes:
        - PublicAttributeName: description of the public attribute.

    Notes:
        - short notes if necessary, e.g., planned improvements, known issues, etc.
        - Consider improving dependency and error handling in future revisions.
    """

    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp

        # Public Properties
        TDF.createProperty(
            self, "State", value="uninit", dependable=True, readOnly=False
        )
