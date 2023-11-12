from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from image_service import generate_text_image
app = FastAPI()

class PlotRequest(BaseModel):
    message: str
    ticker: str
    timeframe: str
    current_value: str

@app.post("/generate_plot/")
async def get_plot(request: PlotRequest):
    
    image_filename = generate_text_image(divergence=request.message,
                                         ticker = request.ticker,
                                         current_value= request.current_value,
                                         time_frame=request.timeframe)
    
    # Return the image file as a response
    return FileResponse(path=image_filename, media_type="image/png", filename="plot.png")
    # return {"file_path":image_filename}
