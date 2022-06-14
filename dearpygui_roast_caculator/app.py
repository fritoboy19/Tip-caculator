# app.py - My DearPyGUI windowed app
from locale import ABDAY_1
from turtle import width
import dearpygui.dearpygui as dpg

dpg.create_context()

#Generate unique ids for all widgets we want to change in runtime
MV_id= dpg.generate_uuid()
A1_id= dpg.generate_uuid()
A2_id= dpg.generate_uuid()
A3_id= dpg.generate_uuid()
output_id= dpg.generate_uuid()


dpg.create_viewport(title='Roast Caculator', width=600, height=300)

with dpg.window(label="Roast Caculator", width=600, height=300 ):
    dpg.add_text("Welcome to the Roast Caculator")
    dpg.add_input_int(label="Maximum Value", width=100, tag=MV_id)
    dpg.add_input_text(label="Action 1", width=200)
    dpg.add_input_int(label="Action 1 value", width=100, tag=A1_id)
    dpg.add_input_text(label="Action 2", width=200)
    dpg.add_input_int(label="Action 2 value", width=100, tag=A2_id)
    dpg.add_input_text(label="Action 3", width=200)
    dpg.add_input_int(label="Action 3 value", width=100, tag=A3_id)
    dpg.add_button(label="Calculate")
    dpg.add_button(label="Clear")
    dpg.add_text("", tag=output_id, width=400)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()