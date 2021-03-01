<script>
    
    import Navbar from "../../components/Navbar.svelte";
    import Tuille from "../../components/Tuille.svelte";
    import * as mainQuizz from "../../components/mainQuizz.json";
</script>

<style>
    
</style>

<svelte:head>
    <link rel="stylesheet" href="hack.css">
</svelte:head>

<Navbar />

{#each mainQuizz.allQuizz as quizz}
    <Tuille src="{quizz.image}" route="{quizz.route}">
        <span slot="title">
            {quizz.title}
        </span>

        <span slot="proposeBy">
            {quizz.creator}
        </span>
</Tuille>

{/each}


