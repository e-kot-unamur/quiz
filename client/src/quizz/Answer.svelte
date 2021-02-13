<script>
    export let answerText;
    export let checkAnswerHandler;
    export let bgColor = '#86CAF4';
</script>

<style>
    .answer{
        display: inline-block;
        width: 45%;
        margin: 10px auto;
        border-radius: 8px;
    }
</style>

<button type="button" on:click={() => checkAnswerHandler(answerText)} class="answer" style="background-color : {bgColor};">
    {answerText}
</button>