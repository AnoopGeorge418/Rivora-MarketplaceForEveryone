from enum import Enum


class AuthProvidersEnum(str, Enum):
    META = "meta"
    EMAIL = "email"
    GOOGLE = "google"
    GITHUB = "github"
