import pytest
from unittest.mock import Mock
from project import countdown, set_timer, change_font_color, reset


def test_countdown():
    # Mock the clock and countdown_label objects
    clock = Mock()
    countdown_label = Mock()

    # Set the countdown function's global variables to the mock objects
    countdown.__globals__["clock"] = clock
    countdown.__globals__["countdown_label"] = countdown_label

    # Call the countdown function
    countdown(60)

    # Check if the after method was called on the clock object
    clock.after.assert_called_once_with(1000, countdown, 59)

    # Check if the config method was called on the countdown_label object
    countdown_label.config.assert_called_once_with(text="01:00", fg="#008000")


def test_set_timer():
    # Mock the start_button and timer_var objects
    start_button = Mock()
    timer_var = Mock()

    # Set the set_timer function's global variables to the mock objects
    set_timer.__globals__["start_button"] = start_button
    set_timer.__globals__["timer_var"] = timer_var

    # Set the return value of the get method of timer_var
    timer_var.get.return_value = 1

    # Mock the countdown function
    set_timer.__globals__["countdown"] = Mock()

    # Call the set_timer function
    set_timer()

    # Check if the countdown function was called with the correct argument
    set_timer.__globals__["countdown"].assert_called_once_with(60)

    # Check if the config method was called on the start_button object
    start_button.config.assert_called_once_with(state="disabled")


def test_change_font_color():
    # Mock the font object
    font = Mock()

    # Call the change_font_color function
    change_font_color(font)

    # Check if the config method was called on the font object
    assert font.config.call_count == 1


def test_reset():
    # Mock the clock, countdown_label, start_button, activity_buttons, timer_buttons, activity_var, and timer_var objects
    clock = Mock()
    countdown_label = Mock()
    start_button = Mock()
    activity_buttons = [Mock(), Mock()]
    timer_buttons = [Mock(), Mock()]
    activity_var = Mock()
    timer_var = Mock()

    # Set the reset function's global variables to the mock objects
    reset.__globals__["clock"] = clock
    reset.__globals__["countdown_label"] = countdown_label
    reset.__globals__["start_button"] = start_button
    reset.__globals__["activity_buttons"] = activity_buttons
    reset.__globals__["timer_buttons"] = timer_buttons
    reset.__globals__["activity_var"] = activity_var
    reset.__globals__["timer_var"] = timer_var

    # Call the reset function
    reset()

    # Check if the after_cancel method was called on the clock object
    clock.after_cancel.assert_called_once()

    # Check if the config method was called on the countdown_label object
    countdown_label.config.assert_called_once_with(text="00:00")

    # Check if the config method was called on the start_button object
    start_button.config.assert_called_once_with(state="normal")

    # Check if the config method was called on each activity_button and timer_button object
    for button in activity_buttons + timer_buttons:
        button.config.assert_called_once_with(state="normal")

    # Check if the set method was called on the activity_var and timer_var objects
    activity_var.set.assert_called_once_with(None)
    timer_var.set.assert_called_once_with(None)
