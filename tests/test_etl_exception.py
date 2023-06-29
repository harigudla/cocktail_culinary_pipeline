"""Tests for etl_exception.py module. """

import pytest
from etl.etl_exceptions import EtlExecutionException


# Arrange
@pytest.fixture(scope='module')
def etl_exception_instance():
    """Initialize and return EtlExecutionException instance. """
    
    message = "An error occurred during the ETL process."
    exception = EtlExecutionException(message)
    return exception


def test_exception_message(etl_exception_instance):
    """Test exception message.

    Args:
        etl_exception_instance (obj): Pytest fixture for EtlExecutionException instance.
        
    """

    message = "An error occurred during the ETL process."
    assert str(etl_exception_instance) == message


def test_exception_type(etl_exception_instance):
    """Test exception type.

    Args:
        etl_exception_instance (obj): Pytest fixture for EtlExecutionException instance.

    """
    assert isinstance(etl_exception_instance, Exception)
    assert isinstance(etl_exception_instance, EtlExecutionException)


