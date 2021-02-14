<script>
    export let answerText;
    export let checkAnswerHandler;
    export let bgColor = '#86CAF4';
    export let selected;
</script>

<style>
    button {
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

    .disabled {
        opacity: 0.5;
    }
</style>

<button type="button" 
        on:click={() => checkAnswerHandler(answerText)} 
        style="background-color : {bgColor};" 
        class:disabled="{selected === true}"
>
    {answerText}
</button>