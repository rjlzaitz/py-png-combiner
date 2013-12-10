import os, sys
from PIL import Image

# face cookie naming: face-[face-type][hat-type][acc-type].png
# message cookie naming: msg-[frosting-type][border-type][message-type]
# for example: a snowman with a top hat and bow tie would be face-441.png
# for example: a bah humbug with silver balls and green frosting would be msg-241.png 

#face cookies file array
faces = ("face-1.png", "face-2.png", "face-3.png", "face-4.png")
hats = ("hat-1.png", "hat-2.png", "hat-3.png", "hat-4.png")
accessories = ("acc-1.png", "acc-2.png", "acc-3.png", "acc-4.png")

#create each face cookie and save
for face in faces:
	for hat in hats:
		for accessory in accessories:
			
			#create filename using index of each component
			face_id = str(faces.index(face) + 1)
			hat_id = str(hats.index(hat) + 1)
			acc_id = str(accessories.index(accessory) + 1)
			filename = "face-" + face_id + hat_id + acc_id + ".png"
			
			#open each needed image
			cookie = Image.open("Cookie blank.png")
			img_a = Image.open("Face/" + face)
			img_b = Image.open("Face/" + hat)
			img_c = Image.open("Face/" + accessory)

			#combine the images and save with correct filename
			img_start = Image.composite(img_b, img_a, img_b)
			img_middle = Image.composite(img_c, img_start, img_c)
			img_final = Image.composite(img_middle, cookie, img_middle).save(filename)

#message cookies file array
frostings = ("frost-1.png", "frost-2.png", "frost-3.png", "frost-4.png")
borders = ("border-1.png", "border-2.png", "border-3.png", "border-4.png") 
messages = ("msg-1.png", "msg-2.png", "msg-3.png", "msg-4.png") 

#create each message cookie and save
for frosting in frostings:
	for border in borders:
		for message in messages:

			#create filename using index of each component
			frosting_id = str(frostings.index(frosting) + 1)
			border_id = str(borders.index(border) + 1)
			message_id = str(messages.index(message) + 1)
			filename = "msg-" + frosting_id + border_id + message_id + ".png"

			#open each needed image
			cookie = Image.open("Cookie blank.png")
			img_a = Image.open("Message/" + frosting)
			img_b = Image.open("Message/" + border)
			img_c = Image.open("Message/" + message)

			#combine the images and save with correct filename
			img_start = Image.composite(img_b, img_a, img_b)
			img_middle = Image.composite(img_c, img_start, img_c)
			img_final = Image.composite(img_middle, cookie, img_middle).save(filename)
						


