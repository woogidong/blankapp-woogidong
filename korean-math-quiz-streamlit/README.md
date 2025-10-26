# Korean Math Quiz Streamlit

This project is a math learning application built with Streamlit, designed to provide quizzes based on the South Korean middle and high school math curriculum. The app identifies weak areas based on incorrect answers, helping users improve their understanding of mathematical concepts.

## Features

- **Quizzes**: Interactive quizzes covering various topics from the South Korean curriculum for middle and high school students.
- **Review**: Users can review their answers, see correct responses, and understand explanations for questions they got wrong.
- **Analytics**: Performance analytics that highlight weak areas and track progress over time.
- **User Progress Tracking**: Monitors user performance and provides insights into areas needing improvement.

## Project Structure

```
korean-math-quiz-streamlit
├── src
│   ├── streamlit_app.py        # Main entry point for the Streamlit application
│   ├── pages                   # Contains different pages of the app
│   │   ├── home.py             # Home page with navigation options
│   │   ├── quiz.py             # Quiz functionality
│   │   ├── review.py           # Review of quiz answers
│   │   └── analytics.py        # User performance analytics
│   ├── data                    # Data files for curriculum and questions
│   │   ├── curriculum
│   │   │   ├── middle_school.json  # Middle school curriculum data
│   │   │   └── high_school.json    # High school curriculum data
│   │   └── questions
│   │       └── sample_questions.json # Sample quiz questions
│   ├── models                  # Models for user progress tracking
│   │   └── user_progress.py    # User progress tracking functionality
│   ├── utils                   # Utility functions for the app
│   │   ├── quiz_generator.py    # Functions to generate quizzes
│   │   ├── scorer.py            # Functions to calculate scores
│   │   └── curriculum_mapper.py  # Maps curriculum topics to quiz questions
│   └── components              # Reusable UI components
│       ├── ui.py               # UI components for the app
│       └── charts.py           # Visualization functions for analytics
├── tests                       # Unit tests for the application
│   ├── test_quiz_generator.py   # Tests for quiz generation
│   └── test_scoring.py          # Tests for scoring functionality
├── requirements.txt            # Project dependencies
├── .streamlit                  # Streamlit configuration
│   └── config.toml            # Configuration settings for the app
├── .gitignore                  # Files to ignore by Git
└── README.md                   # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd korean-math-quiz-streamlit
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```
   streamlit run src/streamlit_app.py
   ```

## Usage

- Navigate through the home page to access quizzes, review sections, and analytics.
- Complete quizzes and review your answers to identify areas for improvement.
- Use the analytics page to track your progress and performance over time.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.