from pynput import keyboard
from datetime import datetime
import os

# Log file path
LOG_FILE = 'keystrokes.log'

def on_press(key):
    try:
        # Get current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Format the key
        if hasattr(key, 'char') and key.char is not None:
            key_str = key.char
        else:
            key_str = str(key).replace('Key.', '')
        
        # Handle special keys
        if key_str == 'space':
            key_str = ' '
        elif key_str == 'enter':
            key_str = '\n'
        elif key_str == 'tab':
            key_str = '\t'
        elif key_str == 'backspace':
            key_str = '[BACKSPACE]'
        elif key_str == 'esc':
            key_str = '[ESC]'
            # Stop the listener on ESC
            return False
        
        # Write to log file
        with open(LOG_FILE, 'a') as f:
            f.write(f"{timestamp}: '{key_str}'\n")
            
    except Exception as e:
        # Log any errors
        with open(LOG_FILE, 'a') as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: [ERROR] {str(e)}\n")

def main():
    # Ensure log file exists
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            f.write("Keystroke log started\n")
    
    print("Keystroke logger started. Press ESC to stop.")
    print("Logging to:", LOG_FILE)
    
    # Start the listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    
    # After stopping, display the log contents
    print("\n--- Session Log ---")
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            log_content = f.read()
            print(log_content)
    else:
        print("No log file found.")
    print("--- End of Log ---")

if __name__ == "__main__":
    main()
