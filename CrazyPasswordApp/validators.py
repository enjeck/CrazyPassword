import re
from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


currentYear = str(datetime.now().year)

# Helper  function to sum all digits in a number
def sumDigits(txt):
    sumdig = sum(int(x) for x in txt if x.isdigit())
    return sumdig

class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("Your password must contain at least 1 number."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 number."
        )

class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("Your password must contain at least 1 uppercase letter."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase letter."
        )


class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("Your password must contain at least 1 lowercase letter."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 lowercase letter."
        )


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("Your password must contain at least 1 special character."),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 special character."
        )

class MinLengthValidator(object):
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError(
                _("Your password must have at least 8 characters."),
                code='password_min_length',
            )

    def get_help_text(self):
        return _(
            "Your password must have at least 8 characters."
        )

class AnotherLengthValidator(object):
    def validate(self, password, user=None):
        if len(password) < 15:
            raise ValidationError(
                _("Your password must have at least 15 characters."),
                code='password_another_length',
            )

    def get_help_text(self):
        return _(
            "Your password must have at least 8 characters."
        )

class MaxLengthValidator(object):
    def validate(self, password, user=None):
        if len(password) > 40:
            raise ValidationError(
                _("Your password cannot exceed 40 characters."),
                code='password_max_length',
            )

    def get_help_text(self):
        return _(
            "Your password cannot exceed 40 characters."
        )

class NoSpaceValidator(object):
    def validate(self, password, user=None):
        if re.findall('\s', password):
            raise ValidationError(
                _("Your password cannot contain spaces."),
                code='password_no_space',
            )

    def get_help_text(self):
        return _(
            "Your password cannot contain spaces."
        )   
            

class UpperCountValidator(object):
    def validate(self, password, user=None):
        if not len(re.findall('[A-Z]', password)) > 3:
            raise ValidationError(
                _("Your password must contain more than 3 capital letters."),
                code='password_count_upper',
            )

    def get_help_text(self):
        return _(
            "Your password must contain more than 3 capital letters."
        )

class LowerCountValidator(object):
    def validate(self, password, user=None):
        if not len(re.findall('[a-z]', password)) > 2:
            raise ValidationError(
                _("Your password must contain more than 3 lowercase letters."),
                code='password_number_lower',
            )

    def get_help_text(self):
        return _(
            "Your password must contain more than 3 lowercase letters."
        )

class NoEValidator(object):
    def validate(self, password, user=None):
        if re.findall('E', password):
            raise ValidationError(
                _("Your password cannot contain a capital E."),
                code='password_no_e',
            )

    def get_help_text(self):
        return _(
            "Your password cannot contain a capital E."
        )

class NoSValidator(object):
    def validate(self, password, user=None):
        if re.findall('S', password):
            raise ValidationError(
                _("Your password cannot contain a capital S."),
                code='password_no_s',
            )

    def get_help_text(self):
        return _(
            "Your password cannot contain a capital S."
        )

class IdenticalNumbersValidator(object):
    def validate(self, password, user=None):
        if not re.findall(r"(([0-9])\2)", password):
            raise ValidationError(
                _("Your password must contain two identical numbers in a row."),
                code='password_identical_numbers',
            )

    def get_help_text(self):
        return _(
            "Your password must contain two identical numbers in a row."
        )

class RangeCountValidator(object):
    def validate(self, password, user=None):
        if not len(password) < 20 and len(password) > 30:
            raise ValidationError(
                _("Your password should be between 20 and 30 characters."),
                code='password_range_count',
            )

    def get_help_text(self):
        return _(
            "Your password should be between 20 and 30 characters."
        )

class GreekLetterValidator(object):
    def validate(self, password, user=None):
        if not re.findall(r"[\u0370-\u03FF]", password):
            raise ValidationError(
                _("Your password must contain a Greek letter."),
                code='password_greek_letter',
            )

    def get_help_text(self):
        return _(
            "Your password must contain a Greek letter."
        )

class CapitalNeighborValidator(object):
    def validate(self, password, user=None):
        if re.findall(r"[A-Z]{2}", password):
            raise ValidationError(
                _("Capital letters cannot be next to eachother."),
                code='password_capital_neighbor',
            )

    def get_help_text(self):
        return _(
            "Capital letters cannot be next to eachother."
        )

class SumNumbersValidator(object):
    def validate(self, password, user=None):
        if sumDigits(password) != 50:
            raise ValidationError(
                _("The sum of all digits in your password must be 50."),
                code='password_sum_numbers',
            )

    def get_help_text(self):
        return _(
            "The sum of all digits in your password must be 50."
        )

class YearValidator(object):
    def validate(self, password, user=None):
        if currentYear not in password:
            raise ValidationError(
                _("Your password must contain the current year."),
                code='password_this_year',
            )

    def get_help_text(self):
        return _(
            "Your password must contain the current year."
        )

class UpperCountValidator(object):
    def validate(self, password, user=None):
        if len(re.findall("[A-Z]", password)) != 5:
            raise ValidationError(
                _("Your password must include exactly 5 capital letters."),
                code='password_upper_count',
            )

    def get_help_text(self):
        return _(
            "Your password must include exactly 5 capital letters."
        )

