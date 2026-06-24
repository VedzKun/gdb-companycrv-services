from fastapi import Depends
from app.services.company_verification_service import CompanyVerificationService

def get_company_service() -> CompanyVerificationService:
    """Provider for CompanyVerificationService."""
    return CompanyVerificationService()
