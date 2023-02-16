from random import randint
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Notebook
from tkmacosx import Button
import random, pygame, time, webbrowser, os, time, customtkinter, tkinter, subprocess
from mutagen.mp3 import MP3
from datetime import date
from PIL import Image
from listmusic import list_music
from background import list_background

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")
customtkinter.deactivate_automatic_dpi_awareness()

root = customtkinter.CTk()
root.title("ZINFY")
root.resizable(False, False)

# get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calculate the x and y coordinates of the top-left corner of the window
x = int((screen_width - 900) / 2)  # 900 is the width of the window
y = int((screen_height - 700) / 2)  # 700 is the height of the window

# set the size and position of the window
root.geometry(f"800x600+{x}+{y}")

style = ttk.Style()
style.theme_use("aqua")
text_color = "#F2F3F4"

pygame.mixer.init()

# command 
def insert_song_short(e):
   global insert_song
   insert_song = insert_song + 1
   # print(f"insert song {insert_song}")

   # insert random 200 songs
   for song in range(200):
      # get list_music from listmusic.py 
      song = random.choice(list_music)
      song = song.replace("audio/", "")
      song = song.replace(".mp3", "")
      # insert name song on song box 
      song_box.insert(0, song)
   
def insert_song():
   global insert_song
   insert_song = insert_song + 1
   
   # insert random 200 songs 
   for song in range(200):
      # get list_music from listmusic.py
      song = random.choice(list_music)
      song = song.replace("audio/", "")
      song = song.replace(".mp3", "")
      # insert name song on song box 
      song_box.insert(0, song)
   
# play music 
def play_song(): 
   # get the first song that is highlighted 
   song = song_box.get(ACTIVE)

   # save value of song to date that is get(ACTIVE)
   data = song
   subprocess.run("pbcopy", text=True, input=data)

   # save value of song to song box that is get(ACTIVE)
   show_song = song
   # show song play to bar_play
   if len(show_song) > 50:
      show_song = show_song[:50]
      show_song = f"{show_song}..."
   show_song = show_song.upper() # upper text

   # save value of song to date that is get(ACTIVE)
   img_song = song
   global b_song
   b_song = f"background/{img_song}.png"

   # show 
   bar_play.configure(text=show_song)
   button_pause.configure(image=pause_img)
   background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(b_song), size=(800,600)))

   # play song 
   song = f"audio/{song}.mp3"
   pygame.mixer.music.load(song)
   pygame.mixer.music.play(loops=0)

   # call play time function
   play_time()

   # update slider top position
   slider_postition = int(length_song)
   scale_slider.configure(to=slider_postition)
   scale_slider.set(0)

   # process_bar.configure(to=slider_postition)
   # process_bar.set(0)

# process bar 
def play_time():
   # convert time play to current time
   current_time = pygame.mixer.music.get_pos() / 1000
   converted_current_time = time.strftime("%M:%S", time.gmtime(current_time))

   # convert length time of mp3 file to current time
   current_song = song_box.curselection()
   song = song_box.get(current_song)
   
   # get length of song 
   song = f"audio/{song}.mp3"
   song = MP3(song)
   global length_song
   length_song = song.info.length

   # time of song that is converted 
   converted_current_song = time.strftime("%M:%S", time.gmtime(length_song))

   # show time process 
   label_process_left.configure(text=converted_current_time)
   label_process_right.configure(text=converted_current_song)
   # label_bottom.configure(text=f"{converted_current_time} of {converted_current_song}")

   scale_slider.set(current_time)
   # process_bar.set(current_time)
   # update time 
   label_bottom.after(1000, play_time)
   
def play_song_shortcut(e): 
   # get the first song that is highlighted 
   song = song_box.get(ACTIVE)

   # save value of song to date that is get(ACTIVE)
   data = song
   subprocess.run("pbcopy", text=True, input=data)

   # save value of song to show song that is get() 
   show_song = song
   # show song play to bar_play
   if len(show_song) > 50:
      show_song = show_song[:50]
      show_song = f"{show_song}..."
   show_song = show_song.upper() # upper text

   # save value of song to date that is get(ACTIVE)
   img_song = song
   img_song = f"background/{img_song}.png"

   # show 
   bar_play.configure(text=show_song)
   button_pause.configure(image=pause_img)
   background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(img_song), size=(800,600)))

   # play song 
   song = f"audio/{song}.mp3"
   pygame.mixer.music.load(song)
   pygame.mixer.music.play(loops=0)

   # call play time function
   play_time()
   # update slider top position
   slider_postition = int(length_song)
   scale_slider.configure(to=slider_postition)
   scale_slider.set(0)

   # process_bar.configure(to=slider_postition)
   # process_bar.set(0)

