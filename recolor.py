import argparse
from PIL import Image
import os,glob,sys

parser = argparse.ArgumentParser(description='Icons recolor script')
parser.add_argument('-p', type=str) # path
parser.add_argument('-c', default="#000000") # color

SRC_DIR = parser.parse_args().p
COLOR = parser.parse_args().c

clr = str(COLOR).replace("#","").strip()
R_NEW, G_NEW, B_NEW = tuple(int(clr[i:i+2],16) for i in (0, 2 ,4))
DEST_DIR = os.path.join(SRC_DIR,'recolored_{}'.format(clr))

if not os.path.exists(DEST_DIR):
	os.mkdir(DEST_DIR)

def recolor(png,clr):
	img_name = os.path.basename(png)
	im = Image.open(png).convert("RGBA")
	pixels = im.load()
	width, height = im.size
	for x in xrange(width):
		for y in xrange(height):
			r, g, b, a = im.getpixel((x, y))
			pixels[x, y] = (R_NEW, G_NEW, B_NEW, a)
	im.save(os.path.join(DEST_DIR,img_name))

for j in glob.glob(os.path.join(SRC_DIR,"*.png")):
	recolor(j, clr)
