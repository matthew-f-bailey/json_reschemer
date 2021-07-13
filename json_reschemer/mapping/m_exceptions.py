

class MissingDefinitionError(Exception):
    """Error raised when input mappings were missing the key "ITEM_DEFINITION"

    :param Exception: Base Exception class
    :type Exception: Exception
    """

    def __init__(self, msg) -> None:
        self.msg = msg

    def __str__(self):
        return self.msg