# play the next song 
def next_song():
   if random_mode == True:
      # get the current song
      next_song = song_box.curselection()

      # get random number (random position) 
      random_position = randint(5, 20)

      next_song = next_song[0] + random_position
      song = song_box.get(next_song)

      # save value of song to date that is get(ACTIVE)
      data = song
      subprocess.run("pbcopy", text=True, input=data)

      # save value of song to song box that is get(ACTIVE)
      show_song = song
      # show song play to bar_play
      if len(show_song) > 50:
         show_song = show_song[:50]
         show_song = f"{show_song}..."
      show_song = show_song.upper() # upper text
      bar_play.configure(text=show_song)

      # save value of song to date that is get(ACTIVE)
      img_song = song
      check_song = song

      # check song if it has the background in the folder 
      check_song = f"{check_song}.png"

      # if the song is in the folder continue playing song 
      if check_song in list_background:
         # show background 
         img_song = f"background/{img_song}.png"
         background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(img_song), size=(800,600)))

         # play song 
         song = f"audio/{song}.mp3"
         pygame.mixer.music.load(song)
         pygame.mixer.music.play()

         # clear the current selection
         song_box.selection_clear(0, END)
         # get curselection to the next song 
         song_box.activate(next_song)
         song_box.selection_set(next_song, last=None)

         # change the img pause btn when moving 
         button_pause.configure(image=pause_img)

         play_time()
         slider_postition = int(length_song)
         scale_slider.config(to=slider_postition)
         scale_slider.set(0)
      else:
         # if not call play_song function to play that song again
         # play_song()

         # get the current song
         next_song = song_box.curselection()

         # get random number (random position) 
         random_position = randint(5, 20)

         next_song = next_song[0] - random_position
         song = song_box.get(next_song)

         # save value of song to date that is get(ACTIVE)
         data = song
         subprocess.run("pbcopy", text=True, input=data)

         # save value of song to song box that is get(ACTIVE)
         show_song = song
         # show song play to bar_play
         if len(show_song) > 50:
            show_song = show_song[:50]
            show_song = f"{show_song}..."
         show_song = show_song.upper() # upper text
         bar_play.configure(text=show_song)

         # save value of song to date that is get(ACTIVE)
         img_song = song

         # show background 
         img_song = f"background/{img_song}.png"
         background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(img_song), size=(800,600)))

         # play song 
         song = f"audio/{song}.mp3"
         pygame.mixer.music.load(song)
         pygame.mixer.music.play()

         # clear the current selection
         song_box.selection_clear(0, END)
         # get curselection to the next song 
         song_box.activate(next_song)
         song_box.selection_set(next_song, last=None)

         # change the img pause btn when moving 
         button_pause.configure(image=pause_img)

         play_time()
         slider_postition = int(length_song)
         scale_slider.config(to=slider_postition)
         scale_slider.set(0)

   # the next song (not random)
   else:
      # get the current song
      next_song = song_box.curselection()
      # add one: move to the next song + 1
      next_song = next_song[0] + 1
      song = song_box.get(next_song)

      # save value of song to date that is get(ACTIVE)
      data = song
      subprocess.run("pbcopy", text=True, input=data)

      # save value of song to song box that is get(ACTIVE)
      show_song = song
      # show song play to bar_play
      if len(show_song) > 50:
         show_song = show_song[:50]
         show_song = f"{show_song}..."
      show_song = show_song.upper() # upper text
      bar_play.configure(text=show_song)

      # save value of song to date that is get(ACTIVE)
      img_song = song
      check_song = song

      # check song if it has the background in the folder 
      check_song = f"{check_song}.png"
      
      # if the song is in the folder continue playing song 
      if check_song in list_background:
         # show background 
         img_song = f"background/{img_song}.png"
         background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(img_song), size=(800,600)))

         # play song 
         song = f"audio/{song}.mp3"
         pygame.mixer.music.load(song)
         pygame.mixer.music.play()

         # clear the current selection
         song_box.selection_clear(0, END)
         # get curselection to the next song 
         song_box.activate(next_song)
         song_box.selection_set(next_song, last=None)

         # change the img pause btn when moving 
         button_pause.configure(image=pause_img)

         play_time()
         slider_postition = int(length_song)
         scale_slider.config(to=slider_postition)
         scale_slider.set(0)
      else:
         # if not call play_song function to play that song again
         # play_song()

         # highlight the first song 
         song_box.activate(0)
         song_box.selection_set(0, last=None)

         # get the current song
         next_song = song_box.curselection()
         next_song = next_song[0]
         song = song_box.get(next_song)

         # save value of song to date that is get(ACTIVE)
         data = song
         subprocess.run("pbcopy", text=True, input=data)

         # save value of song to song box that is get(ACTIVE)
         show_song = song
         # show song play to bar_play
         if len(show_song) > 50:
            show_song = show_song[:50]
            show_song = f"{show_song}..."
         show_song = show_song.upper() # upper text
         bar_play.configure(text=show_song)

         # save value of song to date that is get(ACTIVE)
         img_song = song
         check_song = song

         # check song if it has the background in the folder 
         check_song = f"{check_song}.png"
         
         # if the song is in the folder continue playing song 
         if check_song in list_background:
            # show background 
            img_song = f"background/{img_song}.png"
            background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(img_song), size=(800,600)))

            # play song 
            song = f"audio/{song}.mp3"
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()

            # clear the current selection
            song_box.selection_clear(0, END)
            # get curselection to the next song 
            song_box.activate(next_song)
            song_box.selection_set(next_song, last=None)

            # change the img pause btn when moving 
            button_pause.configure(image=pause_img)

            play_time()
            slider_postition = int(length_song)
            scale_slider.config(to=slider_postition)
            scale_slider.set(0)

