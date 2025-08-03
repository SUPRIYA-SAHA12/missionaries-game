def play_game():
    boat_side = 'Right'
    miss_on_right = 3
    cann_on_right = 3
    miss_on_left = 0
    cann_on_left = 0
    print("M=", miss_on_left, 'C=', cann_on_left, '|.....B|', "M=", miss_on_right, "C=", cann_on_right)
    while True:
        Miss = int(input("Enter the number of Missionaries: "))
        Cann = int(input("Enter the number of Cannibals: "))
        if (Miss + Cann) != 1 and (Miss + Cann) != 2:
            print("Invalid Move")
            continue
        if boat_side == 'Right':
            if miss_on_right < Miss or cann_on_right < Cann:
                print("invalid move")
                continue
            miss_on_right -= Miss
            cann_on_right -= Cann
            miss_on_left += Miss
            cann_on_left += Cann
            boat_side = 'Left'
        else:
            if miss_on_left < Miss or cann_on_left < Cann:
                print("invalid move")
                continue
            miss_on_left -= Miss
            cann_on_left -= Cann
            miss_on_right += Miss
            cann_on_right += Cann
            boat_side = 'Right'
        print("M=", miss_on_left, 'C=', cann_on_left, '|.....B|', "M=", miss_on_right, "C=", cann_on_right)
        if (miss_on_right > 0 and miss_on_right < cann_on_right) or (miss_on_left > 0 and miss_on_left < cann_on_left):
            print("you lost")
            return
        if miss_on_left == 3 and cann_on_left == 3:
            print("you win")
            return

if __name__ == "__main__":
    play_game()
