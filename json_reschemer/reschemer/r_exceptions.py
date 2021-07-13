class MissingItemDefinitionError(Exception):
    """Exception for missing item definition

    :param Exception: Base Exception class
    :type Exception: Exception
    """

    def __init__(self):
        self.msg = \
            "No Item Defintion found upon Reschemer Initialization"

    def __str__(self):
        return f'{self.msg}'
