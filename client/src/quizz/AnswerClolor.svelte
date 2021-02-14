<script>

    export let color;
    export let checkAnswerColorHandler;

</script>


    <button on:click={() => checkAnswerColorHandler(color)} class="answerColor" style="background-color:{color}">
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
    

</style>