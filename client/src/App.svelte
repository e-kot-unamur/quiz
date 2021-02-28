<script>
import {Router, Route,Link} from "svelte-routing";
import Navbar from "./components/Navbar.svelte";
import Main from "./routes/main/Main.svelte";
import About from "./routes/about/About.svelte";
import ISTQuizz from "./routes/quizz/GlobalQuizz.svelte";
import Results from "./components/Results.svelte"
export let url = "";
import * as mainQuizz from "./components/mainQuizz.json";
</script>



<svelte:head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://use.typekit.net/bqg3mtv.css">
</svelte:head>

<style>
    main {
        background-color: #609d9f;
		padding-bottom: 70px;
    }
</style>

<main>
	<Router {url}>
		<div>
			<Route path="/" component={Main} />
			<Route path="about" component={About} />
			<Route path="Results" component={Results} />

			{#each mainQuizz.allQuizz as quizz,i}
				<Route path="{quizz.route}"><ISTQuizz index={i} /></Route>
			{/each}			
		</div>
	</Router>
</main>
