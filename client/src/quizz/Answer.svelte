<script>
    export let answerText;
    export let checkAnswerHandler;
    export let bgColor = '#86CAF4';
</script>

<style>
    .answer{
        font-family: marine, sans-serif;
        font-size: 1.1em;
        font-weight: bold;
        font-style: normal;
        color : whitesmoke;

        display: inline-block;
        width: 45%;
        margin: 10px auto;
        border-radius: 0px;
        padding: 20px 0 ;
    }
</style>

<button type="button" on:click={() => checkAnswerHandler(answerText)} class="answer" style="background-color : {bgColor};">
    {answerText}
</button>