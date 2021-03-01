<script>
    export let color;
    export let checkAnswerHandler;
    export let selected;
    export let label;
</script>

<style>
    .answerColor {
        display: inline-block;
        height: 100px;
        width: 30%;
        margin: 10px auto;
        border-radius: 8px;
        font-weight: bold;
        color: white;
    }

    .disabled {
        opacity: 0.4;
    }
</style>

<button on:click={() => checkAnswerHandler(color)} 
    class="answerColor" 
    style="background-color:{color}"
    class:disabled="{selected === true}"
>
    {label}
</button>
