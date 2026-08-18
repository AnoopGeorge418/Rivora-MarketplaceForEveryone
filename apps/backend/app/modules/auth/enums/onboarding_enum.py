from enum import Enum


class OnboardingStatusEnum(str, Enum):
    PENDING_VERIFICATION = "pending_verification"  # signed up, OTP not confirmed
    VERIFIED = "verified"  # OTP confirmed, profile not filled
    PROFILE_COMPLETE = "profile_complete"  # firstname/lastname/username set
    ONBOARDED = "onboarded"
