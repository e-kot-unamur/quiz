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
	let points = 0;
	
	const quizz = [
		{
		"type" : "QCM",
        "question": "En 2018, les USA ont atteint un triste record de personnes qui ont contracté une MST. Combien de personnes en ont attrapé ?",
        "answers": ['1 million', '2 millions', '4 millions', '8 millions'],
		"correctAnswer": 1,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux ! 2 millions de personnes on contracté une MST aux USA en 2018 !"	
		},
		{
		"type" : "QCM",
        "question": "Les personnes les plus affectées par la Syphilis sont :",
        "answers": ['Les femmes de 25 à 40 ans', 'Les femmes de 20 à 30 ans', 'Les hommes de 25 à 40 ans', 'Les hommes de 20 à 30 ans'],
		"correctAnswer": 2,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux ! Les personnes les plus affectées par la Syphilis sont les hommes de 25 à 40 ans !"	
		},
		{
		"type" : "QCM",
        "question": "En 1 an, ..... personnes dans le monde contractent une MST tels que la chlamydia, gonorrhée ou syphilis.",
        "answers": ['268 millions', '357 millions', '374 millions', '412 millions'],
		"correctAnswer": 1,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux ! La réponse est 357 millions !"	
		},
		{
		"type" : "QCM",
        "question": "Quelle est l’IST la plus fréquente en Belgique ?",
        "answers": ['La chlamydia ', 'La gonorrhée', 'La syphilis', 'La trichomonase'],
		"correctAnswer": 0,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux ! L'IST la plus fréquente en Belgique la chlamydia !"	
		},
		{
		"type" : "QCM",
        "question": "Par jour, dans le monde, combien de personnes contractent une IST ?",
        "answers": ['Plus de 800 000', 'Plus d’1 million ', 'Plus de 1.5 million', 'Plus de 2 millions'],
		"correctAnswer": 1,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux ! Plus d'1 million de personnes contractent une IST par jour dans le monde !"	
		},
		{
		"type" : "QCM",
        "question": "Quelle région du monde est celle la plus touchée par le nombre de cas de VIH (virus de l'immunodéficience humaine) ?",
        "answers": ['L’afrique subsaharienne', 'L’europe centrale', 'L’amérique latine ', 'L’Asie centrale'],
		"correctAnswer": 0,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux ! La région la plus touchée par le VIH est l'afrique subsaharienne !"
		},
		{
		"type" : "QCM",
        "question": "Quelle est l’IST la plus fréquente en Inde ?",
        "answers": ['Le granulome inguinal', 'Le chancre mou', 'L’herpès génital', 'La gonorrhée'],
		"correctAnswer": 2,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux ! L’IST la plus fréquente en Inde est l'herpès génital !"	
		},
		{
		"type" : "QCM",
        "question": "Combien de personnes sont touchées par une MST en moyenne dans le monde ?",
        "answers": ['1 personne sur 10', '1 personne sur 25', '1 personne sur 50', '1 personne sur 200'],
		"correctAnswer": 1,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux ! 1 personne sur 25 est touché par une MST dans le monde !"	
		},
		{
		"type" : "QCM",
        "question": "Avec les années, le nombre de personnes infectées par une MST...",
        "answers": ['Augmente ', 'Diminue', 'Reste stable', 'Se rapproche de 0'],
		"correctAnswer": 0,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux ! Le nombre de personnes infectées par une MST augmente !"	
		},
		{
		"type" : "QCM",
        "question": "Quel pays a distribué des préservatifs pour combattre le virus Zika (une MST aussi) ?",
        "answers": ['La Chine', 'Le pérou', 'Les Etats-Unis', 'L’Inde'],
		"correctAnswer": 1,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux ! C'est le Pérou !"	
		},
		{
		"type" : "QCM",
        "question": "Quelles sont les quatre infections les plus répandues chez les personnes de 15 à 49 ?",
        "answers": ['Le VIH, la mycose, la syphilis et la chlamydia', 'La chlamydiose, la gonorrhée, la syphilis et la trichomonase', 'Les poux', 'D’autres MST tel que l’infection par le VIH'],
		"correctAnswer": 1,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux ! C'est la chlamydiose, la gonorrhée, la syphilis et la trichomonase"	
		},
		{
		"type" : "QCM",
        "question": "Combien de temps dois-je attendre pour faire un dépistage du VIH par prise de sang après une prise de risque ?",
        "answers": ['1 jours', '2 semaines', '6 semaines', '3 mois'],
		"correctAnswer": 2,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux !"	
		},
		{
		"type" : "VF",
        "question": "Les IST se transmettent uniquement lors des pénétrations non protégées",
        "answers": ['Vrai', 'Faux'],
		"correctAnswer": 1,
        "justificationTrue":"Bonne réponse ! Un simple contact cutané avec des lésions peut suffire à transmettre certaines IST !",
        "justificationFalse":"C’est faux, un simple contact cutané avec des lésions peut suffire à transmettre certaines IST !"	
		},
		{
		"type" : "QCM",
        "question": "En 2019, combien de personnes vivaient avec le VIH dans le monde ?",
        "answers": ['12 millions', '25 millions', '38 millions', '44 millions'],
		"correctAnswer": 2,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux ! 38 millions de personnes vivaient avec le VIH dans le monde en 2019 !"	
		},
		{
		"type" : "QCM",
        "question": "Quelle est l’espérance de vie d’une personne atteinte du sida dans le monde ?",
        "answers": ['- de 5 ans', '+ de 5 ans', '+ de 10 ans', '+ de 20 ans'],
		"correctAnswer": 3,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux ! L’espérance de vie d’une personne atteinte du sida est de plus de 20 ans !"	
		},
		{
		"type" : "QCM",
        "question": "Laquelle de ces propositions ne protège PAS des MST?",
        "answers": ['le préservatif masculin', 'Le préservatif féminin', 'La pilule contraceptive', 'Digue dentaire (carré latex)'],
		"correctAnswer": 2,
        "justificationTrue":"Bonne réponse !",
        "justificationFalse":"Faux !"	
		},
		{
        "type" : "VF",
        "question": "Lors d’un match d’improvisation un jouteur peut être exclu du match.",
        "answers": ['Vrai', 'Faux'],
		"correctAnswer": 0,
        "justificationTrue":"Bonne réponse ! Lors d’un match d'improvisation, il arrive qu’un jouteur puisse se faire sortir de scène dans le cas où il a accumulé deux fautes personnelles.",
        "justificationFalse":"Faux ! Lors d’un match d'improvisation, il arrive qu’un jouteur puisse se faire sortir de scène dans le cas où il a accumulé deux fautes personnelles.!"
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
			points += 1;
		}
		else if(currentQuestion.answers.indexOf(answerText) != currentQuestion.correctAnswer && selected == false) {
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
			if(quizzIndex === quizz.length - 1) endQuizz = false;
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
		left: 5%;
		z-index: 1;
	}

	.progressBar {
		display: inline-block;
	}

	@media (min-width: 850px) { 
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

	<!-- Justification -->
	<div class="justification">
		<Justification justification = {justification} {goodAnswer}/>
	</div>

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
						<button class="results"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-award" viewBox="0 0 16 16">
							<path d="M9.669.864L8 0 6.331.864l-1.858.282-.842 1.68-1.337 1.32L2.6 6l-.306 1.854 1.337 1.32.842 1.68 1.858.282L8 12l1.669-.864 1.858-.282.842-1.68 1.337-1.32L13.4 6l.306-1.854-1.337-1.32-.842-1.68L9.669.864zm1.196 1.193l.684 1.365 1.086 1.072L12.387 6l.248 1.506-1.086 1.072-.684 1.365-1.51.229L8 10.874l-1.355-.702-1.51-.229-.684-1.365-1.086-1.072L3.614 6l-.25-1.506 1.087-1.072.684-1.365 1.51-.229L8 1.126l1.356.702 1.509.229z"/>
							<path d="M4 11.794V16l4-1 4 1v-4.206l-2.018.306L8 13.126 6.018 12.1 4 11.794z"/>
						  </svg>  Voir mes résultats {points}/{quizz.length}
						</button>
					{:else }
						<div class="progressBar">
							Il reste : {quizz.length - quizzIndex - 1} question{quizz.length - quizzIndex - 1 === 1 ? '' : 's'}
							
						</div>
						<svg on:click={() => navButton()} style="cursor : pointer" class="nextQuestion" xmlns="http://www.w3.org/2000/svg"  height="40" viewBox="0 0 16 16">
							<path d="M0 14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v12zm4.5-6.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5a.5.5 0 0 1 0-1z"/>
						 </svg>
					{/if}
				</div>
			</div>
		{/if}
	</div>