from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from pytz import timezone, utc

def generate_text_image(divergence = "Bearish RSI \nDivergence Detected" ,ticker = "BTCUSDT"
                        ,output_path="text_image.png", timezone_name='US/Eastern',current_value = "10503",
                        time_frame = "4H"):
    # Get the current datetime in UTC
    now_utc = datetime.now(utc)

    # Convert to a specific timezone
    target_timezone = timezone(timezone_name)
    now_target = now_utc.astimezone(target_timezone)

    # Format the datetime as "hours:minutes" (HH:MM)
    formatted_time = now_target.strftime('%H:%M')

    # Create a new image with a white background
    width, height = 800, 400
    image = Image.new("RGB", (width, height), "black")

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Define your text messages and fonts
    text_messages = [
        divergence, ticker,
        "Current Value", current_value,
        "Time Frame", time_frame, f"{formatted_time} UTC"
    ]
    fonts = [
        ImageFont.truetype("liberation-fonts-ttf/LiberationMono-Bold.ttf", 30),
        ImageFont.truetype("liberation-fonts-ttf/LiberationMono-Bold.ttf", 60),
        ImageFont.truetype("liberation-fonts-ttf/LiberationMono-Bold.ttf", 30),
        ImageFont.truetype("liberation-fonts-ttf/LiberationMono-Bold.ttf", 30),
        ImageFont.truetype("liberation-fonts-ttf/LiberationMono-Bold.ttf", 30),
        ImageFont.truetype("liberation-fonts-ttf/LiberationMono-Bold.ttf", 30),
        ImageFont.truetype("liberation-fonts-ttf/LiberationMono-Bold.ttf", 15)
    ]

    # Set the positions for each text message
    positions = [(50, 70), (50, 150), (50, 250), (300, 250), (50, 300), (250, 300), (50, 375)]

    # Set the font colors
    font_colors = [(255, 114, 112), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)]

    # Draw the text on the image
    for i in range(len(text_messages)):
        draw.text(positions[i], text_messages[i], font=fonts[i], fill=font_colors[i])

    # Save the image
    image.save(output_path)
    return output_path

# Example usage:
# generate_text_image(ticker = "Ethusdt")
