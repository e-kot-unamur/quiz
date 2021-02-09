<!-- Manage all quizzes -->
<script>
    //Uses each individual user
    import Quiz from './Quiz.svelte'
    import { quizzes } from './data-quiz.js'
    import * as quizz1 from './data-quiz.json'
    let test = [quizz1];
</script>
<style>
    table{
        text-align:left;
    }
    table th{
        padding-right: 100px;
    }
</style>
<!-- <div id="quizzes">
    {#each Object.keys($quizzes) as key}
    <Quiz key={key} quiz={$quizzes[key]} />
    {/each}
    <pre>
        {JSON.stringify($quizzes, null, 2)}  To display them in vertical mode
    </pre>
</div> -->
<p>Quiz</p>
<table>
    <tr>
        <th>Question1</th>
        <th>Question2</th> 
        <th>Question3</th>
    </tr>
    <tr>
        <th>
            <p>Type : {quizz1.qu0.type}<br>
            Question : {quizz1.qu0.question}<br>
            {quizz1.qu0.options[0].opt0}<br>
            {quizz1.qu0.options[0].opt1}<br>
            {quizz1.qu0.options[0].opt2}<br>
            Réponse{quizz1.qu0.answer}<br>
            Justif si bon{quizz1.qu0.justificationTrue}<br>
            Justif si faux{quizz1.qu0.justificationFalse}</p>
        </th>
        <th>
            <p>Type : {quizz1.qu1.type}<br>
            Question : {quizz1.qu1.question}<br>
            Faire un bouton vrai/faux<br>
            Réponse{quizz1.qu1.answer}<br>
            Justif si bon{quizz1.qu1.justificationTrue}<br>
            Justif si faux{quizz1.qu1.justificationFalse}</p>
        </th>
        <th>
            <p>Type : {quizz1.qu2.type}<br>
                Question : {quizz1.qu2.question}<br>
                {quizz1.qu2.options[0].opt0}<br>
                {quizz1.qu2.options[0].opt1}<br>
                {quizz1.qu2.options[0].opt2}<br>
                Vert : {quizz1.qu2.answerGreen}<br>
                Orange : {quizz1.qu2.answerOrange}<br>
                Justif Verte{quizz1.qu2.justificationGreen}<br>
                Justif Orange{quizz1.qu2.justificationOrange}
                Justif Rouge{quizz1.qu2.justificationRed}</p>
        </th>
    </tr>
</table>
<!--Test For Loop-->
{#each test as tmp}
    <p>{tmp.qu0.type}</p>
{/each}