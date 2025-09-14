from pathlib import Path
from dotenv import load_dotenv
import os

class Config: 
    def __init__(self, env_file: str):
        env_path = Path(env_file)
        if not env_path.exists():
            raise FileNotFoundError(f"Env file not found: {env_file}")
        load_dotenv(env_path)
        self.HOSTNAME = os.getenv('HOSTNAME')

def load_config(env_name: str) -> Config:
    base = Path(__file__).parent
    env_dir = base / 'env'
    env_file = env_dir / f"{env_name}.env"
    return Config(str(env_file))