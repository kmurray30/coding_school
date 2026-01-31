# Validate file uploads: size, type, extension.

from fastapi import FastAPI, File, UploadFile, HTTPException
from pathlib import Path

app = FastAPI()

UPLOAD_DIR = Path("./uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

# Configuration
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".pdf"}
ALLOWED_CONTENT_TYPES = {
    "image/jpeg",
    "image/png",
    "application/pdf"
}

@app.post("/upload-validated")
async def upload_with_validation(file: UploadFile = File(...)):
    """Upload with validation"""
    
    # Validate file extension
    file_ext = Path(file.filename).suffix.lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"File type not allowed. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    
    # Validate content type
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Content type not allowed: {file.content_type}"
        )
    
    # Read file to check size
    contents = await file.read()
    file_size = len(contents)
    
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Max size: {MAX_FILE_SIZE / 1024 / 1024}MB"
        )
    
    if file_size == 0:
        raise HTTPException(
            status_code=400,
            detail="Empty file not allowed"
        )
    
    # Save file
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as f:
        f.write(contents)
    
    return {
        "filename": file.filename,
        "size": file_size,
        "content_type": file.content_type,
        "message": "File uploaded successfully"
    }

# Run with: uvicorn exercise2_file_validation:app --reload
#
# Test:
# Valid: curl -F "file=@image.jpg" http://localhost:8000/upload-validated
# Too large: curl -F "file=@largefile.jpg" → 400 error
# Wrong type: curl -F "file=@document.docx" → 400 error
#
# Always validate user uploads:
# ✅ File size (prevent abuse)
# ✅ File type (security)
# ✅ File extension (security)
# ✅ Content (scan for malware in production)
