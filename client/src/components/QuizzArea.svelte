<script>
    
	import Question from './Question.svelte';
    import Answer from './Answer.svelte';
    import Justification from './Justification.svelte';
	import AnswerColor from './AnswerClolor.svelte';
	import Results from './Results.svelte';
	import Help from './Help.svelte';
	
	import * as mainQuizz from "./mainQuizz.json";
	
	export let index;

	const timerInSeconds = 10;
    let quizzIndex = 0;
	let endQuizz = false;
	let selected = false;
	let goodAnswer = false;
	let justification = "";
	let points = 0;
	let totalTime = 0;
	let time = timerInSeconds;
	
	
	// Test Baetslé Routing 
	let quizzStart = false;
	let quizzResult = false;

	function startQuizz() {
		quizzStart = true;
		timer = setInterval(updateTimer,1000);
	}

	function viewResult() {
		quizzResult = true;
	}

	// End test Baetsle 
	
	const quizz = mainQuizz.allQuizz[index].quizz; 
	
	
	function checkAnswerHandler(answerText){
		
		let currentQuestion = quizz[quizzIndex];
		// if it is the right answer
		if(currentQuestion.answers.indexOf(answerText) === currentQuestion.correctAnswer && selected == false){
			selected = true;
			goodAnswer = true;
			justification = "";
			justification += quizz[quizzIndex].justificationTrue;
			points += 1;
			
		}
		// if it is the wrong answer
		else if(currentQuestion.answers.indexOf(answerText) != currentQuestion.correctAnswer && selected == false ){
			selected = true;
			goodAnswer = false;
			justification = "";
			if(currentQuestion.answers)
			justification += quizz[quizzIndex].justificationFalse;
			
		}
		console.log(points)
	}
	
	function navButton(){
		if(selected != false){
			justification = "";
			selected = false;			
			quizzIndex += 1;
			// timer
			time = timerInSeconds;
			timer = setInterval(updateTimer,1000);
			if(quizzIndex === quizz.length ) endQuizz = true;
		}
	}

	// Timer
	//let timer = setInterval(updateTimer,1000);
	let timer;
	function updateTimer(){

		if(time > 0)
			time--;

		if(selected){
			clearInterval(timer);
			totalTime += timerInSeconds - time;
		}
		
		if(!selected && time == 0) {
			clearInterval(timer);
			selected = true;
			goodAnswer = false;
			justification += quizz[quizzIndex].justificationFalse;
			totalTime += timerInSeconds - time;
			
		};		
	}

</script>

<style>
	.presentationArea {
		margin-top: 20px;
		background-color: #D3EAEB;
		padding : 30px 45px;
		width : 90%;
	}

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
		fill : black;
		margin-top: 10px;
		position: relative;
		left : 55%
	}

	.results {
		margin-top: 10px;
		position: relative;
		left : 50%
	}

	.justification {
		width : 90%;
		margin: auto;
		text-align: center;
		
		position: fixed;
		top : 2px;
		left: 5%;
		z-index: 1;
	}

	.progressBar {
		display: inline-block;
	}

	@media (min-width: 850px) { 
		.presentationArea {
			width: 70%;
		}
		.quizzArea {
			width : 50%;
		}	

		.nextQuestion {
			width: 25%;
			fill : black;
			left : 65%;
		}

		.justification {
			width: 50%;
			left : 25%;
		}

		.results {
			left : 80%;
		}
	}
