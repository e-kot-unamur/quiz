<script>
	import {Router, Route, Link} from "svelte-routing";
	import Navbar from "./routes/Navbar.svelte";
	import About from "./routes/about/About.svelte";
	import Quizzes from "./routes/quizzes/Quizzes.svelte";

	const contact = "https://www.messenger.com/t/ekotnamur";
	export let url = "";
</script>

<main>
		<Router {url}>
			<Navbar />
			<div>
				<Route path="/" component={Quizzes} />
				<Route path="about" component={About} />
				<Route path="contact" component={contact} />
			</div>
		</Router>
</main>
