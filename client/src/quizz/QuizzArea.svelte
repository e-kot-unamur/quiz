<script>
    import Question from './quizz/Question.svelte';
    import Answer from './quizz/Answer.svelte';
    import Justification from './quizz/Justification.svelte';


    let quizzIndex = 0;
	let justification = "";
    const quizz = [
		{
        "type" : "VF",
        "question": "Exemple de question 1 ?",
        "answers": ['Vrai', 'Faux'],
		"correctAnswer": 0,
        "justificationTrue":"Bonne réponse ! T'es vraiment un pro de la baise !",
        "justificationFalse":"Faux ! Faut vraiment que tu te renseignes mon bougre !"
    	},
		{
		"type" : "VF",
        "question": "Exemple de question 2 ?",
        "answers": ['Vrai', 'Faux'],
		"correctAnswer": 1,
        "justificationTrue":"Bonne réponse ! T'es vraiment un pro de la baise !",
        "justificationFalse":"Faux ! Faux vraiment que tu renseigne mon bougre !"	
		}
	]
	
	function checkAnswerHandler(answerText){
		let currentQuestion = quizz[quizzIndex];
		
		if(currentQuestion.answers.indexOf(answerText) === currentQuestion.correctAnswer){
			//todo : add the points
			justification = "";
			justification += quizz[quizzIndex].justificationTrue;
		}
		else {
			justification = "";
			justification += quizz[quizzIndex].justificationFalse;

		}	
	}
	function nextQuestion(){
		quizzIndex +=1;
	}
	 

</script>

<div class="QuizzArea">

	<Question questionText = {quizz[quizzIndex].question} />
	
	<div class="answers">
		<Answer answerText = {quizz[quizzIndex].answers[0]} checkAnswerHandler = {checkAnswerHandler} />
		<Answer answerText = {quizz[quizzIndex].answers[1]} checkAnswerHandler = {checkAnswerHandler} />
	</div>
	<Justification justification = {justification}/>
	<button onclick="nextQuestion()"> Question suivante</button>
</div>

<style>

</style>
