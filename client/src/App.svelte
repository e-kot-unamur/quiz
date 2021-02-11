<script>
	import {Router, Route, Link} from "svelte-routing";
	import Navbar from "./routes/Navbar.svelte";
	import Main from "./routes/main/Main.svelte";
	import About from "./routes/about/About.svelte";
	import Quizzes from "./routes/quizzes/Quizzes.svelte";
	import Help from "./routes/help/Help.svelte";
	export let url = "";
</script>

<main>
		<Router {url}>
			<Navbar />
			<div>
				<Route component={Main} />
				<Route path="IST-MST/0" component={Help} />
				<Route path="IST-MST/1" component={Quizzes} />
				<Route path="about" component={About} />
			</div>
		</Router>
</main>
