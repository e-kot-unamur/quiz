<script>
    
	import Question from './Question.svelte';
    import Answer from './Answer.svelte';
    import Justification from './Justification.svelte';
	import AnswerColor from './AnswerClolor.svelte';

    let quizzIndex = 0;
	let endQuizz = false;
	let selected = false;
	let justification = "";
	let textNavButton = "Question suivante";
    
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
        "justificationFalse":"Faux ! Faut vraiment que tu te renseignes mon bougre !"	
		},
		{
		"type" : "QCM",
        "question": "Exemple de question 3 ?",
        "answers": ['Vrai', 'Faux', 'Peut etre', 'Je ne sais pas'],
		"correctAnswer": 3,
        "justificationTrue":"Bonne réponse ! T'es vraiment un pro de la baise !",
        "justificationFalse":"Faux ! Faut vraiment que tu te renseignes mon bougre !"	
		},
		{
		"type" : "color",
        "question": "Exemple de question 4 ?",
        "answers": ['Vert', 'Orange', 'Rouge'],
		"correctAnswer": 0,
        "justificationTrue":"Bonne réponse ! T'es vraiment un pro de la baise !",
        "justificationFalse":"Faux ! Faut vraiment que tu te renseignes mon bougre !"
		}

	]
	
	function checkAnswerHandler(answerText){
		let currentQuestion = quizz[quizzIndex];
		
		if(currentQuestion.answers.indexOf(answerText) === currentQuestion.correctAnswer && selected == false){
			
			selected = true;
			justification = "";
			justification += quizz[quizzIndex].justificationTrue;
		}
		else if(currentQuestion.answers.indexOf(answerText) != currentQuestion.correctAnswer && selected == false) {
			selected = true;
			justification = "";
			justification += quizz[quizzIndex].justificationFalse;

		}	
	}

	function navButton(){
		if(selected != false){
			justification = "";
			if(quizz.length == quizzIndex + 1){
				textNavButton = "Accéder aux résultats";
				endQuizz = true;
			}
				
			else{
				quizzIndex += 1;
				selected = false;	
			}
		}
	}
	

</script>

<style>
	.quizzArea {
		/* Verticial align */
		margin-top: 50vh; 
  		transform: translateY(-50%); 

		border : 1px solid black;
		padding : 15px;
		width : 100%;
	}

	@media (min-width: 768px) { 
		.quizzArea {
			width : 50%;
		}	
	}
</style>


<div class="quizzArea container-fluid">
		<!-- Question -->
		<div class="row align-items-center text-center">
			<Question questionText = {quizz[quizzIndex].question} />
		</div>

		<!-- Answers -->
		<div class="row align-items-center answers">
			{#if quizz[quizzIndex].type == "VF" && !endQuizz}
				<Answer answerText = {quizz[quizzIndex].answers[0]} checkAnswerHandler = {checkAnswerHandler} />
				<Answer answerText = {quizz[quizzIndex].answers[1]} checkAnswerHandler = {checkAnswerHandler} />
			{:else if quizz[quizzIndex].type == "QCM" && !endQuizz}
				<Answer answerText = {quizz[quizzIndex].answers[0]} checkAnswerHandler = {checkAnswerHandler} />
				<Answer answerText = {quizz[quizzIndex].answers[1]} checkAnswerHandler = {checkAnswerHandler} />	
				<Answer answerText = {quizz[quizzIndex].answers[2]} checkAnswerHandler = {checkAnswerHandler} />
				<Answer answerText = {quizz[quizzIndex].answers[3]} checkAnswerHandler = {checkAnswerHandler} />
			
				{:else if quizz[quizzIndex].type == "color" && !endQuizz}
				<AnswerColor color = "VERT"  />
				<AnswerColor color = "ORANGE" />
				<AnswerColor color = "ROUGE" />
			{/if}
		</div>

		<!-- Justification -->
		<div class="row align-items-center text-center">
			<Justification justification = {justification}/>
			<button on:click={() => navButton()}> {textNavButton} </button>
		</div>
</div>