def next_song_shortcut(e):
   if random_mode == True:
      # get the current song
      next_song = song_box.curselection()

      # get random number (random position) 
      random_position = randint(5, 10)

      next_song = next_song[0] + random_position
      song = song_box.get(next_song)

      # save value of song to date that is get(ACTIVE)
      data = song
      subprocess.run("pbcopy", text=True, input=data)

      # save value of song to song box that is get(ACTIVE)
      show_song = song
      # show song play to bar_play
      if len(show_song) > 50:
         show_song = show_song[:50]
         show_song = f"{show_song}..."
      show_song = show_song.upper() # upper text
      bar_play.configure(text=show_song)

      # save value of song to date that is get(ACTIVE)
      img_song = song
      check_song = song

      # check song if it has the background in the folder 
      check_song = f"{check_song}.png"

      # if the song is in the folder continue playing song 
      if check_song in list_background:
         # show background 
         img_song = f"background/{img_song}.png"
         background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(img_song), size=(800,600)))

         # play song 
         song = f"audio/{song}.mp3"
         pygame.mixer.music.load(song)
         pygame.mixer.music.play()

         # clear the current selection
         song_box.selection_clear(0, END)
         # get curselection to the next song 
         song_box.activate(next_song)
         song_box.selection_set(next_song, last=None)

         # change the img pause btn when moving 
         button_pause.configure(image=pause_img)

         play_time()
         slider_postition = int(length_song)
         scale_slider.config(to=slider_postition)
         scale_slider.set(0)
      else:
         # if not call play_song function to play that song again
         # play_song()

         # get the current song
         next_song = song_box.curselection()

         # get random number (random position) 
         random_position = randint(5, 10)

         next_song = next_song[0] - random_position
         song = song_box.get(next_song)

         # save value of song to date that is get(ACTIVE)
         data = song
         subprocess.run("pbcopy", text=True, input=data)

         # save value of song to song box that is get(ACTIVE)
         show_song = song
         # show song play to bar_play
         if len(show_song) > 50:
            show_song = show_song[:50]
            show_song = f"{show_song}..."
         show_song = show_song.upper() # upper text
         bar_play.configure(text=show_song)

         # save value of song to date that is get(ACTIVE)
         img_song = song

         # show background 
         img_song = f"background/{img_song}.png"
         background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(img_song), size=(800,600)))

         # play song 
         song = f"audio/{song}.mp3"
         pygame.mixer.music.load(song)
         pygame.mixer.music.play()

         # clear the current selection
         song_box.selection_clear(0, END)
         # get curselection to the next song 
         song_box.activate(next_song)
         song_box.selection_set(next_song, last=None)

         # change the img pause btn when moving 
         button_pause.configure(image=pause_img)

         play_time()
         slider_postition = int(length_song)
         scale_slider.config(to=slider_postition)
         scale_slider.set(0)

   # Not random
   else:
      # get the current song
      next_song = song_box.curselection()
      # add one: move to the next song + 1
      next_song = next_song[0] + 1
      song = song_box.get(next_song)

      # save value of song to date that is get(ACTIVE)
      data = song
      subprocess.run("pbcopy", text=True, input=data)

      # save value of song to song box that is get(ACTIVE)
      show_song = song
      # show song play to bar_play
      if len(show_song) > 50:
         show_song = show_song[:50]
         show_song = f"{show_song}..."
      show_song = show_song.upper() # upper text
      bar_play.configure(text=show_song)

      # save value of song to date that is get(ACTIVE)
      img_song = song
      check_song = song

      # check song if it has the background in the folder 
      check_song = f"{check_song}.png"
      # print(check_song)

      # if the song is in the folder continue playing song 
      if check_song in list_background:
         # show background 
         img_song = f"background/{img_song}.png"
         background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(img_song), size=(800,600)))

         # play song 
         song = f"audio/{song}.mp3"
         pygame.mixer.music.load(song)
         pygame.mixer.music.play()

         # clear the current selection
         song_box.selection_clear(0, END)
         # get curselection to the next song 
         song_box.activate(next_song)
         song_box.selection_set(next_song, last=None)

         # change the img pause btn when moving 
         button_pause.configure(image=pause_img)

         play_time()
         slider_postition = int(length_song)
         scale_slider.config(to=slider_postition)
         scale_slider.set(0)
      else:
         # if not call play_song function to play that song again
         # play_song()

         # highlight the first song 
         song_box.activate(0)
         song_box.selection_set(0, last=None)

         # get the current song
         next_song = song_box.curselection()
         next_song = next_song[0]
         song = song_box.get(next_song)

         # save value of song to date that is get(ACTIVE)
         data = song
         subprocess.run("pbcopy", text=True, input=data)

         # save value of song to song box that is get(ACTIVE)
         show_song = song
         # show song play to bar_play
         if len(show_song) > 50:
            show_song = show_song[:50]
            show_song = f"{show_song}..."
         show_song = show_song.upper() # upper text
         bar_play.configure(text=show_song)

         # save value of song to date that is get(ACTIVE)
         img_song = song
         check_song = song

         # check song if it has the background in the folder 
         check_song = f"{check_song}.png"
         
         # if the song is in the folder continue playing song 
         if check_song in list_background:
            # show background 
            img_song = f"background/{img_song}.png"
            background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(img_song), size=(800,600)))

            # play song 
            song = f"audio/{song}.mp3"
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()

            # clear the current selection
            song_box.selection_clear(0, END)
            # get curselection to the next song 
            song_box.activate(next_song)
            song_box.selection_set(next_song, last=None)

            # change the img pause btn when moving 
            button_pause.configure(image=pause_img)

            play_time()
            slider_postition = int(length_song)
            scale_slider.config(to=slider_postition)
            scale_slider.set(0)

