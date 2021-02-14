<script>

    export let color;
    export let checkAnswerHandler;
    export let selected;

</script>

    <button on:click={() => checkAnswerHandler(color)} class="answerColor" style="background-color:{color}"
        class:disabled="{selected === true}">
        <!--{color}-->
    </button>

<style>
    .answerColor {
        display: inline-block;
        height: 100px;
        width: 30%;
        margin: 10px auto;
        border-radius: 8px;
    }

    .disabled {
        opacity: 0.4;
    }
</style>