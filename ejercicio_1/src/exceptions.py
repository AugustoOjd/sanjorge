from fastapi import HTTPException, status


def validate_existe_subsidiary_id(subsidiary):
    if subsidiary is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Subsidiary id not found"
        )