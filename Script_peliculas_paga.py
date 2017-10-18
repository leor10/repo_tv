

import plugintools


def Teclado():
	plugintools.keyboard_input()
	
# Entry point
def run():
    plugintools.log("main_list")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()
				
# Main menu
def main_list(params):
    plugintools.log("main_list "+repr(params))

    plugintools.add_item( 
        action="Teclado", 
        title="VOLVER AL FUTURO 1" ,
        url="https://www953.playercdn.net/186/0/gowR-_3wLrd0fphAtLUOzQ/1508428925/170425/727IcgyKRjWzZet.mp4" ,
        folder=True )   