from typing import Tuple
from src.core.utils import execute_code

def execute_code_service(code: str) -> Tuple[str, str]:
    return execute_code(code)
