# app/views/validators.py
# Created at: Mon Feb 08 2021 11:40:42 GMT+0100 (Central European Standard Time)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
app/views/validators.py
INSERT docstring paragraph

Example:
        INSERT example

Todo:
        * INSERT TODO lines
        *

.. _Google Python Style Guide (reference):
http://google.github.io/styleguide/pyguide.html
"""

# pylint: disable=import-error
# Futures

# Generic/Built-in
from datetime import datetime

# Other Libs
from dateparser import parse
from PyInquirer import Validator, ValidationError

# Owned

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


# pylint: disable=too-few-public-methods
class NumberValidator(Validator):
    """NumberValidator.
    """

    # pylint: disable=raise-missing-from
    # pylint: disable=no-self-use
    def validate(self, document):
        """Summary of validate.

        Args:
            document

        Raises:
            ValidationError
        """
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Entrez un nombre',
                cursor_position=len(document.text))  # Move cursor to end
        try:
            assert int(document.text) > 0
        except AssertionError:
            raise ValidationError(
                message='Entrez un nombre plus grand que 0',
                cursor_position=len(document.text))  # Move cursor to end


# pylint: disable=too-few-public-methods
class StringValidator(Validator):
    """StringValidator.
    """

    # pylint: disable=raise-missing-from
    # pylint: disable=no-self-use
    def validate(self, document):
        """Summary of validate.

        Args:
            document

        Raises:
            ValidationError
        """
        try:
            assert document.text
        except AssertionError:
            raise ValidationError(
                message='Vous n\'avez rien renseigne, CTRL + C pour quitter...')


# pylint: disable=too-few-public-methods
class DateValidator(Validator):
    """DateValidator.
    """

    # pylint: disable=raise-missing-from
    # pylint: disable=no-self-use
    def validate(self, document):
        """Summary of validate.

        Args:
            document

        Raises:
            ValidationError
        """
        try:
            assert is_date(document.text)
        except (ValueError, AssertionError):
            raise ValidationError(
                message='Entrez une date valide',
                cursor_position=len(document.text))  # Move cursor to end


class FutureDateValidator(DateValidator):
    """DateValidator.
    """

    # pylint: disable=raise-missing-from
    # pylint: disable=no-self-use
    def validate(self, document):
        """Summary of validate.

        Args:
            document

        Raises:
            ValidationError
        """
        super().validate(document)
        try:
            assert is_future_date(document.text)
        except AssertionError:
            raise ValidationError(
                message='Votre tournoi ne peut avoir lieu avant aujourd\'hui',
                cursor_position=len(document.text))  # Move cursor to end


def is_date(string) -> bool:
    """Summary of is_date.
    Returns whether the string can be interpreted as a date.

    Args:
        string

    Returns:
        bool
    """
    return bool(parse(string, settings={'DATE_ORDER': 'DMY',
                                        'STRICT_PARSING': True}))


def is_future_date(string) -> bool:
    """Summary of is_future_date.

    Args:
        string

    Returns:
        bool: Description of return value
    """
    date = parse(string, settings={'DATE_ORDER': 'DMY',
                                   'STRICT_PARSING': True})
    now = datetime.now()

    return bool(date >= now)
