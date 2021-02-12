<script>
    export let answerText;
    export let checkAnswerHandler;
</script>

<style>

</style>

<button on:click={() => checkAnswerHandler(answerText)} class="Answer">
    {answerText}
</button>