# play the previous song 
def previous_song():
   # get the current song 
   previous_song = song_box.curselection()
   previous_song = previous_song[0] - 1
   song = song_box.get(previous_song)

   # save value of song to date that is get(ACTIVE)
   data = song
   subprocess.run("pbcopy", text=True, input=data)

   # save value of song to show_song that is get() 
   show_song = song
   # show song play to bar_play
   if len(show_song) > 50:
      show_song = show_song[:50]
      show_song = f"{show_song}..."
   show_song = show_song.upper() # upper text
   bar_play.configure(text=show_song)

   # save value of song to date that is get(ACTIVE)
   img_song = song
   check_song = song

   # check song if it has the background in the folder 
   check_song = f"{check_song}.png"
   # print(check_song)
   
   # if the song is in the folder continue playing song 
   if check_song in list_background:
      # show background 
      img_song = f"background/{img_song}.png"
      background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(img_song), size=(800,600)))

      # play song 
      song = f"audio/{song}.mp3"
      pygame.mixer.music.load(song)
      pygame.mixer.music.play()

      # clear and highlight the previous song
      song_box.selection_clear(0, END)
      song_box.activate(previous_song)
      song_box.selection_set(previous_song, last=None)

      # change the img pause btn when moving 
      button_pause.configure(image=pause_img)

      play_time()
      slider_postition = int(length_song)
      scale_slider.config(to=slider_postition)
      scale_slider.set(0)

   else:
      # if not call play_song function to play that song again
      # play_song()
      # last_song = song_box.size() - 1
      # song_box.selection_set(last_song)

      global insert_song 
      the_last_song = insert_song * 199

      if insert_song > 1:
         the_last_song = the_last_song + (insert_song-1)
      # print(the_last_song)

      # clear highlight the song at the end 
      song_box.selection_clear(0, END)
      song_box.activate(the_last_song)
      song_box.selection_set(the_last_song, last=None)

      # get the current song
      previous_song = song_box.curselection()
      song = song_box.get(previous_song)

      # save value of song to date that is get(ACTIVE)
      data = song
      subprocess.run("pbcopy", text=True, input=data)

      # save value of song to show_song that is get() 
      show_song = song
      # show song play to bar_play
      if len(show_song) > 50:
         show_song = show_song[:50]
         show_song = f"{show_song}..."
      show_song = show_song.upper() # upper text
      bar_play.configure(text=show_song)

      # save value of song to date that is get(ACTIVE)
      img_song = song
      check_song = song

      # show background 
      img_song = f"background/{img_song}.png"
      background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(img_song), size=(800,600)))

      # play song 
      song = f"audio/{song}.mp3"
      pygame.mixer.music.load(song)
      pygame.mixer.music.play()

      # clear and highlight the previous song
      song_box.selection_clear(0, END)
      song_box.activate(previous_song)
      song_box.selection_set(previous_song, last=None)

      # change the img pause btn when moving 
      button_pause.configure(image=pause_img)

      play_time()
      slider_postition = int(length_song)
      scale_slider.config(to=slider_postition)
      scale_slider.set(0)

