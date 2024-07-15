import subprocess
import os
from typing import Tuple

def execute_code(code: str) -> Tuple[str, str]:
    file_path = 'inflex/run.inf'
    
    try:
        with open(file_path, 'w') as file:
            file.write(code)
        
        result = subprocess.run(['python', 'inflex/inFlex.py', file_path], capture_output=True, text=True, check=True)
        output = result.stdout
        errors = result.stderr
        
    except subprocess.CalledProcessError as e:
        output = e.stdout
        errors = e.stderr
    
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
    
    return output, errors
