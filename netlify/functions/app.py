import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import and create Flask app
from app import app

def handler(event, context):
    """Netlify serverless function handler"""
    return app(event, context)
