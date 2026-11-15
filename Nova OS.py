import os
import time
import platform
import socket
import datetime
import getpass
import webbrowser
import subprocess
import shutil

# ===== WARNA =====
R = "\033[0m"
G = "\033[92m"
C = "\033[96m"
Y = "\033[93m"
B = "\033[94m"
P = "\033[95m"
W = "\033[97m"
O = "\033[38;5;208m"

NAME = "NovaOS"
VER = "3.1"

try:
    USER = getpass.getuser()
except:
    USER = "nova"

try:
    HOST = socket.gethostname()
except:
    HOST = "computer"

history = []


# ============================================================
# CLEAR
# ============================================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ============================================================
# BOOT
# ============================================================

def bar(text):
    print(C + text + R)

    for i in range(21):
        print(
            "\r" + B + "[" +
            G + "#" * i +
            W + "-" * (20 - i) +
            B + "] " +
            str(i * 5) + "%" + R,
            end="",
            flush=True
        )
        time.sleep(0.03)

    print()


def ok(text):
    print(G + "[ OK ] " + R + text)
    time.sleep(0.08)


def boot():
    clear()

    print(O + "================================" + R)
    print(O + "          N O V A O S           " + R)
    print(O + "        TERMINAL EDITION        " + R)
    print(O + "================================" + R)
    print()

    ok("Bootloader started")
    ok("Loading kernel")
    bar("Kernel modules")
    ok("Kernel loaded")

    print()
    ok("CPU manager")
    ok("Memory manager")
    ok("Process manager")
    bar("Initializing memory")

    print()
    ok("Filesystem")
    ok("Storage manager")
    ok("Device manager")
    bar("Mounting filesystem")

    print()
    ok("Network service")
    ok("Security service")
    ok("User service")
    ok("System logger")
    ok("Background service")

    print()
    ok("Browser service")
    ok("Google service")
    ok("Web launcher")

    print()
    bar("Starting NovaShell")
    ok("Command parser")
    ok("Terminal renderer")
    ok("Shell environment")

    print()
    print(G + "[ PASS ] Kernel" + R)
    print(G + "[ PASS ] Memory" + R)
    print(G + "[ PASS ] Filesystem" + R)
    print(G + "[ PASS ] Devices" + R)
    print(G + "[ PASS ] Network" + R)
    print(G + "[ PASS ] Browser" + R)
    print(G + "[ PASS ] Google" + R)
    print(G + "[ PASS ] Services" + R)
    print(G + "[ PASS ] NovaShell" + R)

    print()
    print(G + "NovaOS boot completed successfully!" + R)

    time.sleep(1)
    clear()


# ============================================================
# BANNER
# ============================================================

def banner():
    print(O + "╔══════════════════════════════╗" + R)
    print(O + "║" + W + "          NOVAOS 3.1         " + O + "║" + R)
    print(O + "╚══════════════════════════════╝" + R)

    print(C + "Ketik 'help' untuk bantuan." + R)
    print()


# ============================================================
# PROMPT
# ============================================================

def prompt():
    return (
        G + USER + R +
        "@" +
        C + HOST + R +
        ":~$ "
    )


# ============================================================
# BROWSER
# ============================================================

