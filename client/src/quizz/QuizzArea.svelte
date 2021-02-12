<script>
    
	import Question from './Question.svelte';
    import Answer from './Answer.svelte';
    import Justification from './Justification.svelte';
	

    let quizzIndex = 0;
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
		justification = "";
		if(quizz.length == quizzIndex + 1) 
			textNavButton = "Accéder aux résultats";
		else{
			setTimeout(() => quizzIndex += 1 , 1000 );
			selected = false;	
		}
			

			
	}
	

</script>

<div class="QuizzArea">

	<Question questionText = {quizz[quizzIndex].question} />
	
	<div class="answers">
		<Answer answerText = {quizz[quizzIndex].answers[0]} checkAnswerHandler = {checkAnswerHandler} />
		<Answer answerText = {quizz[quizzIndex].answers[1]} checkAnswerHandler = {checkAnswerHandler} />
		{#if quizz[quizzIndex].answers.length === 4 }
			<Answer answerText = {quizz[quizzIndex].answers[2]} checkAnswerHandler = {checkAnswerHandler} />
			<Answer answerText = {quizz[quizzIndex].answers[3]} checkAnswerHandler = {checkAnswerHandler} />
		{/if}
	</div>
	<Justification justification = {justification}/>
	<button on:click={() => navButton()}> {textNavButton} </button>
</div>

<style>

</style>
