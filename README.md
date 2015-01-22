# Isolate and Frame

This is a Blender add-on for isolating and framing a selected animation channel in the Graph Editor.

Usage instructions:

  1. Select the channel
  2. Move your mouse cursor to the Graph Editor
  3. Press <kbd>Shift</kbd>+<kbd>V</kbd> or choose Channel > Isolate and Frame from the menu.

## Notes

The operator *can* work with your mouse cursor still in the Channels region of the Graph Editor, but not with the hotkey. Instead, you'll need to use the <kbd>Space</kbd> search feature and find "Isolate and Frame" there. Fortunately, Blender remembers your search, so subsequent uses can be pretty fast (<kbd>Space</kbd> > <kbd>Enter</kbd>).

## Known Issues

Unfortunately, the hotkey will not work in the Channels region of the Graph Editor. For some reason, there's no way to set a hotkey that will work from there. In fact, Shift+V is actually assigned to a visibility toggle in that region, but it cannot be overridden. So, until that gets fixed, the fastest method is to use the Spacebar search workaround.

## Wishlist

It would be nice if this happened automatically upon selecting an animation channel. Unfortunately, Blender's Python API doesn't have access to selection events. Maybe one day...
