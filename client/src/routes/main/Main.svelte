<script>
    
    import Navbar from "../../quizz/Navbar.svelte";
    import Tuille from "../../quizz/Tuille.svelte";
    import * as mainQuizz from "../../quizz/mainQuizz.json";
</script>

<style>

</style>

<Navbar />

{#each mainQuizz.allQuizz as quizz }
    <h1>Test</h1>


{/each}

<Tuille src="images/STD.png">
    <span slot="title">
        {mainQuizz.allQuizz[0].title}
    </span>

    <span slot="proposeBy">
        {mainQuizz.allQuizz[0].creator}
    </span>
</Tuille>




