from enum import Enum


class AuthRolesEnum(str, Enum):
    USER = "user"
    ADMIN = "admin"
    VENDOR = "vendor"
    DEVELOPER = "developer"
    SUPER_ADMIN = "super admin"
