from scripts.display import Display

display = Display()

display.updateLine(0,0,"123456789")

display.removeLastLine()
display.removeLastLine()
display.refresh()