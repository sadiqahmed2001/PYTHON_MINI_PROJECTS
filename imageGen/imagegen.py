import requests
from PIL import Image
from io import BytesIO

# Function to generate an image from a prompt using the RapidAPI service
def generate_image_from_prompt(prompt, rapidapi_key, output_file='generated_image.png'):
    url = "https://ai-image-generator-from-a-prompt-using-openai-api.p.rapidapi.com/image"
    
    querystring = {"prompt": prompt}
    
    headers = {
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": "ai-image-generator-from-a-prompt-using-openai-api.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        # Assuming the response contains a URL to the generated image
        image_url = response.json().get('url')
        
        if image_url:
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))
            image.save(output_file)
            print(f"Image saved as {output_file}")
        else:
            print("No URL found in the response.")
    else:
        print(f"Failed to generate image: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # Take the prompt as input from the user
    prompt = input("Enter your image prompt: ")
    rapidapi_key = "ef6b15a96cmsh921ff8b61f7b985p17cea9jsna24db7a3c119"  # Your RapidAPI key
    
    generate_image_from_prompt(prompt, rapidapi_key)
