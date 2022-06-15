# app.py - My DearPyGUI windowed app
from turtle import color
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
dpg.create_viewport(title='Tip Caculator', width=250, height=200)
with dpg.window(label="Tip Caculator", width=250, height=200 ):
    dpg.add_text("Welcome to the Tip Caculator")

    dpg.add_input_float(label="Total Amount", width=100, tag=total_id )
#title 
    dpg.add_text("Tip percentage")
#percentages 
    dpg.add_button(label="4%",callback=caculation_A)
    dpg.add_same_line()
    dpg.add_button(label="5%",callback=caculation_B)
    dpg.add_same_line()
    dpg.add_button(label="10%",callback=caculation_C)
    dpg.add_button(label="15%",callback=caculation_D)
    dpg.add_same_line()
    dpg.add_button(label="20%",callback=caculation_E)
    dpg.add_same_line()
    dpg.add_button(label="25%",callback=caculation_F)
    dpg.add_text("Tip amount:")
    dpg.add_text("",tag=y)

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (39, 76, 125), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 10, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()