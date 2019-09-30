import subprocess


#BOOT_PATH = '/boot/config.txt'
BOOT_PATH = 'tmp/config.txt'

# 0 is the normal configuration. 1 is 90 degrees. 2 is 180 degress. 3 is 270 degrees.
def rotate_screen(screen_rotation: str):
    print(f"Rotating screen {screen_rotation} angles")   
    display_rotate = int(int(screen_rotation)/90)
    display_rotate_str = f"display_rotate={display_rotate}\navoid_warnings=1"
    print (f"Saving to file: {BOOT_PATH}  -> {display_rotate_str}")
    with open(BOOT_PATH, "a") as boot_config:
        boot_config.write(f"\n{display_rotate_str}\n")


def restart_raspberry():
    print("Restarting raspberry pi!")
    subprocess.call(["sudo","reboot"])