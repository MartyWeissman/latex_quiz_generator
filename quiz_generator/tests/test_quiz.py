"""
Tests for the Quiz class
"""
from unittest.mock import Mock

from quiz_generator.quiz import Quiz

def test_quiz_creation():
    """Create a Quiz"""
    question1 = Mock()
    example_quiz = Quiz(
        [question1],
        quiz_name="Test quiz",
        quiz_version="Unit test version",
        preamble="Preamble, preamble, more preamble"
    )
    assert question1 in example_quiz.questions

    question2 = Mock()
    example_quiz.add_question(question2)
    assert question2 in example_quiz.questions

def test_quiz_creation():
    """Test question output is correctly generated for a Quiz"""
    question_1_text = "Content of question1"
    question_2_text = "Content of question2"
    question1 = Mock()
    question1.question_to_latex = question_1_text
    question2 = Mock()
    question2.question_to_latex = question_2_text

    name = "Mock quiz"
    test_quiz = Quiz(
        questions=[question1, question2],
        quiz_name=name
    )
    rendered_quiz = test_quiz.quiz_to_latex()
    assert name in rendered_quiz
    assert question_1_text in rendered_quiz
    assert question_2_text in rendered_quiz

def test_marking_sheet():
    """Test marking sheet correctly made for a Quiz"""
    answer_to_q_1 = "Answer to question1"
    answer_to_q_2 = "Answer to question2"
    question1 = Mock()
    question1.answer_to_latex = answer_to_q_1
    question2 = Mock()
    question2.answer_to_latex = answer_to_q_2

    name = "Mock quiz"
    test_quiz = Quiz(
        questions=[question1, question2],
        quiz_name=name
    )
    marking_sheet = test_quiz.create_marking_sheet()
    assert name in marking_sheet
    assert answer_to_q_1 in marking_sheet
    assert answer_to_q_2 in marking_sheet
