#References:
# http://docs.paramiko.org/en/stable/
# https://www.devdungeon.com/content/python-ssh-tutorial - Building up the connection
# https://www.raspberrypi.org/blog/pi-hole-raspberry-pi/#:~:text=Instead%20of%20installing%20adblockers%20on,games%20and%20on%20smart%20TVs. - Pihole install

import paramiko

# Establish SSH connection to host
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="raspberrypi", username="pi", password="") #enter password for pi

# Enters command to check status of remote pi-hole server and provides output
commands = "pihole status"
stdin, stdout, stderr = ssh.exec_command(commands)
lines = stdout.readlines()

#Checks if Pi-hole blocking is enabled
if lines[7] == "  [✓] Pi-hole blocking is enabled\n": # Replace lines[7] with lines[6] if you do not have the "Hello world" as first item in lines
    print("Pihole is up")
else:
    print("Pihole is down")
    print("Attempting to re-enable Pihole")
    stdin, stdout, stderr = ssh.exec_command("pihole enable")
    lines = stdout.readlines()
    if lines[2] == "\r\x1b[K  [✓] Pi-hole Enabled\n":
        print("Pihole is up")
    else:
        print("Attempt to re-enable Pihole failed. Please check to see if the device is running.")



#Closes out SSHClient
ssh.close()