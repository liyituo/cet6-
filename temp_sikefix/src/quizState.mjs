export function createQuiz(lesson) {
  return {
    lessonId: lesson.id,
    lesson,
    currentIndex: 0,
    answers: [],
    isComplete: lesson.questions.length === 0,
  };
}

export function answerCurrent(quiz, selectedLabel) {
  if (quiz.isComplete) {
    throw new Error("Cannot answer a complete quiz.");
  }

  const question = quiz.lesson.questions[quiz.currentIndex];
  const selectedOption = question.options.find(
    (option) => option.label === selectedLabel,
  );
  const correctOption = question.options.find(
    (option) => option.label === question.answer,
  );
  const answer = {
    number: question.number,
    selected: selectedLabel,
    selectedText: selectedOption?.text || "",
    correct: question.answer,
    correctText: question.answerText || correctOption?.text || "",
    isCorrect: selectedLabel === question.answer,
  };
  const answers = [...quiz.answers, answer];
  const currentIndex = quiz.currentIndex + 1;
  const isComplete = currentIndex >= quiz.lesson.questions.length;

  return {
    ...quiz,
    currentIndex: isComplete ? quiz.currentIndex : currentIndex,
    answers,
    isComplete,
  };
}

export function getResult(quiz) {
  const total = quiz.lesson.questions.length;
  const correct = quiz.answers.filter((answer) => answer.isCorrect).length;
  return {
    correct,
    total,
    percent: total === 0 ? 0 : Math.round((correct / total) * 100),
  };
}
