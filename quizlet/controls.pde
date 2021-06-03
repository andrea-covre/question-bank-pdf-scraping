void keyPressed() {
  if (keyCode == LEFT) {
    if (currentIndex > 1) {
      currentIndex -= 1;
      currentQuestion = getQuestion(timeline.get(currentIndex));
    }
    showAnswer = false;
  }
  if (keyCode == RIGHT) {
    if (currentIndex == timeline.size() - 1) {
      currentQuestion = getNewQuestion();
      currentIndex += 1;
    } else {
      currentIndex += 1;
      currentQuestion = getQuestion(timeline.get(currentIndex));
    }
    showAnswer = false;
  }
  if (key == 32) {
    showAnswer = !showAnswer;
  }
}
