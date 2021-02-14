<script>
    
	import Question from './Question.svelte';
    import Answer from './Answer.svelte';
    import Justification from './Justification.svelte';
	import AnswerColor from './AnswerClolor.svelte';

    let quizzIndex = 0;
	let endQuizz = false;
	let selected = false;
	let goodAnswer = false;
	let justification = "";
	
    
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
        "answers": ['green', 'orange', 'red'],
		"correctAnswer": 2,
        "justificationTrue":"Bonne réponse ! Le numérique produit 6% des émissions de gaz à effet de serre et 4% de la consommation électrique mondiale. Ces chiffres concernent la production d’appareils, leur utilisation et l’utilisation d’internet. ",
        "justificationFalse":"Faux ! Le numérique produit 6% des émissions de gaz à effet de serre et 4% de la consommation électrique mondiale. Ces chiffres concernent la production d’appareils, leur utilisation et l’utilisation d’internet.  !"

		}

	]
	
	function checkAnswerHandler(answerText){
		let currentQuestion = quizz[quizzIndex];
		
		if(currentQuestion.answers.indexOf(answerText) === currentQuestion.correctAnswer && selected == false){
			
			selected = true;
			goodAnswer = true;
			justification = "";
			justification += quizz[quizzIndex].justificationTrue;
		}
		else if(currentQuestion.answers.indexOf(answerText) != currentQuestion.correctAnswer && selected == false) {
			selected = true;
			goodAnswer = false;
			justification = "";
			if(currentQuestion.answers)
			justification += quizz[quizzIndex].justificationFalse;

		}	
	}
	
	function navButton(){
		if(selected != false){
			justification = "";
			selected = false;
			if( quizzIndex <= quizz.length - 2 ){
				quizzIndex += 1;
				testText = quizzIndex;
			} 
			else endQuizz = true;
		}
	}
</script>

<style>
	.quizzArea {
		/* Verticial align */
		margin: 50vh auto 0 auto; 
		transform: translateY(-50%);
		
		/*background-color: whitesmoke;*/
		background-color: #D3EAEB;
		padding : 30px 45px;
		width : 90%;
	}

	.nextQuestion {
		margin: 10px auto;
		display: block;
		background-color: white;
		border : 1px solid blue;
		border-radius: 5px;
		text-align: center;
	}

	@media (min-width: 768px) { 
		.quizzArea {
			width : 50%;
		}	

		.nextQuestion {
			width: 25%;
		}
	}
</style>

	<div class="quizzArea container-fluid rounded-1 shadow-lg ">
		<!-- Question -->
		{#if !endQuizz}
			<div class="row align-items-center text-center mb-3">
				<Question questionText = {quizz[quizzIndex].question} />
			</div>
		{/if}
		<!-- Answers -->
		<div class="row align-items-center answers">
			{#if quizz[quizzIndex].type == "VF" && !endQuizz}
				<Answer answerText = {quizz[quizzIndex].answers[0]} checkAnswerHandler = {checkAnswerHandler} bgColor = '#8D6F9E' />
				<Answer answerText = {quizz[quizzIndex].answers[1]} checkAnswerHandler = {checkAnswerHandler} bgColor = '#579E78' />
			{:else if quizz[quizzIndex].type == "QCM" && !endQuizz}
				<Answer answerText = {quizz[quizzIndex].answers[0]} checkAnswerHandler = {checkAnswerHandler} bgColor = '#8D6F9E'/>
				<Answer answerText = {quizz[quizzIndex].answers[1]} checkAnswerHandler = {checkAnswerHandler} bgColor = '#579E78'/>	
				<Answer answerText = {quizz[quizzIndex].answers[2]} checkAnswerHandler = {checkAnswerHandler} bgColor = '#86CAF4' />
				<Answer answerText = {quizz[quizzIndex].answers[3]} checkAnswerHandler = {checkAnswerHandler} bgColor = '#9E824F'/>
			
				{:else if quizz[quizzIndex].type == "color" && !endQuizz}
				<AnswerColor color = "green" checkAnswerHandler = {checkAnswerHandler} />
				<AnswerColor color = "orange" checkAnswerHandler = {checkAnswerHandler} />
				<AnswerColor color = "red" checkAnswerHandler = {checkAnswerHandler} />
			{/if}
		</div>	

		<!-- Justification -->
		<div class="row align-items-center text-center">
			<Justification justification = {justification} {goodAnswer}/>
		</div>

		<!-- Next question -->
		{#if selected}
			<div class="row next">
				<div class="col">
					{#if quizzIndex === quizz.length - 1}
						<button class="results"> Allez au résultats <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-circle" viewBox="0 0 16 16">
							<path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/>
						</svg> 
						</button>
					{:else }
						<button on:click={() => navButton()} class="nextQuestion"> Question suivante <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-circle" viewBox="0 0 16 16">
						<path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/>
						</svg> 
						</button>
					{/if}
				</div>
			</div>
		{/if}
</div>
