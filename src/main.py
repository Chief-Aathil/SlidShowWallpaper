"""
This is a slideshow wallpaper script.
Save the image paths in config.json.
These paths are loaded into a list.
They are then ordered in required fashion(random/alphabetical/...)
and enqueued into a circular queue.
The queue is processed at regular intervals(timeout also stored in config.py).
"""
__author__="Aathil"

config_file="config.json"
default_order='FOLDER ORDER'#TODO:  should i use enum here for other values?
default_settings=''#TODO: define all settings values. like fill/fit/stretch, background colour etc
queue=[]

def loadList(config_file,order=default_order):
    list=[]
    #TODO:  add image file paths from config_file to list
    #TODO: apply order
    return list


#TODO: would be better to use a class of some default library queue
def enque(list):
    #TODO: add list items to queue(global)
    return 


def setWallpaper(img,settings=default_settings):
    return

def main():
    settings='' #TODO: retrieve settings from config file
    enque(loadList())
    while(True):
        for element in queue:
            setWallpaper(element,settings)
            #TODO: wait for timeout
            #TODO: log here
        enque()
        #TODO: log here
