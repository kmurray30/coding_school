# Handle file uploads in FastAPI.

from fastapi import FastAPI, File, UploadFile, HTTPException
from pathlib import Path
import shutil

app = FastAPI()

# Directory to store uploads
UPLOAD_DIR = Path("./uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Basic file upload"""
    # Save file
    file_path = UPLOAD_DIR / file.filename
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file_path.stat().st_size,
        "path": str(file_path)
    }

@app.post("/upload-multiple")
async def upload_multiple_files(files: list[UploadFile] = File(...)):
    """Upload multiple files"""
    uploaded = []
    
    for file in files:
        file_path = UPLOAD_DIR / file.filename
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        uploaded.append({
            "filename": file.filename,
            "size": file_path.stat().st_size
        })
    
    return {"files": uploaded, "count": len(uploaded)}

@app.get("/files/{filename}")
async def download_file(filename: str):
    """Download a file"""
    file_path = UPLOAD_DIR / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    from fastapi.responses import FileResponse
    return FileResponse(file_path, filename=filename)

# Run with: uvicorn exercise1_file_upload:app --reload
#
# Test with curl:
# Upload: curl -F "file=@/path/to/file.txt" http://localhost:8000/upload
# Download: curl http://localhost:8000/files/file.txt
#
# Or test in /docs with file upload UI
