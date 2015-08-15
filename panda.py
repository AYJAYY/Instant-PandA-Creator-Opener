import webbrowser

while 1 == 1:
	url_to_split = raw_input("Enter URL:")
	split = url_to_split.split("preview")
	link = split[0] + "previewandaccept" + split[1] 
	new_tab = 2
<<<<<<< HEAD
	webbrowser.open(link, new=new_tab)
=======
	webbrowser.open(link, new=new_tab)
>>>>>>> origin/master
