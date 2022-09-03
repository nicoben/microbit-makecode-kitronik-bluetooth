def on_bluetooth_disconnected():
    basic.show_icon(IconNames.SAD)
def on_bluetooth_connected():
    basic.show_icon(IconNames.HAPPY)

def on_mes_dpad_controller_id_microbit_evt():
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_A_DOWN:
        basic.show_string("A")
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_A_UP:
        basic.clear_screen()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_B_DOWN:
        basic.show_string("B")
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_B_UP:
        basic.clear_screen()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_C_DOWN:
        basic.show_string("C")
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_C_UP:
        basic.clear_screen()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_D_DOWN:
        basic.show_string("D")
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_D_UP:
        basic.clear_screen()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_1_DOWN:
        basic.show_string("1")
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_1_UP:
        basic.clear_screen()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_2_DOWN:
        basic.show_string("2")
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_2_UP:
        basic.clear_screen()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_3_DOWN:
        basic.show_string("3")
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_3_UP:
        basic.clear_screen()
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_4_DOWN:
        basic.show_string("4")
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_4_UP:
        basic.clear_screen()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MICROBIT_EVT_ANY,
    on_mes_dpad_controller_id_microbit_evt)

bluetooth.on_bluetooth_connected(on_bluetooth_connected)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_forever():
    led.toggle(randint(0, 4), randint(0, 4))
    basic.pause(1000)
basic.forever(on_forever)
