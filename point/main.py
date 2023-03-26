import points
import game_menu

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = points.Points()
    menu = game_menu.GameMenu(game)
    menu.show_menu()
