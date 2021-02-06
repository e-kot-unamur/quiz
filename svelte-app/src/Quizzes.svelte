<!-- Manage all quizzes -->
<script>
    //Uses each individual user
    import Quiz from './Quiz.svelte'
    import { quizzes } from './data-quiz.js'
</script>

<div id="quizzes">
    {#each Object.keys($quizzes) as key}
    <Quiz key={key} quiz={$quizzes[key]} />
    {/each}
   <!--  <pre>
        {JSON.stringify($quizzes, null, 2)}  To display them in vertical mode
    </pre> -->
</div>