try: # Add error handling

        # Importing pyttsx3 module for text to speech conversion 
        import pyttsx3

        # Initializing the pyttsx3 engine
        engine = pyttsx3.init()

        # Getting to current property
        volume=engine.getProperty('volume')
        voice=engine.getProperty('voice')
        rate=engine.getProperty('rate')

        # Printing the welcome massage and volume on console and speak it out
        print("""\t\t\t\t**Welcome to Robo speaker**
                \t\t\t* To exit write 'Q' on prompt*
                \t\t\t* To set voice write '@voice' on prompt*
                \t\t\t* To set volume write '@vol' on prompt*
                \t\t\t* To set rate write '@rate' on prompt*""")
        engine.say("welcome to Robo speaker")
        print(f"volume level -> {volume}\n")
        engine.say(f"volume level -> {volume}")
        print(f"voice rate -> {rate}\n")
        engine.say(f"voice rate -> {rate}")
        engine.runAndWait()
        engine.stop()

        # Create a function to set the voice rate
        def Rate():
                user_volume_rate=int(input("setting voice rate : "))
                engine.setProperty('rate',user_volume_rate)
                engine.say(f"volume rate {user_volume_rate}")
                engine.runAndWait()
                print(f"voice rate -> {user_volume_rate}")

        # Create a function to set the voice 
        def Voice():
                user_voice=int(input("setting voice ( 0 for male and 1 for female ) : "))
                engine.setProperty('voice',voice[user_voice])
                engine.say(f"voice is {user_voice}")
                engine.runAndWait()
                print(f"voice is -> {user_voice}")

        # Create a function to set the volume
        def vol():
                user_volume=float(input("setting volume level between 0 and 1 : "))
                engine.setProperty('volume',user_volume)
                engine.say(f"volume level {user_volume}")
                engine.runAndWait()
                print(f"volume level -> {user_volume}")

        # Set a boolean flag to True for while loop
        s=True

        # Prompt user to enter input
        engine.say("Enter what you want to say")
        engine.runAndWait()
        engine.stop()

        # Start the while loop to get user input and speak it out
        while s:
               x=input("Enter what you want to say : ")

               # Speak out the user input
               engine.say(x)
               engine.runAndWait()

               # Call vol() function if user enter '@vol'
               if(x=='@vol'):
                vol() # Calling vol() function

               # Call Rate() function if user enter '@vol'
               if(x=='@rate'):
                Rate() # Calling Rate() function

               # Call Voice() function if user enter '@vol'
               if(x=='@voice'):
                Voice()# Calling Voice() function

               # Break the loop if user enters 'Q'
               if(x=="Q"):
                q=str(input("Do you want to exit?(Y/N) : "))
                if q in ('y', 'Y'):
                     engine.stop()
                     break
                else:
                     pass

except Exception as e:
   print(f"Some error occurred : {e}")