def previous_song_shortcut(e):
   # get the current song 
   previous_song = song_box.curselection()
   previous_song = previous_song[0] - 1
   song = song_box.get(previous_song)

   # save value of song to date that is get(ACTIVE)
   data = song
   subprocess.run("pbcopy", text=True, input=data)

   # save value of song to show_song that is get() 
   show_song = song
   # show song play to bar_play
   if len(show_song) > 50:
      show_song = show_song[:50]
      show_song = f"{show_song}..."
   show_song = show_song.upper() # upper text
   bar_play.configure(text=show_song)

   # save value of song to date that is get(ACTIVE)
   img_song = song
   check_song = song

   # check song if it has the background in the folder 
   check_song = f"{check_song}.png"
   # print(check_song)
   
   # if the song is in the folder continue playing song 
   if check_song in list_background:
      # show background 
      img_song = f"background/{img_song}.png"
      background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(img_song), size=(800,600)))

      # play song 
      song = f"audio/{song}.mp3"
      pygame.mixer.music.load(song)
      pygame.mixer.music.play()

      # clear and highlight the previous song
      song_box.selection_clear(0, END)
      song_box.activate(previous_song)
      song_box.selection_set(previous_song, last=None)

      # change the img pause btn when moving 
      button_pause.configure(image=pause_img)

      play_time()
      slider_postition = int(length_song)
      scale_slider.config(to=slider_postition)
      scale_slider.set(0)

   else:
      # if not call play_song function to play that song again
      # play_song()
      # last_song = song_box.size() - 1
      # song_box.selection_set(last_song)

      global insert_song 
      the_last_song = insert_song * 199

      if insert_song > 1:
         the_last_song = the_last_song + (insert_song-1)
      # print(the_last_song)

      # clear highlight the song at the end 
      song_box.selection_clear(0, END)
      song_box.activate(the_last_song)
      song_box.selection_set(the_last_song, last=None)

      # get the current song
      previous_song = song_box.curselection()
      song = song_box.get(previous_song)

      # save value of song to date that is get(ACTIVE)
      data = song
      subprocess.run("pbcopy", text=True, input=data)

      # save value of song to show_song that is get() 
      show_song = song
      # show song play to bar_play
      if len(show_song) > 50:
         show_song = show_song[:50]
         show_song = f"{show_song}..."
      show_song = show_song.upper() # upper text
      bar_play.configure(text=show_song)

      # save value of song to date that is get(ACTIVE)
      img_song = song
      check_song = song

      # show background 
      img_song = f"background/{img_song}.png"
      background_label.configure(image=customtkinter.CTkImage(light_image = Image.open(img_song), size=(800,600)))

      # play song 
      song = f"audio/{song}.mp3"
      pygame.mixer.music.load(song)
      pygame.mixer.music.play()

      # clear and highlight the previous song
      song_box.selection_clear(0, END)
      song_box.activate(previous_song)
      song_box.selection_set(previous_song, last=None)

      # change the img pause btn when moving 
      button_pause.configure(image=pause_img)

      play_time()
      slider_postition = int(length_song)
      scale_slider.config(to=slider_postition)
      scale_slider.set(0)

# stop playing and continue playing 
def pause():
   if pygame.mixer.music.get_busy() == True:
      pygame.mixer.music.pause()
      button_pause.configure(image=stop_img)
   else:
      pygame.mixer.music.unpause()
      button_pause.configure(image=pause_img)

#shortcut
def pause_shortcut(e): 
   if pygame.mixer.music.get_busy() == True:
      pygame.mixer.music.pause()
      button_pause.configure(image=stop_img)
   else:
      pygame.mixer.music.unpause()
      button_pause.configure(image=pause_img)

