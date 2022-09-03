control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MICROBIT_EVT_ANY, function on_mes_dpad_controller_id_microbit_evt() {
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_A_DOWN) {
        basic.showString("A")
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_A_UP) {
        basic.clearScreen()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_B_DOWN) {
        basic.showString("B")
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_B_UP) {
        basic.clearScreen()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_C_DOWN) {
        basic.showString("C")
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_C_UP) {
        basic.clearScreen()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_D_DOWN) {
        basic.showString("D")
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_D_UP) {
        basic.clearScreen()
    }
    
})
basic.forever(function on_forever() {
    led.toggle(randint(0, 4), randint(0, 4))
    basic.pause(1000)
})
