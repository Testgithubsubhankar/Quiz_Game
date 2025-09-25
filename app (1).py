import streamlit as st
import random

# Define the quiz questions, options, and correct answers
quiz_data = [
    {
        "question": "What is the capital city of India?",
        "options": ["A) Mumbai", "B) Delhi", "C) Kolkata", "D) Chennai"],
        "correct_answer": "B",
        "explanation": "Delhi is the capital city of India, serving as the political and administrative center."
    },
    {
        "question": "Which river is considered the holiest in India?",
        "options": ["A) Yamuna", "B) Ganges", "C) Brahmaputra", "D) Godavari"],
        "correct_answer": "B",
        "explanation": "The Ganges is considered the holiest river in India, revered in Hinduism."
    },
    {
        "question": "The Taj Mahal is located in which city?",
        "options": ["A) Jaipur", "B) Agra", "C) Varanasi", "D) Lucknow"],
        "correct_answer": "B",
        "explanation": "The Taj Mahal, a UNESCO World Heritage Site, is located in Agra, Uttar Pradesh."
    },
    {
        "question": "India is the largest producer of which spice?",
        "options": ["A) Saffron", "B) Turmeric", "C) Black Pepper", "D) Cardamom"],
        "correct_answer": "B",
        "explanation": "India is the largest producer of turmeric, widely used in cooking and traditional medicine."
    },
    {
        "question": "Is Hindi the only official language of India?",
        "options": ["A) True", "B) False"],
        "correct_answer": "B",
        "explanation": "India has 22 official languages, including Hindi, Tamil, Bengali, and others."
    }
]

def run_quiz():
    st.title("India Quiz Game")
    st.write("Test your knowledge about India! Answer the questions below and see your score.")

    # Initialize session state for score, question index, and answers
    if 'score' not in st.session_state:
        st.session_state.score = 0
        st.session_state.current_question = 0
        st.session_state.answered = False
        st.session_state.user_answer = None
        st.session_state.quiz_completed = False
        st.session_state.shuffled_questions = random.sample(quiz_data, len(quiz_data))

    # Check if quiz is completed
    if st.session_state.current_question < len(st.session_state.shuffled_questions) and not st.session_state.quiz_completed:
        question_data = st.session_state.shuffled_questions[st.session_state.current_question]
        st.subheader(f"Question {st.session_state.current_question + 1}: {question_data['question']}")
        
        # Display options as radio buttons
        user_answer = st.radio("Choose your answer:", question_data['options'], key=f"q{st.session_state.current_question}")
        
        # Submit button
        if st.button("Submit Answer"):
            st.session_state.answered = True
            st.session_state.user_answer = user_answer[0]  # Get the letter (A, B, etc.)
            
            # Check if answer is correct
            if st.session_state.user_answer == question_data['correct_answer']:
                st.session_state.score += 1
                st.success("Correct! " + question_data['explanation'])
            else:
                st.error(f"Incorrect! The correct answer is {question_data['correct_answer']}. " + question_data['explanation'])
            
            # Move to next question
            st.session_state.current_question += 1
            st.session_state.answered = False
            st.session_state.user_answer = None
            
            # Check if quiz is complete
            if st.session_state.current_question >= len(st.session_state.shuffled_questions):
                st.session_state.quiz_completed = True

    # Display final score when quiz is complete
    if st.session_state.quiz_completed:
        st.subheader("Quiz Completed!")
        st.write(f"Your final score: {st.session_state.score}/{len(st.session_state.shuffled_questions)}")
        percentage = (st.session_state.score / len(st.session_state.shuffled_questions)) * 100
        st.write(f"Percentage: {percentage:.2f}%")
        
        # Feedback based on score
        if percentage == 100:
            st.balloons()
            st.write("Perfect score! You're an India expert!")
        elif percentage >= 60:
            st.write("Great job! You know a lot about India!")
        else:
            st.write("Nice try! Keep learning about India!")
        
        # Reset quiz button
        if st.button("Restart Quiz"):
            st.session_state.score = 0
            st.session_state.current_question = 0
            st.session_state.answered = False
            st.session_state.user_answer = None
            st.session_state.quiz_completed = False
            st.session_state.shuffled_questions = random.sample(quiz_data, len(quiz_data))
            st.experimental_rerun()

if __name__ == "__main__":
    run_quiz()
