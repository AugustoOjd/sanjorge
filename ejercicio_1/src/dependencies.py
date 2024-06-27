from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os
load_dotenv()


secret_key = os.environ.get("API_KEY_HEADER")


api_key_header = APIKeyHeader(name="x-api-key", description='api key propital')


def validate_api_key(api_key: str = Security(api_key_header)):
    if api_key_header:
        if secret_key == api_key:
            return api_key_header
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='invalidate api key'
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='api key not found'
        )