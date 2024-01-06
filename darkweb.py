import os
import subprocess

# Function to print with color
def print_with_color(line, color_code):
    print(f"\033[{color_code}m{line}\033[0m")

# Function to calculate the center position for the banner
def get_terminal_center(width):
    terminal_width = os.get_terminal_size().columns
    return (terminal_width - width) // 2

# Check if the network is reachable (placeholder function, implement as needed)
def is_network_reachable():
    return True  # Implement your network check logic here

# Clear the terminal
os.system('clear')

# Display the banner at the top of the terminal
banner = [
    "╭━━━╮╱╱╱╱╭╮╱╭╮╭╮╭╮╱╱╭╮",
    "╰╮╭╮┃╱╱╱╱┃┃╱┃┃┃┃┃╱╱┃┃",
    "╱┃┃┃┣━━┳━┫┃╭┫┃┃┃┃┣━━┫╰━╮",
    "╱┃┃┃┃╭╮┃╭┫╰╯┫╰╯╰╯┃┃━┫╭╮┃",
    "╭╯╰╯┃╭╮┃┃┃╭╮╋╮╭╮╭┫┃━┫╰╯┃",
    "╰━━━┻╯╰┻╯╰╯╰╯╰╯╰╯╰━━┻━━╯"
]

color_codes = ["38;5;196", "38;5;105"]

# Print the banner at the top of the terminal
for line in banner:
    padding = get_terminal_center(len(line))
    print_with_color(" " * padding + line, color_codes[banner.index(line) % len(color_codes)])

author_info = [
    "Author: Md. Arman Hussen",
    "GitHub: TeamBlackBerry",
    "Telegram: @TeamBlackBerry"
]

# Print author information
for line in author_info:
    padding = get_terminal_center(len(line))
    print_with_color(" " * padding + line, "38;5;105")

# Check if the network is reachable
if not is_network_reachable():
    print_with_color("\nTurn on your data or Wi-Fi to proceed.", "38;5;196")
    exit()

def start_installation():
    print("\033[38;5;40m1. Start Installation:\033[0m")

    # Change directory to /etc and remove resolv.conf
    subprocess.run(['cd', '/etc'], check=True)
    subprocess.run(['rm', 'resolv.conf'], check=True)

    # Change directory to /root/tbbDarkWebmake and move resolv.conf back to /etc
    subprocess.run(['cd', '/root/tbbDarkWebmake'], check=True)
    subprocess.run(['mv', 'resolv.conf', '/etc'], check=True)

    # Update, upgrade, and install required packages
    subprocess.run(['apt', 'update'], check=True)
    subprocess.run(['apt', 'upgrade', '-y'], check=True)
    subprocess.run(['apt', 'install', 'wget', 'tor', 'apache2', '-y'], check=True)

    # Change directory to /etc/apache2 and replace apache2.conf and ports.conf
    subprocess.run(['cd', '/etc/apache2'], check=True)
    subprocess.run(['rm', 'apache2.conf', 'ports.conf'], check=True)
    subprocess.run(['cd', '/root/tbbDarkWebmake'], check=True)
    subprocess.run(['mv', 'apache2.conf', 'ports.conf', '/etc/apache2'], check=True)

    # Change directory to /etc/tor and replace torrc
    subprocess.run(['cd', '/etc/tor'], check=True)
    subprocess.run(['rm', 'torrc'], check=True)
    subprocess.run(['cd', '/root/tbbDarkWebmake'], check=True)
    subprocess.run(['mv', 'torrc', '/etc/tor'], check=True)

    completion_message = "Installation Complete. Now You Can Run It."
    center_position_completion = get_terminal_center(len(completion_message))
    print("\n" * center_position_completion)
    print_with_color(completion_message, "38;5;40")
    print("\n" * center_position_completion)

def start_darkweb():
    print("\033[38;5;40m2. Start DarkWeb:\033[0m")
    subprocess.run(['service', 'tor', 'start'])
    subprocess.run(['service', 'apache2', 'restart'])

    darkweb_message = "DarkWeb Started Successfully."
    center_position_darkweb = get_terminal_center(len(darkweb_message))
    print("\n" * center_position_darkweb)
    print_with_color(darkweb_message, "38;5;40")
    print("\n" * center_position_darkweb)

def customize_html_code():
    print("\033[38;5;40m3. Customize HTML Code:\033[0m")
    # Implement your logic for customizing HTML code
    html_code = input("Enter your customized HTML code: ")
    # Save or process the customized HTML code as needed

    customization_message = "HTML Code Customized Successfully."
    center_position_customization = get_terminal_center(len(customization_message))
    print("\n" * center_position_customization)
    print_with_color(customization_message, "38;5;40")
    print("\n" * center_position_customization)

def main():
    print("Enter your choice:")
    print("1. For Installation")
    print("2. For Start DarkWeb")
    print("3. Customize HTML Code")
    
    option = input()

    if option == '1':
        start_installation()
    elif option == '2':
        start_darkweb()
    elif option == '3':
        customize_html_code()
    else:
        print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
