import vlc

def radio_play():
    radio_url = input("Write internet radio URL: ")
    player = vlc.MediaPlayer(radio_url)

    print("Commands: play, pause, stop, quit")
    while True:
        command = input("Write command: ").strip().lower()

        if command == "play":
            player.play()
            print("Radio is playing.")
        elif command == "pause":
            player.pause()
            print("Radio is paused.")
        elif command == "stop":
            player.stop()
            print("Radio is stopped.")
        elif command == "quit":
            print("Closing app...")
            player.stop()
            break
        else:
            print("Unknown command. Try: play, pause, stop, quit.")

radio_play()
