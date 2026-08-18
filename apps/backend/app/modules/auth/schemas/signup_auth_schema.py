from pydantic import BaseModel, EmailStr, field_validator


class SignupRequestSchema(BaseModel):
    email: EmailStr
    otp: str

    @field_validator("otp")
    @classmethod
    def validate_otp(cls, v: str) -> str:
        v = v.strip()
        if len(v) != 6:
            raise ValueError("Otp should have length of 6.")

        return v


class SignupResponseSchema(BaseModel): ...
