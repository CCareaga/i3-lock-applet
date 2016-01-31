from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify
import signal
import os
import subprocess

APPINDICATOR_ID = 'TestApp'
icon_path = os.path.dirname(os.path.realpath(__file__)) + "/icons"

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    notify.init(APPINDICATOR_ID)
    print icon_path
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, icon_path+"/icon.png", appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    img = gtk.Image()
    img2 = gtk.Image()
    img3 = gtk.Image()

    lock_item = gtk.ImageMenuItem('Lock')
    img.set_from_file(icon_path + "/lock.png")
    lock_item.set_image(img)
    lock_item.connect('activate', lock)

    exit_item = gtk.ImageMenuItem('Exit-i3')
    img2.set_from_file(icon_path + "/exit.png")
    exit_item.set_image(img2)
    exit_item.connect('activate', exit)

    restart_item = gtk.ImageMenuItem('Restart')
    img3.set_from_file(icon_path + "/restart.png")
    restart_item.set_image(img3)
    restart_item.connect('activate', restart)
    
    menu.append(lock_item)
    menu.append(exit_item)
    menu.append(restart_item)
     
    menu.show_all()
    return menu

def lock(source):
    screenshot = 'scrot ' + icon_path + "/scrot.png"
    os.system(screenshot)
    lock_command = 'i3lock -i ' + icon_path + "/scrot.png"
    os.system(lock_command)

def exit(source):
    os.system('i3-msg exit')

def restart(source):
    os.system('reboot')

if __name__ == "__main__":
    main()