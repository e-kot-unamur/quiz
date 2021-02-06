<script>
	import { Router, Route } from "svelte-routing";
	import About from "./About.svelte";
	import Quizzes from './Quizzes.svelte'
	export let url = "";
</script>
<main>
	<Quizzes />
	<div class="container">
		<Router {url}>
		  <Route path="/about" component={About} />
		</Router>
	</div>
	
</main>
