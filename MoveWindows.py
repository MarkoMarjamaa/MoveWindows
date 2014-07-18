#!/usr/bin/env python

import win32gui
import time
import win32api
import sys

def enumChildHandler(hwndChild, lParam):
	if win32gui.IsWindowVisible(hwndChild):
		rect = win32gui.GetWindowRect(hwndChild)
		x = rect[0]
		y = rect[1]
		w = rect[2] - x
		h = rect[3] - y
		print "\tLocation: (%d, %d) \t    Size: (%d, %d) \tWindow:%s" % (x, y,w, h,win32gui.GetWindowText(hwndChild))
		if ( x >=  width) :
			print "wrong, new X :%d" % ( x % width )


def enumParentHandler(hwnd, lParam):

	if win32gui.IsWindowVisible(hwnd):
		rect = win32gui.GetWindowRect(hwnd)
		x = rect[0]
		y = rect[1]
		w = rect[2] - x
		h = rect[3] - y
#		print "Location: (%d, %d) \t    Size: (%d, %d) \tWindow:%s" % (x, y,w, h,win32gui.GetWindowText(hwnd))
		# If windows is outside screen
		if ( x >=  width) :
			print "Location: (%d, %d) \t    Size: (%d, %d) \tWindow:%s" % (x, y,w, h,win32gui.GetWindowText(hwnd))
			print "wrong, new X :%d" % ( x % width )
			#Move window to screen
			win32gui.MoveWindow(hwnd, x % width, y % height, w, h, True)
#		if (win32gui.IsIconic(hwnd)) : 
#			print "Minimized"
#	try:
#		win32gui.EnumChildWindows(hwnd, enumChildHandler, None)
#	except :
#		pass


# Call main
if __name__ == "__main__":

	width  = win32api.GetSystemMetrics (0)
	height = win32api.GetSystemMetrics (1)

	#print "width =", width
	#print "height =", height

	if len(sys.argv) < 2:
		# Loop all windows
		win32gui.EnumWindows(enumParentHandler, None)
	else : 
		while True:
			win32gui.EnumWindows(enumParentHandler, None)
			time.sleep(float(sys.argv[1]))
			print "Refresh"
