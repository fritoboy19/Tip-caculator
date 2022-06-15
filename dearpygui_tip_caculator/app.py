# app.py - My DearPyGUI windowed app
import dearpygui.dearpygui as dpg

dpg.create_context()

total_id=dpg.generate_uuid()
output_id = dpg.generate_uuid()
y=dpg.generate_uuid()
#caculations
def caculation_A():
    perctange =str(dpg.get_value(total_id)/100*4)
    output= perctange
    dpg.set_value(y, perctange)

def caculation_B():
    perctange =str(dpg.get_value(total_id)/100*5)
    output= perctange
    dpg.set_value(y, perctange)

def caculation_C():
    perctange =str(dpg.get_value(total_id)/100*10)
    output= perctange
    dpg.set_value(y, perctange)

def caculation_D():
    perctange =str(dpg.get_value(total_id)/100*15)
    output= perctange
    dpg.set_value(y, perctange)

def caculation_E():
    perctange =str(dpg.get_value(total_id)/100*20)
    output= perctange
    dpg.set_value(y, perctange)

def caculation_F():
    perctange =str(dpg.get_value(total_id)/100*25)
    output= perctange
    dpg.set_value(y, perctange)

#GUI
dpg.create_viewport(title='Tip Caculator', width=600, height=400)
with dpg.window(label="Tip Caculator", width=600, height=400 ):
    dpg.add_text("Welcome to the Tip Caculator")

    dpg.add_input_float(label="Total Amount", width=100, tag=total_id )
#title 
    dpg.add_text("Tip percentage")
#percentages 
    dpg.add_button(label="4%",callback=caculation_A)
    dpg.add_button(label="5%",callback=caculation_B)
    dpg.add_button(label="10%",callback=caculation_C)
    dpg.add_button(label="15%",callback=caculation_D)
    dpg.add_button(label="20%",callback=caculation_E)
    dpg.add_button(label="25%",callback=caculation_F)
    dpg.add_text("Tip amount:",tag=y)
    # dpg.add_text("",tag=y)
    
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()