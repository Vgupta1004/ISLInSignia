# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:35:52 2020

@author: shara
"""

import pafy
import vlc
import time


url = "https://www.youtube.com/watch?v=7Im2I6STbms"
video = pafy.new(url)
best = video.getbest()
playurl = best.url

instance  = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new(playurl)
media.get_mrl()
player.set_media(media)
player.play()
time.sleep(50)