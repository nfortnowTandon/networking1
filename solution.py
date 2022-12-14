### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #The student doesn't have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "mtls"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA1 hashing value to the following message: 'NYU Computer Networking' - Use SHA1 hash generator and use the answer in your code":
        answer = "8496abe9fceb5aa927e28bfbd9a2347d1290ef9b"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 4 #transport/host-to-host
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 2 #internet layer
    else:
        answer = "that's not a question we were prepared for :)"
    print(question)
    return(answer)
# Complete all the questions.


# noinspection PyUnreachableCode
debug_questions = ["In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?",
                   "Are encoding and encryption the same? - Yes/No","Is it possible to decrypt a message without a key? - Yes/No",
                   "Is it possible to decode a message without a key? - Yes/No",
                   "Is a hashed message supposed to be un-hashed? - Yes/No",
                   "What is the SHA1 hashing value to the following message: 'NYU Computer Networking' - Use SHA1 hash generator and use the answer in your code",
                   "Is MD5 a secured hashing algorithm? - Yes/No",
                   "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number",
                   "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"]
for q in debug_questions:
    print(welcome_assignment_answers(q))
