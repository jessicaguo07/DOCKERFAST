from fastapi.security import APIKeyHeader
from fastapi import HTTPException, status, Security

# API Keys
api_keys = ['1234567890', '0987654321']
security_scheme = APIKeyHeader(name='X-API-Key', auto_error=False)

def auth_api_key(input_api_key_string: str = Security(security_scheme)):
    if input_api_key_string not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid API Key'
        )

