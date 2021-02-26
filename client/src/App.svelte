<script>
import {Router, Route} from "svelte-routing";
import Navbar from "./routes/Navbar.svelte";
import Main from "./routes/main/Main.svelte";
import About from "./routes/about/About.svelte";
import Help from "./routes/help/Help.svelte";
import ISTQuizz from "./quizz/IST.svelte";
const contact = "https://www.messenger.com/t/ekotnamur";
export let url = "";
</script>


<main>
	<Router {url}>
		<Navbar />
		<div>
			<Route component={Main} />
			<Route path="IST-MST/help" component={Help} />
			<Route path="IST-MST" component={ISTQuizz} />
			<Route path="about" component={About} />
		</div>
	</Router>

</main>
