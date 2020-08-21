// 
/* //<form accept-charset="UTF-8" action="action_page.php" autocomplete="off" method="GET" target="_blank"><fieldset>
    <legend>Title:</legend> 
    <label for="name">Name</label><br /> <input name="name" type="text" value="Frank" /> <br /> 
    <input checked="checked" name="sex" type="radio" value="male" /> Male <br /> <input name="sex" 
    type="radio" value="female" /> Female <br /> <textarea cols="30" rows="2">Long text.</textarea><br /><select>
    <option selected="selected" value="1">Yes</option>
    <option value="2">No</option>
    </select><br /> <input name="democheckbox" type="checkbox" value="1" /> Checkbox<br /> 
      */

//<! github test comment -->

var questionContainer = document.getElementbyID('question');
// you'll probably need to create a container for each type of question (MC, checkbox, sliders)
var resultsContainer = document.getElementbyID('results');
var submitButton = document.getElementbyID('submit');



// objects to represent indiv. questions + array to hold all the questions in a form
// allocate each chunk of questions to their respective form .js file (form1,form2,form3)
// aka remove all these myQuestions objects from the main server page
const myQuestions = [
{
  question: "1. How old are you?",
  answers: {
    a: "Under 18",
    b: "18-24",
    c: "25-34",
    d: "35-44",
    e: "45-54",
    f: "55-64",
    g: "65+"
  },
},
{
  question: "2. What is your gender?",
  answers: {
    a: "Female"
    b: "Male"
    c: "Transgender"
    d: "Prefer not to say"
  },
},
{
  question: "3. What is your sexual orientation?"
  answers: {
    a: "Heterosexual",
    b: "Homosexual",
    c: "Bisexual",
    d: "Pansexual",
    e: "Asexual"
  },
},


]


function buildForm(){
  // variable to store the HTML output
  const output = [];

  // for each question...
  myQuestions.forEach(
    (currentQuestion, questionNumber) => {

      // variable to store the list of possible answers
      const answers = [];

      // and for each available answer....
      for(letter in currentQuestion.answers){

        //...add an HTML radio button
        answers.push(
          `<label>
            <input type="radio" name="question${questionNumber}" value="${letter}">
            ${letter} :
            ${currentQuestion.answers[letter]}
          </label>`
          );
      }

      // add this question and its answers to the output
      output.push(
        `<div class="question"> ${currentQuestion.question} </div>
        <div class="answers"> ${answers.join('')} </div>`
      );
    }
  );

  // finally combine our output list into one string of HTML and put it on the page
  quizContainer.innerHTML = output.join('');
}

function showResults(){}

// display form right away
buildForm();


// on submit, show results
submitButton.addEventListener('click', showResults);


