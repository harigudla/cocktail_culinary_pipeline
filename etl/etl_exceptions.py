"""Used defined etl exception class. """


class EtlExecutionException(Exception):
    """A custom exception for representing errors in etl execution.

    Args:
        Exception (obj): Base class for all python exceptions.

    """

    def __init__(self, message):
        """ Initializes a new EtlExecutionException object with the specified error message.

        Args:
            message (str): The error message for the exception.

        """

        self.message = message