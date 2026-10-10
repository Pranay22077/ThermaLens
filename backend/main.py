import os
import uvicorn

# Load environment variables from .env file if it exists
try:
    from pathlib import Path
    env_file = Path(__file__).parent.parent / '.env'
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip())
except Exception as e:
    print(f"Note: Could not load .env file: {e}")

from app import app
if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=int(os.environ.get("PORT","8000")))
