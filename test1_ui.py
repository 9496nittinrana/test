import pytest
import pygame
from main import draw_board, draw_symbols, draw_hover, display_message, draw_button

@pytest.fixture
def pygame_setup():
    """Initialize Pygame for UI tests"""
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    return screen

def test_pygame_init():
    """Ensure Pygame initializes correctly"""
    assert pygame.get_init() is True

def test_pygame_screen(pygame_setup):
    """Check if Pygame screen initializes without error"""
    assert pygame_setup is not None

def test_draw_board(pygame_setup):
    """Ensure board draws without errors"""
    draw_board()

def test_draw_symbols(pygame_setup):
    """Ensure symbols are drawn correctly"""
    draw_symbols()

def test_draw_hover(pygame_setup):
    """Ensure hover effect is drawn"""
    draw_hover()

def test_display_message(pygame_setup):
    """Ensure message display works"""
    display_message("Test Message")

def test_draw_button(pygame_setup):
    """Ensure button draws and detects clicks"""
    assert not draw_button("Play", 250, 250, 100, 50, (98, 213, 148), (16, 207, 99))

    # Simulate a mouse click on the button
    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': (275, 275)}))
    assert draw_button("Play", 250, 250, 100, 50, (98, 213, 148), (16, 207, 99))
