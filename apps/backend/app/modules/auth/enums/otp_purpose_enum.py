from enum import Enum


class OtpPurposeEnum(str, Enum):
    SIGNUP = "signup"
    RESET = "reset"
