from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import Response, FileResponse
import shutil
import tempfile
import os
import cv2
from app.yolo_utils import yolo_box, yolo_seg 

app = FastAPI(title="YOLO Geometry Explorer")

@app.get("/")
async def serve_home_page():
    return FileResponse("index.html")

@app.post("/process-image/")
async def process_image_endpoint(
    image: UploadFile = File(...), 
    annotation: UploadFile = File(...),
    mode: str = Form("box") # Receives "box" or "segmentation" from frontend
):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_image_path = os.path.join(temp_dir, image.filename)
        temp_annotation_path = os.path.join(temp_dir, annotation.filename)
        with open(temp_image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        with open(temp_annotation_path, "wb") as buffer:
            shutil.copyfileobj(annotation.file, buffer)
            
        if mode == "segmentation":
            processed_image_array = yolo_seg(temp_image_path, temp_annotation_path)
        else:
            processed_image_array = yolo_box(temp_image_path, temp_annotation_path)
        
        # Encode and return the image
        success, encoded_image = cv2.imencode('.jpg', processed_image_array)
        if not success:
            return {"error": "Failed to process image."}
            
        return Response(content=encoded_image.tobytes(), media_type="image/jpeg")