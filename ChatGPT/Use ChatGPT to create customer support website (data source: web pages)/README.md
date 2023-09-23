Building an AI that can answer questions about any website using a large language model called GPT-3.5 Turbo, provided by OpenAI.

The main steps in my program are :-
  1. Web Scrapping & Data Collection : Crawled website (openAI) to gather information
  2. Text Processing & Tokenization: Breakdown the text into token (smaller chunks)
  3. Embdedding Index: Analyzed the text and generated numerical vectors
  4. Question Answering: The GPT-3.5 Turbo model processes the embeddings and context of both the question and the available text to    find relevant parts which helps in generating appropriate answer

Applications:-
1. Command Line Interface:-\
    a. User interacts with the program by inputting questions through the terminal.\
    b. Program processes the questions and finds relevant information from data collected, and try to generate appropriate answer.\
    c. The answer is displayed on the terminal for the user to see.
     
2. Web Based User Interface:-\
a. Web Framework (Flask):\
    Flask is used as a web framework to create a web application.\
 b. HTML Templates:\
    HTML templates are used to create the user interface (webpage) where users can input their questions.\
 c. Question Submission:\
    Users input their questions through the web interface (a form on the webpage).\
 d. Answer Display:\
    The answer is then displayed on the webpage, allowing the user to view it.
