import socket
from appJar import gui
import time
def press(button):
    if button == "Submit":
        address=(app.getEntry("IP->"))
        start=int(app.getEntry("da porta->"))
        stop=int(app.getEntry("ate porta->"))
        openport=[]
        def portscan(address,start,stop):
            
            for port in range(start, stop):
                try:
                    time.sleep(0.5)
                    ps=socket.socket()
                    ps.connect(("{}".format(address), port))
                    print("Port {} is OPEN".format(port))
                    openport.append(port)
                    ps.close()
                except socket.error:
                    print("error")
            return openport
        aport=portscan(address,start,stop)
        app.infoBox("Portas abertas","{}".format(aport))
        app.stop()
    else:
        app.stop()
    
app=gui("Port Scan GUI", "320x320")
app.setBg("black")
app.setFg("red")
app.setFont(14)
app.addLabelEntry("IP->")
app.addLabelEntry("da porta->")
app.addLabelEntry("ate porta->")
app.addLabel("Criador", text="by MrPowerUp",)
app.addButtons(["Submit", "Cancel"], press)
app.go()
