
<script>
import { each } from "svelte/internal";

    import Navbar from "./Navbar.svelte"
    
    export let points = 0;
    export let wrongAnswers = [];
    let email = "";
</script>

<style>
    h1{
        text-align: center;
    }

</style>


<div class="results">
    <Navbar/>
    <h1>Vos résultats</h1>
    <span>Vos points : {points} </span>
    
    <p>Veuillez entrez votre adresse e-mail afin que nous puissions vous recontacter si vous gagnez le concours : </p>
    <input type="text" value={email}/>
    <h1>Justifications </h1>
    {#each wrongAnswers as wrongAnswer}
        <p>{wrongAnswer}</p>
    {/each}

</div>
