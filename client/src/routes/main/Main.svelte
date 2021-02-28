<script>
    
    import Navbar from "../../quizz/Navbar.svelte";
    import Tuille from "../../quizz/Tuille.svelte";
    import * as mainQuizz from "../../quizz/mainQuizz.json";
</script>

<style>

</style>

<Navbar />

{#each mainQuizz.allQuizz as quizz}
    <Tuille src="images/STD.png" route="IST-MST/help">
        <span slot="title">
            {quizz.title}
        </span>

        <span slot="proposeBy">
            {quizz.creator}
        </span>
</Tuille>

{/each}


