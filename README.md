# Company Registration Validation (CRV) Service

## Overview

A standalone microservice that simulates the Ministry of Corporate Affairs (MCA) / Registrar of Companies (ROC) API. It validates Company Registration Numbers (CIN) against a hardcoded list of valid numbers.

**Port:** 8006
**Service Name:** `company_crv_service`

## Features

- **CIN Validation:** Verifies if a 21-character Company Identification Number is valid.
- **Standalone:** Runs independently on port 8006.
- **Simulation:** Uses a set of hardcoded valid CINs to simulate third-party verification.
- **Health Check:** Standard health check endpoint.

## API Endpoints

### 1. Verify Company Registration

**Endpoint:** `POST /api/v1/company/verify`

**Request:**
```json
{
  "registration_number": "U72900KA2020PTC123456"
}
```

**Success Response (200):**
```json
{
  "registration_number": "U72900KA2020PTC123456",
  "is_valid": true,
  "status": "VERIFIED",
  "message": "Company registration number verified successfully",
  "timestamp": "2026-01-21T00:00:00Z"
}
```

**Failure Response (200):**
```json
{
  "registration_number": "U99999KA2026PTC999999",
  "is_valid": false,
  "status": "INVALID",
  "message": "Company registration number not found in MCA records",
  "timestamp": "2026-01-21T00:00:00Z"
}
```

### 2. Get Valid Registration Numbers (Testing)

**Endpoint:** `GET /api/v1/company/valid-companies`

Returns a list of all valid CINs configured in the service.

### 3. Health Check

**Endpoint:** `GET /health`

## Valid Registration Numbers for Testing

The following CINs are hardcoded as valid:

1. `U72900KA2020PTC123456`
2. `L67120MH2019PLC234567`
3. `U74999DL2021PTC345678`
4. `L85110TN2018PLC456789`
5. `U51909GJ2022PTC567890`
6. `L24233WB2017PLC678901`
7. `U45200HR2023PTC789012`
8. `L29130AP2019PLC890123`
9. `U62013RJ2021PTC901234`
10. `L15142UP2020PLC012345`

## Setup & Running

### Prerequisites

- Python 3.9+
- Virtual environment (recommended)

### Installation

1. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Service

```bash
uvicorn app.main:app --port 8006
```

## Security Note

This is a simulation service intended for development and testing environments only. In a production environment, this would be replaced by a secure integration with the actual MCA/ROC APIs.
