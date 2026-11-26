import sys
from pathlib import Path

import pygame

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from game import Game


def main() -> None:
    if not pygame.get_init():
        pygame.init()
    game = Game()
    game.run()


if __name__ == "__main__":
    main()