</style>


	<!-- Introduction au Quizz -->
	{#if !quizzStart}
		<div class="presentationArea container-fluid rounded-1 shadow-lg">
			<Help />
			<button on:click={() => {startQuizz()}} >Next</button>
		</div>
	{:else if quizzResult} 
		<div class="quizzArea container-fluid rounded-1 shadow-lg ">
			<Results score = {points} totalScore = {quizz.length} totalTime = {totalTime}  facts = {mainQuizz.allQuizz[index].facts} />
		</div>
	{:else}
		<!-- Justification -->
		<div class="justification">
			<Justification justification = {justification} {goodAnswer}/>
		</div>
		
		<div class="quizzArea container-fluid rounded-1 shadow-lg ">
			<div>{time}s</div>
			<!-- Question -->
			{#if !endQuizz }
				<div class="row align-items-center text-center mb-3">
					<Question questionText = {quizz[quizzIndex].question} />
				</div>
			{/if}
			<!-- Answers -->
			<div class="row align-items-center answers">
				{#if quizz[quizzIndex].type == "VF" && !endQuizz}
					<Answer answerText = {quizz[quizzIndex].answers[0]} checkAnswerHandler = {checkAnswerHandler} bgColor = '#8D6F9E' {selected} />
					<Answer answerText = {quizz[quizzIndex].answers[1]} checkAnswerHandler = {checkAnswerHandler} bgColor = '#579E78' {selected} />
				{:else if quizz[quizzIndex].type == "QCM" && !endQuizz}
					<Answer answerText = {quizz[quizzIndex].answers[0]} checkAnswerHandler = {checkAnswerHandler} bgColor = '#8D6F9E' {selected}/>
					<Answer answerText = {quizz[quizzIndex].answers[1]} checkAnswerHandler = {checkAnswerHandler} bgColor = '#579E78' {selected}/>	
					<Answer answerText = {quizz[quizzIndex].answers[2]} checkAnswerHandler = {checkAnswerHandler} bgColor = '#86CAF4' {selected} />
					<Answer answerText = {quizz[quizzIndex].answers[3]} checkAnswerHandler = {checkAnswerHandler} bgColor = '#9E824F' {selected}/>
				{:else if quizz[quizzIndex].type == "color" && !endQuizz}
					<AnswerColor color = "green" checkAnswerHandler = {checkAnswerHandler} {selected}/>
					<AnswerColor color = "orange" checkAnswerHandler = {checkAnswerHandler} {selected}/>
					<AnswerColor color = "red" checkAnswerHandler = {checkAnswerHandler} {selected}/>
				{/if}
			</div>

			<!-- Next question -->
			{#if selected}
				<div class="row next">
					<div class="col">
						{#if quizzIndex === quizz.length - 1}
							<button on:click={() => {viewResult()}} class="results"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-award" viewBox="0 0 16 16">
								<path d="M9.669.864L8 0 6.331.864l-1.858.282-.842 1.68-1.337 1.32L2.6 6l-.306 1.854 1.337 1.32.842 1.68 1.858.282L8 12l1.669-.864 1.858-.282.842-1.68 1.337-1.32L13.4 6l.306-1.854-1.337-1.32-.842-1.68L9.669.864zm1.196 1.193l.684 1.365 1.086 1.072L12.387 6l.248 1.506-1.086 1.072-.684 1.365-1.51.229L8 10.874l-1.355-.702-1.51-.229-.684-1.365-1.086-1.072L3.614 6l-.25-1.506 1.087-1.072.684-1.365 1.51-.229L8 1.126l1.356.702 1.509.229z"/>
								<path d="M4 11.794V16l4-1 4 1v-4.206l-2.018.306L8 13.126 6.018 12.1 4 11.794z"/>
							</svg>  Voir mes résultats 
							</button>
						{:else }
							<div class="progressBar">
								Reste : {quizz.length - quizzIndex - 1} question{quizz.length - quizzIndex - 1 === 1 ? '' : 's'}
							</div>
							<svg on:click={() => {navButton();}} class="nextQuestion" xmlns="http://www.w3.org/2000/svg"  height="40" viewBox="0 0 16 16">
								<path style="cursor:pointer" d="M0 14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v12zm4.5-6.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5a.5.5 0 0 1 0-1z"/>
							</svg>
						{/if}
					</div>
				</div>
			{/if}
			<!--<Results points= {points}/>-->
		</div>
	{/if}
