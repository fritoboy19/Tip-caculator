# app.py - My DearPyGUI windowed app
from cProfile import label
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Roast Caculator', width=600, height=300)

with dpg.window(label="Roast Caculator", width=600, height=300 ):
    dpg.add_text("Welcome to the Roast Caculator")
    dpg.add_input_int(label="maximum value", width=100)
    dpg.add_input_text(label="Action 1", width=200)
    dpg.add_input_int(label="Action 1 value", width=100)
    dpg.add_input_text(label="Action 2", width=200)
    dpg.add_input_int(label="Action 2 value", width=100)
    dpg.add_input_text(label="Action 3", width=200)
    dpg.add_input_int(label="Action 3 value", width=100)
    dpg.add_button(label="Calculate")
    dpg.add_button(label="Clear")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()