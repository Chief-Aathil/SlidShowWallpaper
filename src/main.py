"""
This is a slideshow wallpaper script.
Save the image paths in config.py in JSON format.
These paths are loaded into a list.
They are then ordered in required fashion(random/alphabetical/...)
and enqueued into a circular queue.
The queue is processed at regular intervals(timeout also stored in config.py).
"""