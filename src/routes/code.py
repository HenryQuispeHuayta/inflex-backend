from fastapi import APIRouter, HTTPException
from src.schemas.code import CodeRequest
from src.services.code_service import execute_code

router = APIRouter()

@router.post("/execute/")
async def execute_code_endpoint(request: CodeRequest):
    code = request.code
    
    try:
        output, errors = execute_code(code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error executing code: {str(e)}")
    
    if errors:
        raise HTTPException(status_code=400, detail=f"Error executing code: {errors}")
    
    return {"result": output}
