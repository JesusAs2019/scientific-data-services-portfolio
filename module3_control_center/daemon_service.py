# module3_control_center/daemon_service.py
import os
import time

# Use absolute directory tracking relative to the script location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WATCH_DIR = os.path.join(BASE_DIR, "module3_control_center", "incoming_pdfs")
PROCESSED_DIR = os.path.join(BASE_DIR, "module3_control_center", "processed_pdfs")

# Ensure directories exist locally
os.makedirs(WATCH_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

print(f"ChemData AI Engine running.")
print(f"Monitoring folder: '{WATCH_DIR}'...")
print("Checking for files every second... Press Ctrl + C to stop.")

try:
    while True:
        # Actively poll the directory contents
        files = [f for f in os.listdir(WATCH_DIR) if f.lower().endswith('.pdf')]
        
        for filename in files:
            src_path = os.path.join(WATCH_DIR, filename)
            dest_path = os.path.join(PROCESSED_DIR, filename)
            
            print(f"\n[EVENT DETECTED] New file found: {src_path}")
            print("Applying a 2-second operating system write-lock backoff delay...")
            time.sleep(2)
            
            # Safe moving operation
            if os.path.exists(src_path):
                os.rename(src_path, dest_path)
                print(f"[SUCCESS] Document systematically processed and archived to: {dest_path}")
                
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping background observer tracking daemon gracefully...")
    