def open_browser(url):
    try:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        print()
        print(
            C +
            "NovaBrowser membuka: " +
            R +
            W +
            url +
            R
        )

        time.sleep(0.5)

        # Android / Termux
        if shutil.which("termux-open-url"):
            result = subprocess.run(
                ["termux-open-url", url],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            if result.returncode == 0:
                print(G + "[ OK ] Browser Android dibuka." + R)
                return

        # Android menggunakan Activity Manager
        if shutil.which("am"):
            result = subprocess.run(
                [
                    "am",
                    "start",
                    "-a",
                    "android.intent.action.VIEW",
                    "-d",
                    url
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            if result.returncode == 0:
                print(G + "[ OK ] Browser Android dibuka." + R)
                return

        # Windows / Linux / macOS
        result = webbrowser.open_new_tab(url)

        if result:
            print(G + "[ OK ] Browser berhasil dibuka." + R)
        else:
            print(Y + "[ INFO ] Browser tidak dapat dibuka." + R)

    except Exception as e:
        print(Y + "[ ERROR ] " + R + str(e))

    print()


def google():
    open_browser("https://www.google.com")


def youtube():
    open_browser("https://www.youtube.com")


def github():
    open_browser("https://github.com")


# ============================================================
# HELP
# ============================================================

def help_cmd():
    print()
    print(C + "╔════════════════════════════════════╗" + R)
    print(C + "║          PERINTAH NOVAOS           ║" + R)
    print(C + "╚════════════════════════════════════╝" + R)
    print()

    commands = [
        ("help", "bantuan"),
        ("clear", "bersihkan layar"),
        ("date", "tanggal"),
        ("time", "waktu"),
        ("whoami", "user"),
        ("hostname", "nama komputer"),
        ("uname", "informasi sistem"),
        ("neofetch", "info NovaOS"),
        ("ls", "lihat file"),
        ("pwd", "folder sekarang"),
        ("cd", "pindah folder"),
        ("mkdir", "buat folder"),
        ("touch", "buat file"),
        ("echo", "tampilkan teks"),
        ("calc", "kalkulator"),
        ("history", "riwayat command"),
        ("browser", "buka alamat website"),
        ("google", "buka Google"),
        ("youtube", "buka YouTube"),
        ("github", "buka GitHub"),
        ("about", "tentang NovaOS"),
        ("reboot", "restart NovaOS"),
        ("shutdown", "matikan NovaOS"),
        ("exit", "keluar")
    ]

    for command, description in commands:
        print(
            G +
            command.ljust(12) +
            R +
            "- " +
            W +
            description +
            R
        )

    print()


# ============================================================
# NEOFETCH
# ============================================================

def neofetch():
    print()

    print(P + "      _   _  ___  _   _  " + R)
    print(P + "     | \\ | |/ _ \\| | | | " + R)
    print(P + "     |  \\| | | | | | | | " + R)
    print(P + "     | |\\  | |_| | |_| | " + R)
    print(P + "     |_| \\_|\\___/ \\___/  " + R)

    print()

    print(C + "OS       : " + R + NAME + " " + VER)
    print(C + "Shell    : " + R + "NovaShell")
    print(C + "User     : " + R + USER)
    print(C + "Host     : " + R + HOST)
    print(C + "Python   : " + R + platform.python_version())
    print(C + "System   : " + R + platform.system())
    print(C + "Machine  : " + R + platform.machine())

    print()


# ============================================================
# MAIN
# ============================================================

def main():
    boot()
    banner()

    while True:

        try:
            cmd = input(prompt()).strip()

            if cmd == "":
                continue

            history.append(cmd)

            # HELP
            if cmd == "help":
                help_cmd()

            # CLEAR
            elif cmd == "clear":
                clear()
                banner()

            # DATE
            elif cmd == "date":
                print(
                    G +
                    datetime.datetime.now().strftime(
                        "%d-%m-%Y"
                    ) +
                    R
                )

            # TIME
            elif cmd == "time":
                print(
                    C +
                    datetime.datetime.now().strftime(
                        "%H:%M:%S"
                    ) +
                    R
                )

            # WHOAMI
            elif cmd == "whoami":
                print(G + USER + R)

            # HOSTNAME
            elif cmd == "hostname":
                print(C + HOST + R)

            # UNAME
            elif cmd == "uname":
                print(
                    W +
                    NAME +
                    " " +
                    VER +
                    " " +
                    platform.system() +
                    " " +
                    platform.machine() +
                    R
                )

            # NEOFETCH
            elif cmd == "neofetch":
                neofetch()

            # LS
            elif cmd == "ls":

                try:
                    items = os.listdir()

                    if not items:
                        print(Y + "Folder kosong." + R)

                    for x in items:
                        if os.path.isdir(x):
                            print(
                                B +
                                "[DIR ] " +
                                R +
                                x
                            )
                        else:
                            print(
                                W +
                                "[FILE] " +
                                R +
                                x
                            )

                except Exception as e:
                    print(Y + str(e) + R)

            # PWD
            elif cmd == "pwd":
                print(
                    C +
                    os.getcwd() +
                    R
                )

            # CD
            elif cmd.startswith("cd "):

                folder = cmd[3:].strip()

                try:
                    os.chdir(
                        os.path.expanduser(folder)
                    )

                    print(
                        G +
                        "Folder: " +
                        R +
                        os.getcwd()
                    )

                except Exception:
                    print(
                        Y +
                        "Folder tidak ditemukan." +
                        R
                    )

            # MKDIR
            elif cmd.startswith("mkdir "):

                folder = cmd[6:].strip()

                try:
                    os.mkdir(folder)

                    print(
                        G +
                        "Folder berhasil dibuat." +
                        R
                    )

                except Exception as e:
                    print(
                        Y +
                        str(e) +
                        R
                    )

            # TOUCH
            elif cmd.startswith("touch "):

                filename = cmd[6:].strip()

                try:
                    open(
                        filename,
                        "a"
                    ).close()

                    print(
                        G +
                        "File berhasil dibuat." +
                        R
                    )

                except Exception as e:
                    print(
                        Y +
                        str(e) +
                        R
                    )

            # ECHO
            elif cmd.startswith("echo "):

                print(
                    C +
                    cmd[5:] +
                    R
                )

            # CALC
            elif cmd.startswith("calc "):

                try:

                    exp = cmd[5:]

                    allowed = (
                        "0123456789"
                        "+-*/(). "
                    )

                    if all(
                        x in allowed
                        for x in exp
                    ):
                        result = eval(
                            exp,
                            {
                                "__builtins__": {}
                            },
                            {}
                        )

                        print(
                            G +
                            str(result) +
                            R
                        )

                    else:
                        print(
                            Y +
                            "Ekspresi tidak valid." +
                            R
                        )

                except Exception:
                    print(
                        Y +
                        "Perhitungan gagal." +
                        R
                    )

            # HISTORY
            elif cmd == "history":

                if len(history) == 0:
                    print(
                        Y +
                        "Belum ada history." +
                        R
                    )

                for i, x in enumerate(
                    history,
                    1
                ):
                    print(
                        Y +
                        str(i) +
                        "  " +
                        R +
                        x
                    )

            # BROWSER
            elif cmd.startswith("browser "):

                url = cmd[8:].strip()

                if url:
                    open_browser(url)
                else:
                    print(
                        Y +
                        "Contoh: browser google.com" +
                        R
                    )

            # GOOGLE
            elif cmd == "google":
                google()

            # YOUTUBE
            elif cmd == "youtube":
                youtube()

            # GITHUB
            elif cmd == "github":
                github()

            # ABOUT
            elif cmd == "about":

                print()
                print(
                    O +
                    "NovaOS " +
                    VER +
                    R
                )

                print(
                    W +
                    "Terminal Operating System Simulation" +
                    R
                )

                print(
                    C +
                    "Powered by Python" +
                    R
                )

                print(
                    P +
                    "NovaBrowser + Google Support" +
                    R
                )

                print()

            # REBOOT
            elif cmd == "reboot":

                print(
                    Y +
                    "Restarting NovaOS..." +
                    R
                )

                time.sleep(0.5)

                boot()
                banner()

            # SHUTDOWN
            elif (
                cmd == "shutdown" or
                cmd == "exit"
            ):

                clear()

                print(
                    Y +
                    "Shutting down NovaOS..." +
                    R
                )

                time.sleep(1)

                print(
                    G +
                    "NovaOS stopped." +
                    R
                )

                break

            # UNKNOWN
            else:

                print(
                    Y +
                    "Command tidak ditemukan: " +
                    R +
                    cmd
                )

                print(
                    C +
                    "Ketik 'help' untuk bantuan." +
                    R
                )

        except KeyboardInterrupt:

            print()
            print(
                Y +
                "Gunakan 'exit' untuk keluar." +
                R
            )

        except EOFError:

            print()
            print(
                Y +
                "Input dihentikan." +
                R
            )

            break

        except Exception as e:

            print(
                Y +
                "Error: " +
                R +
                str(e)
            )


# ============================================================
# START NOVAOS
# ============================================================

if __name__ == "__main__":
    main()