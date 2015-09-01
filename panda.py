# This is a standard package in Python 2.* 
import webbrowser

# This will keep the program running after you enter a preview link
while True:
    # Try to make the PandA
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
    # If it fails to make the PandA in anyway print out "Invalid URL"
    except:
        # If there is any kind of error - This is currently a catch all
        print "Invalid URL"
