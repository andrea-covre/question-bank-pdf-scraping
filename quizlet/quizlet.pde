JSONObject database;
IntList timeline;

int currentIndex = 1;
JSONObject currentQuestion;
Boolean showAnswer = false;

void setup() {
  size(800, 600);
  database = loadJSONObject("bancaDati.json");
  timeline = new IntList();
  timeline.append(1);
  currentQuestion = getNewQuestion();
}

void draw() {
  background(0);
  fill(255);
  try {
    textSize(14);
    text("Session index: " + currentIndex, 50, 10, 700, 200);
    
    //Q:
    textSize(25);
    text(currentQuestion.getString("Q"), 50, 50, 700, 200);
    
    //A)
    textSize(20);
    //println(currentQuestion.getString("ans"));
    if (showAnswer) {
      if (currentQuestion.getString("ans").equals("A")) {
        fill(0, 255, 0);
      } else {
        fill(255, 0, 0);
      }
    }
    text(currentQuestion.getString("A"), 100, 200, 650, 200);
    
    //B)
    if (showAnswer) {
      if (currentQuestion.getString("ans").equals("B")) {
        fill(0, 255, 0);
      } else {
        fill(255, 0, 0);
      }
    }
    text(currentQuestion.getString("B"), 100, 300, 650, 200);
    
    //C)
    if (showAnswer) {
      if (currentQuestion.getString("ans").equals("C")) {
        fill(0, 255, 0);
      } else {
        fill(255, 0, 0);
      }
    }
    text(currentQuestion.getString("C"), 100, 400, 650, 200);
    
    //D)
    if (showAnswer) {
      if (currentQuestion.getString("ans").equals("D")) {
        fill(0, 255, 0);
      } else {
        fill(255, 0, 0);
      }
    }
    text(currentQuestion.getString("D"), 100, 500, 650, 200);
  } catch (Exception e) {
    timeline.remove(timeline.size() - 1);
    currentQuestion = getNewQuestion();
  }
  //print(currentIndex);
  //print("   Q: ");
  //println(timeline.get(currentIndex));
  
}


JSONObject getNewQuestion() {
  int i = int(random(1, 6001));
  JSONObject question;
  try {
    question = database.getJSONObject(String.valueOf(i));
    timeline.append(i);
  } catch (Exception e) {
    question = getNewQuestion();
  }
  return question;
}

JSONObject getQuestion(int i) {
  return database.getJSONObject(String.valueOf(i));
}
