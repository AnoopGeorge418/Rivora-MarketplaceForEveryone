from pydantic import BaseModel, field_validator


class LoginRequestSchema(BaseModel):
    # TODO - Build logic in service layer
    identifier: str  # can be username or email
    password: str

    @field_validator("identifier")
    @classmethod
    def identifier_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Username or Email required")

        return v


class TokenResponse(BaseModel): ...
