"""
Test script to validate backend setup
Run: python test_setup.py
"""

import sys
import os
from pathlib import Path

def check_files():
    """Check if all required files exist"""
    required_files = [
        "main.py",
        "config.py",
        "requirements.txt",
        "models/schemas.py",
        "models/database.py",
        "routes/process.py",
        "routes/tasks.py",
        "routes/logs.py",
        "services/orchestrator.py",
        "services/task_repository.py",
        "services/log_repository.py",
    ]
    
    print("📁 Checking files...")
    all_exist = True
    for file in required_files:
        path = Path(file)
        status = "✓" if path.exists() else "✗"
        print(f"  {status} {file}")
        if not path.exists():
            all_exist = False
    
    return all_exist


def check_imports():
    """Check if imports work"""
    print("\n📦 Checking imports...")
    try:
        from models.schemas import ProcessRequest, Task, Log
        print("  ✓ models.schemas")
    except Exception as e:
        print(f"  ✗ models.schemas: {e}")
        return False
    
    try:
        from config import settings
        print("  ✓ config")
    except Exception as e:
        print(f"  ✗ config: {e}")
        return False
    
    try:
        from services.orchestrator import OrchestratorService
        print("  ✓ services.orchestrator")
    except Exception as e:
        print(f"  ✗ services.orchestrator: {e}")
        return False
    
    return True


def main():
    """Run all checks"""
    print("🔍 ET GenAI Backend Setup Validation\n")
    
    # Check files
    files_ok = check_files()
    
    # Check imports
    imports_ok = check_imports()
    
    # Summary
    print("\n" + "="*50)
    if files_ok and imports_ok:
        print("✓ All checks passed! Ready to run.")
        print("\nNext steps:")
        print("1. Ensure MongoDB is running:")
        print("   docker run -d -p 27017:27017 --name mongodb mongo:latest")
        print("\n2. Install dependencies:")
        print("   pip install -r requirements.txt")
        print("\n3. Run the server:")
        print("   python main.py")
        print("\n4. Open browser to: http://localhost:8000/docs")
        return 0
    else:
        print("✗ Some checks failed. Please review above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
