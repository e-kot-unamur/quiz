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
        "question": "Lors d’un match d’improvisation un jouteur peut être exclu du match.",
        "answers": ['Vrai', 'Faux'],
		"correctAnswer": 0,
        "justificationTrue":"Bonne réponse ! Lors d’un match d'improvisation, il arrive qu’un jouteur puisse se faire sortir de scène dans le cas où il a accumulé deux fautes personnelles.",
        "justificationFalse":"Faux ! Lors d’un match d'improvisation, il arrive qu’un jouteur puisse se faire sortir de scène dans le cas où il a accumulé deux fautes personnelles.!"
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
        "question": "La part du numérique des émissions de gaz à effet de serre est de ",
        "answers": ['2%', '6%', '8%', '18%'],
		"correctAnswer": 1,
        "justificationTrue":"Bonne réponse ! Le numérique produit 6% des émissions de gaz à effet de serre et 4% de la consommation électrique mondiale. Ces chiffres concernent la production d’appareils, leur utilisation et l’utilisation d’internet. ",
        "justificationFalse":"Faux ! Le numérique produit 6% des émissions de gaz à effet de serre et 4% de la consommation électrique mondiale. Ces chiffres concernent la production d’appareils, leur utilisation et l’utilisation d’internet.  !"	
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
		margin: 50vh auto 0 auto; 
		transform: translateY(-50%);
		
		padding : 30px 45px;
		width : 90%;
	}

	@media (min-width: 768px) { 
		.quizzArea {
			width : 50%;
		}	
	}
</style>


<div class="quizzArea container-fluid rounded-3 shadow-lg ">
		<!-- Question -->
		<div class="row align-items-center text-center mb-3">
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
