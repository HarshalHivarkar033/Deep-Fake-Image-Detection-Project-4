from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import cv2
import numpy as np
import io

from analysis.frequency import analyze_frequency
from analysis.biological import analyze_biological
from analysis.architectural import analyze_architectural

app = FastAPI(title="TrueLens API")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/analyze")
async def analyze_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File provided is not an image.")
    
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        raise HTTPException(status_code=400, detail="Invalid image file.")
    
    # Run analyses
    freq_score, freq_details = analyze_frequency(img)
    bio_score, bio_details = analyze_biological(img)
    arch_score, arch_details = analyze_architectural(img)
    
    # Calculate overall authenticity score (weighted average)
    # 0 = Definitely Fake, 100 = Definitely Real
    # Let's say all three have equal weight for now.
    weights = {"freq": 0.4, "bio": 0.3, "arch": 0.3}
    overall_score = (freq_score * weights["freq"] + 
                     bio_score * weights["bio"] + 
                     arch_score * weights["arch"])
    
    return {
        "authenticity_score": round(overall_score, 2),
        "breakdown": {
            "frequency_analysis": {
                "score": round(freq_score, 2),
                "details": freq_details
            },
            "biological_analysis": {
                "score": round(bio_score, 2),
                "details": bio_details
            },
            "architectural_analysis": {
                "score": round(arch_score, 2),
                "details": arch_details
            }
        }
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
