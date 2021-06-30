def sample_responses(input_text):
    user_message = str (input_text).lower ()
    if user_message in ("lib_start"):
        return """
               Welcome to The library bot, 
        Enter your Branch(Eg:if in First year , enter lib_FE)
        Type help for help regarding this bot
                """

    elif user_message in ("lib_FirstYear", "lib_fe", "lib_FE"):
        return """
                    This is your Google Drive Link 
                    Sem 1: https://drive.google.com/drive/folders/11hMqTwqzgHf5c6W7oLX-NM-7rSwXsuYj  
                    Sem 2 : https://drive.google.com/drive/u/0/folders/12-3kD6BYkgF74-JTDbbGBQ9MmoMVkKSm
                    """

    elif user_message in ("lib_Computer", "lib_computer", "lib_Comp"):
        return """This is your Google Drive Link 
                       Sem 3: https://drive.google.com/drive/u/0/folders/1oc-GsqGFiLpuz_5Y8MOelCc5A_Icsu8u  
                       Sem 4 : https://drive.google.com/drive/folders/1tEBwoWgCk3opIg6BI0uV3c9A1Z3CY56T
                       Sem 5 : https://drive.google.com/drive/u/0/folders/1SH8cP796K5DzuCwT9yGqYxaWLgAwhDZR
                       Sem 6 : https://drive.google.com/drive/folders/1NminRHV6bP4dTG1JeBZSDPNQBwGYfz5Z
                       Sem 7 : https://drive.google.com/folderview?id=1-6ecXe3M8LD6OGJw0bcxO4JGHFUhQUyV
                       Sem 8 : https://drive.google.com/drive/folders/1fGfRJPCA_kA1p_DWGUFvTk2gRY-0hNi8
                       """

    elif user_message in ("lib_EXTC", "lib_extc"):
        return """This is your Google Drive Link 
                               Sem 3 : https://drive.google.com/folderview?id=1-J-8W4fc3cgrGNptwRGxCFMcv8cXOHHa
                               Sem 4 : https://drive.google.com/folderview?id=125fed4ZSILRt93nKVaBtK-_yb9NqVxTx
                               Sem 5 : https://drive.google.com/drive/u/0/folders/1K66QKWqzgv8BW8IPbP4j28dUwNJU2iuu
                               Sem 6 : https://drive.google.com/folderview?id=1rsF6KKOnPJpDo6CqkSSzwZHQR2aQTEMN
                               Sem 7 : https://drive.google.com/drive/u/0/folders/181TFqGVN2ItAlicXg841LH1pVWvZ3PVA
                               Sem 8 : https://drive.google.com/folderview?id=1gfVs5kbEddtb4RxwfEivVpT8lEpEwgBm
                               """

    elif user_message in ("lib_Mechanical", "lib_mech"):
        return """This is your Google Drive Link 
                       Sem 3 : https://drive.google.com/drive/u/0/folders/1dXm0vZwOHqB3jWzcRiz_wqVFtMb0sS5A
                       Sem 4 : https://drive.google.com/drive/u/0/folders/1Dxz9ORu_S88BcuKyg01dr72Wn0Y_UNda
                       Sem 5 : https://drive.google.com/drive/folders/1zI2Ib9RWdz7yOmtvE-ZocCCPjGTXXyAM
                       Sem 6 : http://bit.ly/2LqjZce
                       Sem 7 : https://drive.google.com/drive/folders/1i0_d1x3nJ9HQpL5oLwit8fmSCh-9aYNl
                       Sem 8 : http://bit.ly/2Ky7ACm
                       """

    elif user_message in ("lib_Civil", "lib_civil"):
        return """This is your Google Drive Link 
                       Sem 3 : http://bit.ly/2XUVz06
                       Sem 4 : http://bit.ly/2OgHsxW
                       Sem 5 : https://drive.google.com/folderview?id=1jNQTFVlvu4gFC7f2015oApycoYOHEyg7
                       Sem 6 : http://bit.ly/2UbgGob
                       Sem 7 : http://bit.ly/2VU9sa9
                       Sem 8 : http://bit.ly/2UaJNYI
                       """

    elif user_message in ("lib_IT", "lib_civil"):
        return """This is your Google Drive Link 
                       Sem 3 : https://drive.google.com/drive/u/0/mobile/folders/1ya3Z2JCMmTqc9Y3LcqmQ-IAZCJV_-QDF?usp=sharing  
                       Sem 4 : http://bit.ly/2yNIC9I
                       Sem 5 : https://drive.google.com/drive/folders/1m--ICVEdzpUGkZpVkd_C9okIPS3bfCki?usp=sharing
                       Sem 6 : https://drive.google.com/drive/folders/1njkLCSd2dtImIU8O4w3u3kznUPRAm3Ry
                       Sem 7 : https://drive.google.com/drive/folders/1-zM72jHrx0tbEZfGSn_AEAl6QcpDIfsc
                       Sem 8 : https://drive.google.com/drive/folders/1YxSUsj7XOsAer1XWHrOjLO5wFA7yAulO
                       """

    elif user_message in "lib_help":
        return """Type the following words to do the following:
                  lib_start- starts the bot
                  lib_about- tells you about the bot
                  lib_support- Contact detail to give feedback
                  lib_add- Add librarybot to your group 
                  lib_exit- Exit librarybot 
                       """
    elif user_message in "lib_add":
        return """1.Click on the group where you want to add librarybot.
2.Tap on the group’s name, located at the top of the chat window.
3.Click on “Add members”, you can manually select the librarybot by searching the username = libraryinfo_bot.
4.Finally, tap the check icon to add the bot to your group.
5.It will show a notification, touch on “Add”.
And you are done."""

    elif user_message in "lib_about":
        return """This bot is made by Siddharth Shinde
                                       Sanket Salvi
                                       Shriyash Patil
                                       Kaushal Bhoir"""

    elif user_message in "lib_exit":
        return "Bye!"

    else:
        return "I don't understand you.Use 'lib_help' command to input the right commands"
