This project will create a slideshow of pictures as wallpaper

## Approach:
1. Create a list of all image files(can be stored/retrieved using a config file)
2. Add the list to a queue.
3. Retrieve the head of the queue and display that image as wallpaper
4. After a timeout period  repeat *step 4* until queue is empty.
5. Refill the queue
