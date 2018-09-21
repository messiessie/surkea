label 01_C:
    scene TESTSCENE with Dissolve(2.5)
    #oni awakens, the rest of the girls are nearby
    #it's almost lunch, and oni has "taken a nap" after "falling yesterday"
    #the girls chat about lunch and what foods they like most
    #kura brings up that the weather is a little weird recently. Kokoro mentions that it'll be fine, probably. Utagu is nervous because she doesn't have an umbrella. 
    #
    #fade from black to closeup of Oni's eyes
    kura "Oh! You're awake!"
    utagu "Are you alright? You were out for a while there."
    kokoro "She must have been knocked out from that breakfast you made, Kura."
    #eye slowly open
    #fade from Oni to classroom with Kura, Kokoro and Utagu all present  
    kokoro "I WARNED you, Oni is too sensitive to any sort of spice. She couldn't even handle black pepper if she tried to!"
    kura "First off, how dare you. Second, she could barely handle white bread if I made her a toast."
    utagu "…I think that's just gluten intolerance."
    "As we chatter along, Oni sits up slowly, idly rubbing the sleep from her eye."
    "She looks at me first, and lets her eyes wander around the classroom."
    utagu "How are you feeling?"
    oni "I'm fine, thank you. Are you done talking smack about me?"
    "She slowly levers herself to her feet with a nearby chair."
    "Kokoro and Utago go to sit by their desks in the center of the classroom as I help Oni up and grab her chair.
    kura "Are you sure you're okay?"
    kokoro "She's fine, she only took a well earned nap, right?"
    "Utagu and Kokoro chatter as Oni sits down in the chair I brought along. I join in and take a seat as well."
    "Our four desks are pushed together in the center of the barren room."
    "Across from me is Utagu, who nervously flicks her eyes to the clock above the blackboard."
    "Anytime she catches me looking at her I feel like I've caught a very sad, lost puppy. She can be too worried for her own good sometimes, but I know she cares about us."
    "To my right Kokoro lounges, idly fiddling with her hair as she waits for our lunch break to arrive."
    "While she prefers to eat my food rather than make any of her own, she does like to help me out in the kitchen. She just loves to snag a bite or few, I guess."
    "Speaking of food…"
    kura "It's almost lunch, Oni. I promise I won't poison you this time."
    oni "Good thing I didn't miss this one, then."
    "Oni smiles. Her lack of facial expressions can be a little off putting sometimes, but I know she just has a naturally stoic face."
    "She's very relaxing to be with, so I'm glad she's part of our little group." 
    "We sit and waste some time before I decide it's time to go cook."
    "Utagu and Oni sit and chat while Kokoro and I go to prepare for lunch."
    #school bell ringing
    "The school bell rings out to let us know that our lesson is over."
    "Utagu breathes a sigh of relief."
    kura "What's up, Utagu?"
    utagu "Oh, nothing. The homework we got is a bit much."
    kokoro "This assignment is a pain in the butt."
    "…I'm not sure it's the assignment that's making her this gloomy."
    utagu "Just feeling weird today, I guess."
    kura "Maybe it's the weather? It looked like it was going to rain this morning."
    kokoro "Sorry girls, I checked the forecast and they said it'd be sunny all day. We should be fine, look!"
    "Kokoro smiles widely as she points to the window."
    utagu "I hope so. I didn't bring an umbrella today."
    "Utagu sighs again."
    "She opens her eyes a bit more when she spots the bento box I just placed in front of her."
    kokoro "We made your favorite today!"
    kura "I made. You tried to snag most of it while I was cooking."
    utagu "Oh, did you make karaage?"
    kura "And YOU, Kokoro, will have this one."
    "She gladly opens the box I just handed to her."
    kokoro "Oooh! Rice balls are my favorite!"
    "We all sit together like earlier this morning. I hand over a bento box to Oni.
    utagu "How do you even have time to cook lunch in school?"
    oni "You know how it is here, classes are short enough because it's summer. We have so much time to waste here it's almost like we actually ARE on our break."
    "Kokoro leans over her table towards me, her face beaming a smile."
    kura "What about you, Oni?"
    oni "What about what?"
    kura "Lunch, dummy! What do you think is in there?"
    "She ponders for a bit.
    oni "Hmm. With the size and weight of this box I'll say…"
    "I stare at her in anticipation as she hovers the box up and down gently with her hands."
    oni "Vegetable tempura with rice and salmon?"
    kura "Oh, you're good. Or I'm becoming too predictable."
    oni "You just know what I love."
    "We all dig in and chat about various topics."
    "Time seems to fly by us in seconds, because as soon as we finished our lunch, afternoon class begins."
    #school bell ringing
    "We all stretch our arms as the school bell rings."
    kokoro "Haaaaaah, finally the day is over."
    "I watch her jump out of her chair as I put away my books."
    kokoro "Time for the GOOD stuff to begin!"
    oni "What, reading your gossip magazines and talk about cute girls?"
    kokoro "No, stupid! That's for tomorrow! Todaaaay I plan on finding what cookbooks they have hidden around in school."
    kura "So you can tell me what to cook for you?"
    kokoro "That too, but I actually want to try and find this old recipe my mom used to make for me when I was a kid. I don't remember much of it except that it was very gooey and sweet, almost like mochi."
    kura "What about you two?"
    "Utagu reacts and looks at me. Oni stares out the window, so I focus on Utagu."
    utagu "I uh… I was thinking about going to the library. I wanted to read more about some things for the homework we have."
    "Schoolwork or not, I think she just want to spend some time alone with her books."
    "Oni is still looking outside. I'm unsure how to read her expression."
    kura "You going home for the day, Oni?"
    "She looks at me."
    oni "I'll go to the principal's office before I head home. You girls have fun today."
    "She stands up abruptly and leaves the classroom."
    oni "See you tomorrow."
    "Everyone tells her goodbye and then goes their own way."
    "I'm left standing alone in the classroom. I have absolutely no idea what to do for the rest of the day."
    "I could help Kokoro out, or go to the library and sit and read something with Utagu."
    "Hmmm…"
    
    menu:
     "Who should I spend time with this afternoon?"

    #this option shouldn't be unlocked until you have played Kokoro and Utagu's routes
     "Try and find Oni.":
         jump oniroute 

     "Follow Kokoro to the kitchen.":
         jump kokororoute

     "Meet Utagu at the library.":
         jump utaguroute

label oniroute:
    #ONIROUTE
    call 02_O from _call_02_O
return

label kokororoute:
    #KOKOROROUTE
    call 02_K from _call_02_K
return

label utagiroute:
    #UTAGUROUTE
    call 02_U from _call_02_U
return