# add song the Listbox
def add_one_song():
   song = filedialog.askopenfilename(initialdir="audio/", title="Choose a song", filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
   # delete base (/User...audio/) then delete ext (.mp3)
   song = song[41:]
   song = song.replace(".mp3", "")
   song_box.insert(7, song)

   # clear current song
   song_box.selection_clear(0, END)
   # highligh the song that is added 
   song_box.activate(7)
   song_box.selection_set(7, last=None)

def add_many_song():
   songs = filedialog.askopenfiles(initialdir="audio/", title="Choose songs", filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
   for song in songs:
      # get the song name 
      song = os.path.basename(song.name)
      song = song.replace(".mp3", "")      
      song_box.insert(7, song)

      # clear current song
      song_box.selection_clear(0, END)
      # highligh the song that is added 
      song_box.activate(7)
      song_box.selection_set(7, last=None)

def add_songs(e):
   songs = filedialog.askopenfiles(initialdir="audio/", title="Choose songs", filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
   for song in songs:
      # get the song name 
      song = os.path.basename(song.name)
      song = song.replace(".mp3", "")      
      song_box.insert(7, song)

      # clear current song
      song_box.selection_clear(0, END)
      # highligh the song that is added 
      song_box.activate(7) 
      song_box.selection_set(7, last=None)

# remove song 
def delete_song():
   current_song = song_box.curselection()
   song_box.delete(ANCHOR)

   # stop playing 
   # pygame.mixer.music.stop()

   # get the current song
   # add one: move to the next song + 1
   current_song = current_song[0] + 1

   song = song_box.get(current_song)   
   # song = f"audio/{song}.mp3"
   # pygame.mixer.music.load(song)
   # pygame.mixer.music.play()

   song_box.selection_clear(0, END)
   song_box.activate(current_song)
   song_box.selection_set(current_song, last=None)

def delete_song_shortcut(e): # shortcut
   current_song = song_box.curselection()
   song_box.delete(ANCHOR)

   # stop playing 
   # pygame.mixer.music.stop()

   # get the current song
   # add one: move to the next song + 1
   current_song = current_song[0] + 1
   
   # play song 
   # song = song_box.get(current_song)   
   # song = f"audio/{song}.mp3"
   # pygame.mixer.music.load(song)
   # pygame.mixer.music.play()

   # clear and highlight song 
   song_box.selection_clear(0, END)
   song_box.activate(current_song)
   song_box.selection_set(current_song, last=None)

# delete all songs 
def delete_songs():
   song_box.delete(0, END)
   pygame.mixer.music.stop()

def delete_songs_shortcut(e): # shortcut
   song_box.delete(0, END)
   pygame.mixer.music.stop()

# setting 
def edit_menu():
   webbrowser.open("file:///Users/client/Desktop/python/ZINFY/ver4.py")
def edit_button():
   webbrowser.open("file:///Users/client/Desktop/python/ZINFY/ver4.py")
def edit_shortcut(e):
   webbrowser.open("file:///Users/client/Desktop/python/ZINFY/ver4.py")

# close program 
def quit_program(e): 
   # close window 
   root.destroy()

# edit the volume 
def set_volume(value):
   volume = int(value) / 100
   pygame.mixer.music.set_volume(volume)

def slider(x):
   # converted_current_song = time.strftime("%M:%S", time.gmtime(length_song))
   current_time = scale_slider.get()
   # print(current_time)
   # print(length_song)

   # check if the current time of the song is equal to the total length of thesong
   if current_time == int(length_song) and sleep_after_song_end == True:
      subprocess.call(['osascript', '-e', 'tell app "System Events" to sleep'])
      exit()
   # auto play to the next song 
   if current_time == int(length_song) and auto_play == True and repeat_song == False:
      next_song()
   # repeat song 
   if current_time == int(length_song) and repeat_song == True and auto_play == False:
      play_song() 

   if current_time == int(length_song) and repeat_song == False and auto_play == False:
      button_pause.configure(image=stop_img)
      label_process_left.configure(text="00:00")
   # label_slider.config(text=f"{int(current_time)} of {converted_current_song}")

def auto_play_song():
   global auto_play

   if not auto_play:
      auto_play = True
      button_autoplay_song.configure(image=auto_on)
   else:
      auto_play = False
      button_autoplay_song.configure(image=auto_off)

def repeat_play_song():
   global repeat_song
   # Câu if not auto_play lệnh kiểm tra xem giá trị của biến auto_play có đúng không (nghĩa là sai)
   # Nếu giá trị là sai, khối mã bên trong câu lệnh if được thực thi.
   if not repeat_song:
      repeat_song = True
      button_repeat_song.configure(image=rewind_on)
   else:
      repeat_song = False
      button_repeat_song.configure(image=rewind_off)

def auto_play_song_shortcut(e):
   global auto_play
   if not auto_play:
      auto_play = True
      button_autoplay_song.configure(image=auto_on)
   else:
      auto_play = False
      button_autoplay_song.configure(image=auto_off)

def repeat_play_song_shortcut(e):
   global repeat_song
   # Câu if not auto_play lệnh kiểm tra xem giá trị của biến auto_play có đúng không (nghĩa là sai)
   # Nếu giá trị là sai, khối mã bên trong câu lệnh if được thực thi.
   if not repeat_song:
      repeat_song = True
      button_repeat_song.configure(image=rewind_on)
   else:
      repeat_song = False
      button_repeat_song.configure(image=rewind_off)

def sleep():
   global sleep_after_song_end
   if not sleep_after_song_end:
      sleep_after_song_end = True
      button_sleep.configure(text="Sleep: on")
   else:
      sleep_after_song_end = False
      button_sleep.configure(text="Sleep: off")

def sleep_shortcut(e):
   global sleep_after_song_end
   if not sleep_after_song_end:
      sleep_after_song_end = True
      button_sleep.configure(text="Sleep: on")
   else:
      sleep_after_song_end = False
      button_sleep.configure(text="Sleep: off")

def random_song():
   global random_mode
   if not random_mode:
      random_mode = True
      button_random_song.configure(image=random_on)
   else:
      random_mode = False
      button_random_song.configure(image=random_off)

def random_song_shortcut(e):
   global random_mode
   if not random_mode:
      random_mode = True
      button_random_song.configure(image=random_on)
   else:
      random_mode = False
      button_random_song.configure(image=random_off)

# hide and unhide song box 
def hide_unhide_song_box():
   global hide_unhide 
   if not hide_unhide:
      hide_unhide = True
   else:
      hide_unhide = False

   if hide_unhide == True: 
      # widget.pack_forget()
      frame_song_box_scroll.place(y=700)
   else:
      frame_song_box_scroll.place(x=63, y=130)

def hide_unhide_song_box_shortcut(e):
   global hide_unhide 
   if not hide_unhide:
      hide_unhide = True
   else:
      hide_unhide = False

   if hide_unhide == True: 
      # widget.pack_forget()
      frame_song_box_scroll.place(y=700)
   else:
      frame_song_box_scroll.place(x=63, y=130)

def ventura_shortcut(e):
   global ventura
   if not ventura:
      ventura = True
   else:
      ventura = False

   # hide all buttons and only show background with bar_play
   if ventura == True:
      # hide all buttons
      frame_song_box_scroll.place(y=10000)
      control_frame.place(y=10000)
      scale_volume.place(y=10000)
      button_random_song.place(y=10000)
      label_process_left.place(y=10000)
      label_process_right.place(y=10000)
      label_under_slider.place(y=10000)
      scale_slider.place(y=10000)

   else:
      # return the original place of buttons 
      frame_song_box_scroll.place(x=63, y=130)
      control_frame.place(x=226.2, y=470)
      scale_volume.place(x=764, y=150)
      label_process_left.place(x=230, y=513)
      label_process_right.place(x=539, y=513)
      label_under_slider.place(x=255, y=513)
      scale_slider.place(x=269, y=525)
      button_random_song.place(x=170, y=474)

def close_popup(e):
   tab.destroy()

def load_video():
   txt = text.get("1.0", "end")
   print(txt)

def load_video_shortcut(e):
   txt = text.get("1.0", "end")
   print(txt)

# define variable
auto_play = True
repeat_song = False 
sleep_after_song_end = False
random_mode = False
hide_unhide = False
ventura = False
insert_song = 1

# images button 
play_img = customtkinter.CTkImage(light_image=Image.open("images/play.png"), size=(30,30))
pause_img = customtkinter.CTkImage(light_image=Image.open("images/pause.png"), size=(30,30)) 
stop_img = customtkinter.CTkImage(light_image=Image.open("images/stop.png"), size=(30,30)) 
next_song_img = customtkinter.CTkImage(light_image=Image.open("images/next.png"), size=(30,30))
previous_img = customtkinter.CTkImage(light_image=Image.open("images/previous.png"), size=(30,30))
ventura_img = customtkinter.CTkImage(light_image = Image.open("images/ventura.png"), size=(30,30))
auto_on = customtkinter.CTkImage(light_image = Image.open("images/autoplay_on.png"), size=(25,25))
auto_off = customtkinter.CTkImage(light_image = Image.open("images/autoplay_off.png"), size=(25,25))
rewind_on = customtkinter.CTkImage(light_image = Image.open("images/rewind_on.png"), size=(25,25))
rewind_off = customtkinter.CTkImage(light_image = Image.open("images/rewind_off.png"), size=(25,25))
random_on = customtkinter.CTkImage(light_image=Image.open("images/random_on.png"), size=(25,25))
random_off = customtkinter.CTkImage(light_image=Image.open("images/random_off.png"), size=(25,25))

# set background 
canvas = Canvas(root, bg="#FBFCFC", height=600, width=800)
canvas.pack()

# background_img = customtkinter.CTkImage(light_image=Image.open("images/background.png"),  size=(800,600))
# background_img = customtkinter.CTkImage(light_image=Image.open("images/ventura.png"),  size=(800,600))
background_label = customtkinter.CTkLabel(root, image="", text="")
background_label.place(x=0, y=0, relheight=1, relwidth=1)   

frame_song_box_scroll = customtkinter.CTkFrame(root, fg_color="transparent", width=400, height=380)
frame_song_box_scroll.pack(fill=BOTH, expand=True)
frame_song_box_scroll.place(x=63, y=130)
# frame_song_box_scroll.place(x=63, y=830)

# song box #FBFCFC
song_box = Listbox(frame_song_box_scroll, bg="#FBFCFC", fg="#212F3D", width=52, font=("Kozuka Gothic Pro M", 20), selectbackground="#CACFD2", selectforeground="#F4F6F7", borderwidth=0, \
   relief="flat", highlightcolor="black", )
song_box.pack(side=LEFT, fill=BOTH)

# scroll 
scroll_bar = customtkinter.CTkScrollbar(frame_song_box_scroll, orientation="vertical",
   button_color="#2E86C1",
   button_hover_color="#797D7F")
scroll_bar.configure(command=song_box.yview)
scroll_bar.pack(side=RIGHT, fill=Y)

song_box.config(yscrollcommand=scroll_bar.set)

# print song on song box 
for song in range(200):
   # get list_music from listmusic.py 
   song = random.choice(list_music)
   song = song.replace("audio/", "")
   song = song.replace(".mp3", "")

   # insert name song on song box 
   song_box.insert(0, song)
   
   # clear the current selection
   song_box.selection_clear(0, END)
   # highlight the first song name 
   song_box.activate(7)
   song_box.selection_set(7, last=None)

# notebook.add(frame_song_box_scroll, text="All")

# show what song that is being play 

bar_play = customtkinter.CTkButton(root, text="Let choose a song and play", font=("roboto", 23), text_color="#FBFCFC",\
   command=hide_unhide_song_box, border_width=0,)
bar_play.pack()
bar_play.place(x=60, y=60)

# frame 
control_frame = Frame(root, bg="#FBFCFC")
control_frame.pack()
control_frame.place(x=226.2 , y=470)

# player button
button_autoplay_song = customtkinter.CTkButton(control_frame, text="", image=auto_on, command=auto_play_song, width=3)
button_autoplay_song.grid(row=0, column=1, padx=7)

button_repeat_song = customtkinter.CTkButton(control_frame, text="", image=rewind_off, command=repeat_play_song, width=3)
button_repeat_song.grid(row=0, column=6, padx=7)

button_play = customtkinter.CTkButton(control_frame, image=play_img, text="", command=play_song, width=5)
button_play.grid(row=0, column=2, padx=7)

button_pause = customtkinter.CTkButton(control_frame, image=pause_img, text="", command=pause, width=5)
button_pause.grid(row=0, column=4, padx=7)

button_next_song = customtkinter.CTkButton(control_frame, image=next_song_img, text="", command=next_song, width=5)
button_next_song.grid(row=0, column=5, padx=7)

button_foward_song = customtkinter.CTkButton(control_frame, image=previous_img, text="", command=previous_song, width=5)
button_foward_song.grid(row=0, column=3, padx=7)

button_random_song = customtkinter.CTkButton(root, text="", image=random_off, command=random_song, width=5)
button_random_song.pack()
button_random_song.place(x=170, y=474)

'''
button_insert_song = customtkinter.CTkButton(root, text="Add song", font=("Kozuka Gothic Pro M", 15), command=insert_song, text_color=text_color) #, fg="#4D5656"
button_insert_song.pack()
button_insert_song.place(x=-7, y=440)

button_sleep = customtkinter.CTkButton(root, text="Sleep: off", font=("Kozuka Gothic Pro M", 15), command=sleep, text_color=text_color)
button_sleep.pack()
button_sleep.place(x=-7, y=473)

button_edit = customtkinter.CTkButton(root, text="Setting", font=("Kozuka Gothic Pro M", 15), command=edit_button, text_color=text_color)
button_edit.pack()
button_edit.place(x=-7, y=506)

button_delete = customtkinter.CTkButton(root, text="Delete", font=("Kozuka Gothic Pro M", 15), command=delete_song)
button_delete.pack()
button_delete.place(x=-7, y=539)
'''

# Scale 
# Control volume
scale_volume = customtkinter.CTkSlider(root, from_=0, to=100, command=set_volume, \
   cursor="hand2", state=NORMAL, orientation=VERTICAL, width=22)
scale_volume.pack()
scale_volume.set(60)
scale_volume.place(x=764, y=150)

# background for slider 
label_under_slider = customtkinter.CTkLabel(root, text="lable under slider lable under slider lable under slider", 
   fg_color="#E5E7E9", text_color="#E5E7E9")
label_under_slider.pack()
label_under_slider.place(x=255, y=513)

# bar process  
scale_slider = Scale(root, from_=0, to=100, command=slider, state=NORMAL, showvalue = 0, 
   troughcolor = "#3498DB", width=3, orient=HORIZONTAL, length=260, 
   bg="#E5E7E9", activebackground="#E5E7E9") # bg="#E5E7E9"
scale_slider.set(0)
scale_slider.pack()
scale_slider.place(x=269, y=525)

# scale_slider = customtkinter.CTkSlider(root, from_=0, to=100, command=slider, state=NORMAL, 
#    width=360, orientation=HORIZONTAL, 
# ) # bg="#E5E7E9"
# scale_slider.set(0)
# scale_slider.pack()
# scale_slider.place(x=269, y=525)

# process_bar = customtkinter.CTkProgressBar(root)
# process_bar.set(0)
# process_bar.pack()
# process_bar.place(x=269, y=550)

# process bar 
label_bottom = customtkinter.CTkLabel(root, text="", fg_color="#E5E7E9", text_color="#212F3D")
label_bottom.pack(side=BOTTOM, fill=X, ipadx=2)

label_process_left = customtkinter.CTkLabel(root, text="00:00", fg_color="#E5E7E9", text_color="#212F3D")
label_process_left.pack()
label_process_left.place(x=230, y=513)

label_process_right = customtkinter.CTkLabel(root, text="00:00", fg_color="#E5E7E9", text_color="#212F3D")
label_process_right.pack()
label_process_right.place(x=539, y=513)

# create menu 
my_menu = Menu(root)

# setting 
setting = Menu(my_menu)
my_menu.add_cascade(label="Setting", menu=setting)
setting.add_command(label="Edit", command=edit_menu)

# add one song 
add_song = Menu(my_menu)
my_menu.add_cascade(label="Add song", menu=add_song)
add_song.add_command(label="Add one song", command=add_one_song)
# add many songs
add_song.add_command(label="Add many songs", command=add_many_song)

# remove song 
delete_one_song = Menu(my_menu)
my_menu.add_cascade(label="Delete", menu=delete_one_song)
# one song 
delete_one_song.add_command(label="Delete one song", command=delete_song)
# all songs 
delete_one_song.add_command(label="Delete all songs", command=delete_songs)

# menu 
root.configure(menu=my_menu)

# key shortcut 
root.bind("<Command-w>", quit_program)
root.bind("<Command-,>", edit_shortcut)
root.bind("<Command-f>", add_songs)
root.bind("<Right>", next_song_shortcut)
root.bind("<l>", next_song_shortcut)
root.bind("k", pause_shortcut)
root.bind("<space>", pause_shortcut)
root.bind("<Left>", previous_song_shortcut)
root.bind("<j>", previous_song_shortcut)
root.bind("<BackSpace>", delete_song_shortcut)
root.bind("<Command-BackSpace>", delete_songs_shortcut)
root.bind("<s>", play_song_shortcut)
root.bind("<a>", auto_play_song_shortcut)
root.bind("<r>", repeat_play_song_shortcut)
root.bind("<q>", sleep_shortcut)
root.bind("<i>", insert_song_short)
root.bind("<b>", hide_unhide_song_box_shortcut)
root.bind("<Command-v>", ventura_shortcut)
root.bind("<r>", random_song_shortcut)
 
# root.eval('tk::PlaceWindow . center')
root.mainloop()
