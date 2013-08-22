import easygui


versuche=0
while True :
    versuche=versuche+1
    if versuche>3:
        break
    antwort = easygui.buttonbox("Wie gehts?",":)",["Gut!", "Normal!", "Geht so!", "Schlecht!!", "Beenden"],image ="ghost.gif")
    if antwort == "Gut!":
        easygui.msgbox("Das freut mich!",image ="gryphon.gif")
    elif antwort == "Normal!":
        easygui.msgbox("Warum nur Normal?:)",image ="bat.gif")
    elif antwort == "Geht so!":
        easygui.msgbox("Warum geht so!?",image ="augur.gif")
    elif antwort == "Schlecht!!":
        easygui.msgbox("Schlecht? Warum beschwerst du dich dann bei mir?",image ="lich.gif")
    elif antwort == "Beenden":
        easygui.msgbox("BB",image ="ghost.gif")
        break
            






#C:\Users\Leonhard\AppData\Local\Battle for Wesnoth 1.11.5\data\core







