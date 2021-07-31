from pynput import keyboard

class Commands:
    def __init__(self, board):
        self.board = board
    
    def command_runnable(self):
        print(self.board)
        print("Press arrow to move the empty box")
        print("Press 'SHIFT' to shuffle the self.board n times")
        print("Press 'SPACE' to view solution of the current self.board")
        print("Press 'ESC' to exit\n")

        def on_press(key):
            if key in [keyboard.Key.up, keyboard.Key.down, keyboard.Key.right, keyboard.Key.left]:
                if key == keyboard.Key.up:
                    self.board.move_up()
                elif key == keyboard.Key.down:
                    self.board.move_down()
                elif key == keyboard.Key.right:
                    self.board.move_right()
                elif key == keyboard.Key.left:
                    self.board.move_left()
                print(self.board)
                print("Press arrow to move the empty box")
                print("Press 'SHIFT' to shuffle the self.board n times")
                print("Press 'SPACE' to view solution of the current self.board")
                print("Press 'ESC' to exit\n")
            elif key == keyboard.Key.space:
                self.board.solve()
                print("End of solution\n")
                print('------------------\n')
                print("Current self.board :\n")
                print(self.board)
                print("Press arrow to move the empty box again")
                print("Press 'SHIFT' to shuffle the self.board n times")
                print("Press 'SPACE' to view solution of the current self.board")
                print("Press 'ESC' to exit\n")
            elif key == keyboard.Key.shift:
                n = int(input("Enter how many times to shuffle the self.board : "))
                self.board.shuffle(n)
                print()
                print(self.board)
                print("Press arrow to move the empty box")
                print("Press 'SHIFT' to shuffle the self.board n times")
                print("Press 'SPACE' to view solution of the current self.board")
                print("Press 'ESC' to exit\n")
            elif key == keyboard.Key.esc:
                exit()

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
