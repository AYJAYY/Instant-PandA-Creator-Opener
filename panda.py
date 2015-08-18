# This is a standard package in Python 2.* 
import webbrowser

while True:
    try:
        # Get the Preview URL
        url_to_split = raw_input("Enter URL:")
        # Split @ and remove preview
        split = url_to_split.split("preview")
        # Create the PandA
        link = split[0] + "previewandaccept" + split[1]
        # Make sure it opens in a new tab
        new_tab = 2
        # Open the browser with the PandA
        webbrowser.open(link, new=new_tab)

    except:
        # If there is any kind of error - This is currently a catch all
        # This will appear for ANY error
        print "Invalid URL"
