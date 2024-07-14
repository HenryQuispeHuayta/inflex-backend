from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import os

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.post("/execute/")
async def executeCode(request: CodeRequest):
    code = request.code
    
    filePath = 'run.inf'
    
    try:
        with open(filePath, 'w') as file:
            file.write(code)
        
        result = subprocess.run(['python', 'inflex/inFlex.py', filePath], capture_output=True, text=True, check=True)
        
        output = result.stdout
        errors = result.stderr
        
    except subprocess.CalledProcessError as e:
        output = e.stdout
        errors = e.stderr
    finally:
        if os.path.exists(filePath):
            os.remove(filePath)
    
    if errors:
        raise HTTPException(status_code=400, detail=f"Error executing code: {errors}")
    
    return {"result": output}
