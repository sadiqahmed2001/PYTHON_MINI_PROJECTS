import pyscreenshot
import time


delay =int(input("enter the delay time for screen short: "))

print(f"Waiting for {delay} seconds before taking screenshot...")
time.sleep(delay)

# Capture a screenshot of the entire screen
image = pyscreenshot.grab()

# Display the captured screenshot
image.show()

# Save the screenshot as "vscode.png"
image.save("myscreenshorts.png")