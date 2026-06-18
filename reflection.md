# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started? 

- What did the game look like the first time you ran it? 
The first time I ran the game, everything looked like it worked normally. The side bar listed the difficulty of the game which seemed normal. However, on the right side, I was allowed to enter numbers that were greater than 100. Maybe an out of bounds feature could be added to stop the guessing? I did like how the investigator was able to catch if I inputted words instead of numbers.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards"). 
  One bug I noticed at the start was that changing the difficulty reset the nu Another bug that I noticed was the range was incorrect. For example, I would enter 1 and the invesigator would inquire that I go lower.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
100      "Too High          "Too Low"         "Go Higher"
New Game restart game       did not restart   "Game over. Start a new game to try again."
Attempts consistant attempts attemps did not match "None"

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
The AI tools I used on this project was Copilot. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggestion that was correct was converting the secret from a string into an int to ensure lexicograpical operations would not hinder integer comparisons. I verified the result by inputting 100 and verifying that the hint outputted "Go Lower".
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
An AI suggesstion that was misleading was refactoring check_guess to logic_utils. This is because the generated code did not include the repo root in order to run pytest anywhere. In order to run the pytest, I had use the command line to naviagte to the directory to run the pytest which I was not aware of before. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I knew that a bug was really fixed when I testing multiple numbers during the investigation and everything worked correctly. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One manual test I ran was checking if the bounds for the investigation were correct. For example, if the secret number was not 1, "Go Higher" should always display. 
- Did AI help you design or understand any tests? How?
The AI helped design a boundary test to ensure the investigator was diplaying the correct behavior. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would explain "reruns" as a method that restarts the code from the top. I would explain session state as the active state a user is in. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  From this project, I learned when testing a new block of code that has been generated to check even features that were not related to the specific problem to catch potential errors. For example, when the attempt counter was fixed, the "Show Hint" display did not work. Being thorough when testing prevents future issues. 
- What is one thing you would do differently next time you work with AI on a coding task?
One thing I would do differently when working with AI on a coding task would be to try and address multiple small issues in one coding block so I don't run out of credits.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
After completing this project, I know to thorough check behind the AI to ensure the code really works. Not blindly accepting fixes prevents getting lost in the fixes if something breaks.
