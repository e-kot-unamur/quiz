<script>
	//import {Router, Route, Link} from "svelte-routing";
	//import Navbar from "./routes/Navbar.svelte";
	//import Main from "./routes/main/Main.svelte";
	//import About from "./routes/about/About.svelte";
	//import Quizzes from "./routes/quizzes/Quizzes.svelte";
	//import Help from "./routes/help/Help.svelte";
	import QuizzArea from "./quizz/QuizzArea.svelte"
	//const contact = "https://www.messenger.com/t/ekotnamur";
	//export let url = "";
</script>

<svelte:head>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
	<link rel="stylesheet" href="https://use.typekit.net/bqg3mtv.css">
</svelte:head>

<style>
	body {
		height: 100vh;
		background-color: #609d9f;
		border : 1px solid #609d9f;
	}

	.cercle {
		position: absolute;
		display: block;

		animation-name: changeColorAndPlaceCercle;
 	 	animation-duration: 8s;
		animation-iteration-count: infinite;  
		animation-direction: alternate ;
		animation-timing-function: ease;
	}

	@keyframes changeColorAndPlaceCercle {
		0%   {fill:#8DE7EB; left:5%; top:10%; height: 30%;}
		25%  {left:5%; top:11%;}
		50%  {left:6%; top:11%;}
		75%  {left:6%; top:11%;}
		100% {fill:#67A9AB; left:6%; top:11%; height: 35%;}
	}

	.rectangle {
		position: absolute;
		display: block;

		animation-name: changeColorAndPlaceRectangle;
 	 	animation-duration: 10s;
		animation-iteration-count: infinite;  
		animation-direction: alternate ;
		animation-timing-function: ease;
	}

	@keyframes changeColorAndPlaceRectangle {
		0%   {fill:#5EAB82; left:75%; top:70%; height: 95%; transform: rotate(45deg)}
		25%  {left:73%; top:69%;}
		50%  {left:73%; top:69%;}
		75%  {left:73%; top:68%;}
		100% {fill:#64B5A1; left:70%; top:68%; height: 100%; transform: rotate(40deg)}
	}

	.logoEkot {
		position: absolute;
		display: block;

		width : 8%;
		top : 10px;
		left : 90%;
	}
	
	@media (max-width : 850px) {
		.logoEkot {
		width : 15%;
		top : 10px;
		left : 81%;
	}
	}

</style>

<main>
	<!--
		<Router {url}>
			<Navbar />
			<div>
				<Route component={Main} />
				<Route path="IST-MST/0" component={Help} />
				<Route path="IST-MST/1" component={Quizzes} />
				<Route path="about" component={About} />
				<Route path="contact" component={contact} />
			</div>
		</Router>
	-->	
	<body>
		<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="cercle">
			<circle cx="50" cy="50" r="50"/>
		  </svg>

		  <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="rectangle">
			<rect width="100%" height="100%" />
		  </svg>

		  <img src="./logo/logo_blanc.svg" alt="Logo E-kot" class="logoEkot" />
		<QuizzArea/>
	</body>
</main>
