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
</svelte:head>

<style>
	body {
		height: 100%;
		border : 1px solid red;
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
		<QuizzArea/>
	</body>
</main>
