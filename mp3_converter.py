from moviepy.editor import *
import os
file_list = list(os.listdir("C:\\Users\\PIT000\\Downloads\\Video\\temp3\\"))
print(file_list)
for file in file_list:
    video = VideoFileClip("C:\\Users\\PIT000\\Downloads\\Video\\temp3\\"+file)
    print(file)
    if ".mkv" in file:
        video = AudioFileClip("C:\\Users\\PIT000\\Downloads\\Video\\temp3\\"+file)
        video.write_audiofile("C:\\Users\\PIT000\\Desktop\\music\\"+file.replace(".mkv",".mp3"))
    if ".mkv" not in file:
        print("C:\\Users\\PIT000\\Desktop\\music\\"+file)
        video.audio.write_audiofile("C:\\Users\\PIT000\\Desktop\\music\\"+file.replace(".mp4",".mp3"))

folder_name=""
file_list=[]

# lb.grid(column=1, row=4)
# def convert_to_mp3(folder_name):
#     global file_list
#     # for file in file_list:
#     #     video = VideoFileClip(os.path.join(folder_name,file))
#     #     print(file)
#     #     if ".mkv" in file:
#     #         video = AudioFileClip(os.path.join(folder_name,file))
#     #         video.write_audiofile("C:\\Users\\PIT000\\Desktop\\music\\"+file.replace(".mkv",".mp3"))
#     #     if ".mkv" not in file:
#     #         video.audio.write_audiofile("C:\\Users\\PIT000\\Desktop\\music\\"+file.replace(".mp4",".mp3"))
# def showFileList():
#     global listbox
#     global file_list
#     for file in file_list:
#         lb.insert("end",file)
# def select_folder():
#     global folder_name
#     global file_list
#     filetypes = (
#         ('text files', '*.txt'),
#         ('All files', '*.*')
#     )
#     folder_name = fd.askdirectory(
#         title='Select Folder',
#         initialdir='/'
#         # ,filetypes=filetypes
#         )
#     file_list = list(os.listdir(folder_name))
#     showFileList()
#     showinfo(
#         title='Selected Folder',
#         message=folder_name
#     )

# open_button = ttk.Button(
#     frm,
#     text='Open a Folder',
#     command=select_folder
# ).grid(column=1, row=1)

# open_button = ttk.Button(
#     frm,
#     text='Convert',
#     command=lambda:convert_to_mp3(folder_name)
# ).grid(column=1, row=2)

# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)

# root.mainloop()






